"""Check that Markdown chapters retain the original inline TeX formulae."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1] / "lectures/markdown"
BOOKS = (
    ("Complex-Analysis-Notes", "Complex Analysis Notes", 7),
    ("Real-Analysis-Notes", "Real Analysis Notes", 5),
)
INLINE_MATH = re.compile(r"(?<!\$)\$(?!\$)(?:\\.|[^$\\])*\$(?!\$)")


def normalize(value: str) -> str:
    return re.sub(r"\s+", "", re.sub(r"(?m)^> ?", "", value))


for repository, stem, count in BOOKS:
    source = (ROOT / "imports" / repository / f"{stem}.tex").read_text(encoding="utf-8")
    body = source.split(r"\begin{document}", 1)[1].split(r"\end{document}", 1)[0]
    body = re.sub(r"\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\}", "", body)
    files = [ROOT / "converted" / f"{repository}.md"]
    files.extend(ROOT / "converted" / f"{repository}-{number:02d}.md" for number in range(1, count + 1))
    markdown = "".join(file.read_text(encoding="utf-8") for file in files)
    markdown = re.sub(r'<details class="chapter-outline">[\s\S]*?</details>', '', markdown)
    original = list(map(normalize, INLINE_MATH.findall(body)))
    converted = list(map(normalize, INLINE_MATH.findall(markdown.replace("$$", ""))))
    if original != converted:
        difference = next((i for i, (a, b) in enumerate(zip(original, converted)) if a != b), min(len(original), len(converted)))
        raise SystemExit(f"{repository}: inline formula mismatch at index {difference}: {len(original)} original, {len(converted)} converted")
    print(f"{repository}: {count} chapters, {len(original)} inline formulae match")
