"""Check local links and the two hand-maintained indexes before publishing.

Run from the repository root: python scripts/check_site.py
Only Python's standard library is required.
"""

from html.parser import HTMLParser
from hashlib import sha256
import json
from pathlib import Path, PurePosixPath
import re
from urllib.parse import parse_qs, unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
errors = []
lecture_links = []


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        for name in ("href", "src"):
            if name in attributes and attributes[name]:
                self.links.append(attributes[name].strip())


def check_path(path, source):
    if not path.is_relative_to(ROOT):
        errors.append(f"{source}: path escapes the repository: {path}")
    elif not path.exists():
        errors.append(f"{source}: missing {path.relative_to(ROOT)}")


for html_file in ROOT.rglob("*.html"):
    if ".git" in html_file.parts:
        continue
    parser = LinkParser()
    parser.feed(html_file.read_text(encoding="utf-8"))
    for link in parser.links:
        url = urlsplit(link)
        if url.scheme or url.netloc or not url.path:
            continue
        local = unquote(url.path)
        target = (ROOT / local.lstrip("/")) if local.startswith("/") else (html_file.parent / local)
        check_path(target.resolve(), html_file.relative_to(ROOT))
        if target.name == "viewer.html" and "md" in parse_qs(url.query):
            lecture_links.append((parse_qs(url.query)["md"][0], str(html_file.relative_to(ROOT))))

search_file = ROOT / "assets/search-index.json"
search_items = json.loads(search_file.read_text(encoding="utf-8"))
for item in search_items:
    url = urlsplit(item["path"])
    path = url.path
    check_path((ROOT / path).resolve(), "assets/search-index.json")
    if path.endswith("/viewer.html") and "md" in parse_qs(url.query):
        lecture_links.append((parse_qs(url.query)["md"][0], "assets/search-index.json"))

directory_file = ROOT / "lectures/markdown/directory.json"
directory = json.loads(directory_file.read_text(encoding="utf-8"))
ids = set()
for item in directory["files"]:
    file_id = item["id"]
    if file_id in ids:
        errors.append(f"{directory_file.relative_to(ROOT)}: duplicate id {file_id}")
    ids.add(file_id)
    file_name = item["file"]
    parts = PurePosixPath(file_name).parts
    valid_path = (
        parts
        and all(part not in ("", ".", "..") for part in parts)
        and (len(parts) == 1 or (len(parts) > 1 and parts[0] in ("imports", "converted")))
        and "\\" not in file_name
        and "?" not in file_name
        and "#" not in file_name
        and ":" not in file_name
        and "%" not in file_name
        and file_name.lower().endswith(".md")
    )
    if not valid_path:
        errors.append(f"{directory_file.relative_to(ROOT)}: invalid file {file_name}")
    else:
        check_path((directory_file.parent / file_name).resolve(), directory_file.relative_to(ROOT))

for file_id, source in lecture_links:
    if file_id not in ids:
        errors.append(f"{source}: unknown lecture id {file_id}")

for chapter in (directory_file.parent / "converted").glob("*.md"):
    markdown = chapter.read_text(encoding="utf-8")
    for destination in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", markdown):
        url = urlsplit(destination)
        if url.path.endswith("viewer.html"):
            file_id = parse_qs(url.query).get("md", [""])[0]
            if file_id not in ids:
                errors.append(f"{chapter.relative_to(ROOT)}: unknown lecture id {file_id}")
        elif url.path.startswith("figures/"):
            check_path((chapter.parent / unquote(url.path)).resolve(), chapter.relative_to(ROOT))

for catalog in directory_file.parent.glob("*-Notes-Catalog.md"):
    markdown = catalog.read_text(encoding="utf-8")
    destinations = re.findall(r"\]\(<([^>]+)>\)|\]\((viewer\.html\?md=[^)]+)\)", markdown)
    for original, reader in destinations:
        url = urlsplit(original or reader)
        if reader:
            file_id = parse_qs(url.query).get("md", [""])[0]
            if file_id not in ids:
                errors.append(f"{catalog.relative_to(ROOT)}: unknown lecture id {file_id}")
        else:
            check_path((catalog.parent / unquote(url.path)).resolve(), catalog.relative_to(ROOT))

imports = directory_file.parent / "imports"
manifest = json.loads((imports / "manifest.json").read_text(encoding="utf-8"))
import_count = 0
for source in manifest["sources"]:
    source_dir = imports / source["directory"]
    expected = set(source["files"])
    actual = {path.relative_to(source_dir).as_posix() for path in source_dir.rglob("*") if path.is_file()}
    for missing in sorted(expected - actual):
        errors.append(f"{source['directory']}: missing original file {missing}")
    for extra in sorted(actual - expected):
        errors.append(f"{source['directory']}: extra file in original tree {extra}")
    for relative in sorted(expected & actual):
        path = source_dir / relative
        if sha256(path.read_bytes()).hexdigest() != source["files"][relative]:
            errors.append(f"{source['directory']}: changed original file {relative}")
    import_count += len(expected)

if errors:
    print("Site check failed:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print(f"Site check passed: {len(search_items)} search entries, {len(ids)} lecture entries, {import_count} original files unchanged.")
