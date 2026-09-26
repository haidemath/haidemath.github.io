"""Build readable Markdown from the two original LaTeX lecture manuscripts."""

from __future__ import annotations

import re
import json
from html import escape
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "lectures/markdown/imports"
OUTPUT = ROOT / "lectures/markdown/converted"
BOOKS = (
    ("Complex-Analysis-Notes", "Complex Analysis Notes", "复分析", "2026 年 8 月 28 日"),
    ("Real-Analysis-Notes", "Real Analysis Notes", "实分析", "2025 年 7 月 5 日"),
)
BLOCKS = {
    "definition": "定义",
    "theorem": "定理",
    "lemma": "引理",
    "proposition": "命题",
    "corollary": "推论",
    "example": "例",
    "remark": "注",
    "proof": "证明",
}
LAYOUT = {"center", "flushright"}
SKIP = {
    r"\maketitle", r"\frontmatter", r"\mainmatter", r"\begingroup",
    r"\endgroup", r"\tableofcontents", r"\newpage", r"\Large",
    r"\renewcommand{\familydefault}{\rmdefault}", r"\hspace{2em}",
    r"\btocgroup", r"\etocgroup", r"\UseTocStyle{chapter}{emph}{toc}",
    r"\backmatter",
}
HEADING = re.compile(r"^\\(chapter|section|subsection|subsubsection)\*?\{")
BEGIN = re.compile(r"^\\begin\{([^}]+)\}")
END = re.compile(r"^\\end\{([^}]+)\}")
PAR = re.compile(r"\\par\b")


def braced(text: str, start: int) -> tuple[str, int]:
    assert text[start] == "{"
    depth = 0
    for pos in range(start, len(text)):
        if text[pos] == "{" and (pos == 0 or text[pos - 1] != "\\"):
            depth += 1
        elif text[pos] == "}" and (pos == 0 or text[pos - 1] != "\\"):
            depth -= 1
            if depth == 0:
                return text[start + 1:pos], pos + 1
    raise ValueError(f"Unbalanced braces: {text[:90]}")


def inline(text: str, math_context: bool = False) -> str:
    # Keep all prose and all TeX maths verbatim; only convert text styling.
    text = re.sub(r"\\texorpdfstring\{", r"\\texorpdfstring{", text)
    for command, wrap in (("textbf", "**"), ("textit", "*"), ("emph", "*")):
        token = "\\" + command + "{"
        while token in text:
            start = text.index(token)
            value, end = braced(text, start + len(token) - 1)
            text = text[:start] + wrap + value + wrap + text[end:]
    if "$" not in text and not math_context:
        for command in ("text", "textrm"):
            token = "\\" + command + "{"
            while token in text:
                start = text.index(token)
                value, end = braced(text, start + len(token) - 1)
                text = text[:start] + value + text[end:]
    text = PAR.sub("\n\n", text)
    return text


def render_figure(snippet: str, number: int, destination: Path) -> None:
    if (destination / f"complex-figure-{number}.png").exists():
        return
    preamble = r"""
\documentclass[tikz,border=5pt]{standalone}
\usepackage{amsmath}
\usepackage{tikz}
\definecolor{customcolor}{RGB}{32,178,170}
\definecolor{diagramorange}{RGB}{238,118,0}
\tikzset{
  diagram axis/.style={->,>=stealth,thin,draw=black!72},
  diagram map/.style={->,>=stealth,very thick,draw=black!78},
  diagram source/.style={draw=customcolor,very thick,fill=customcolor!10},
  diagram target/.style={draw=diagramorange,very thick,fill=diagramorange!9},
  diagram point/.style={circle,fill=black,inner sep=1.7pt},
  diagram note/.style={font=\small,text=black!72}
}
\begin{document}
"""
    with tempfile.TemporaryDirectory(prefix="notes-figure-") as temp:
        work = Path(temp)
        name = f"complex-figure-{number}"
        (work / f"{name}.tex").write_text(preamble + snippet + "\n\\end{document}\n", encoding="utf-8")
        subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-halt-on-error", f"{name}.tex"],
            cwd=work, check=True, stdout=subprocess.DEVNULL,
        )
        subprocess.run(
            ["pdftoppm", "-f", "1", "-l", "1", "-r", "180", "-png",
             "-singlefile", f"{name}.pdf", str(destination / name)],
            cwd=work, check=True, stdout=subprocess.DEVNULL,
        )


def convert(name: str, stem: str, chinese: str, publication_date: str) -> list[dict]:
    source_path = SOURCE / name / f"{stem}.tex"
    source = source_path.read_text(encoding="utf-8")
    body = source.split(r"\begin{document}", 1)[1].split(r"\end{document}", 1)[0]
    lines = body.splitlines()
    output: list[str] = [
        f"# {stem.removesuffix(' Notes')}", "",
        "Lecture Notes", "",
        f"作者：Stone Sun  ",
        f"时间：{publication_date}  ",
        "联系方式：hefengzhishui@outlook.com", "",
    ]
    quote: list[str] = []
    lists: list[str] = []
    math = False
    inline_math_open = False
    figure = False
    figure_lines: list[str] = []
    figure_count = 0
    block_counts: dict[str, int] = {block: 0 for block in BLOCKS}
    headings = 0

    def emit(value: str = "") -> None:
        if "\n" in value:
            for part in value.split("\n"):
                emit(part)
            return
        prefix = "> " * len(quote)
        if not value:
            output.append(prefix.rstrip())
        else:
            output.append(prefix + ("  " * len(lists) if lists and not value.startswith(("- ", "1. ")) else "") + value)

    def prose(value: str, math_context: bool = False) -> str:
        result = inline(value, math_context)
        if not math_context:
            pieces = re.split(r"(\$[^$]*\$)", result)
            for index in range(0, len(pieces), 2):
                pieces[index] = (pieces[index]
                    .replace(r"\today", publication_date)
                    .replace(r"\qquad", "　")
                    .replace(r"\quad", " "))
            result = "".join(pieces)
            if result.startswith("Stone Sun" + r"\\"):
                result = result.replace(r"\\", "  ", 1)
        return result

    for line_number, raw in enumerate(lines, 1):
        line = raw.strip()
        if figure:
            figure_lines.append(raw)
            if line == r"\end{tikzpicture}":
                figure = False
                render_figure("\n".join(figure_lines), figure_count, OUTPUT / "figures")
                emit(f"![原讲义示意图 {figure_count}](figures/complex-figure-{figure_count}.png)")
                figure_lines = []
            continue
        if line.startswith(r"\begin{tikzpicture}"):
            figure_count += 1
            figure = True
            figure_lines = [raw]
            continue
        odd_dollars = line.count("$") % 2 == 1
        line_math_context = math or inline_math_open or odd_dollars
        if odd_dollars:
            inline_math_open = not inline_math_open
        if not line:
            emit()
            continue
        if line in SKIP:
            continue
        heading = HEADING.match(line)
        if heading:
            label, end = braced(line, heading.end() - 1)
            if label.startswith(r"\texorpdfstring{"):
                label, _ = braced(label, len(r"\texorpdfstring"))
            level = {"chapter": 2, "section": 3, "subsection": 4, "subsubsection": 5}[heading.group(1)]
            emit()
            emit("#" * level + " " + prose(label))
            emit()
            headings += 1
            continue
        match = BEGIN.match(line)
        if match:
            env = match.group(1)
            rest = line[match.end():].strip()
            if env in BLOCKS:
                emit()
                quote.append(env)
                block_counts[env] += 1
                emit(f"**{BLOCKS[env]}**")
                emit()
            elif env in ("itemize", "enumerate"):
                lists.append(env)
                emit()
            elif env in LAYOUT:
                pass
            elif env == "equation*":
                emit("$$")
            elif env == "align*":
                emit("$$")
                emit(r"\begin{aligned}")
            elif env in ("cases", "aligned", "array", "vmatrix"):
                emit(line)
                continue
            else:
                raise ValueError(f"{name}:{line_number}: unknown environment {env}")
            if rest:
                emit(prose(rest))
            continue
        match = END.match(line)
        if match:
            env = match.group(1)
            if env in BLOCKS:
                assert quote.pop() == env
                emit()
            elif env in ("itemize", "enumerate"):
                assert lists.pop() == env
                emit()
            elif env in LAYOUT:
                pass
            elif env == "equation*":
                emit("$$")
            elif env == "align*":
                emit(r"\end{aligned}")
                emit("$$")
            elif env in ("cases", "aligned", "array", "vmatrix"):
                emit(line)
            else:
                raise ValueError(f"{name}:{line_number}: unknown environment {env}")
            continue
        if line == r"\[":
            assert not math
            math = True
            emit("$$")
            continue
        if line == r"\]":
            assert math
            math = False
            emit("$$")
            continue
        if line.startswith(r"\item"):
            if not lists:
                raise ValueError(f"{name}:{line_number}: item outside list")
            marker = "- " if lists[-1] == "itemize" else "1. "
            emit(marker + prose(line[5:].strip()))
            continue
        if line.startswith("%"):
            continue
        emit(prose(line, line_math_context))

    assert not quote and not lists and not math and not inline_math_open and not figure
    assert figure_count == source.count(r"\begin{tikzpicture}")
    assert headings == sum(bool(HEADING.match(line.strip())) for line in lines)
    for env, count in block_counts.items():
        assert count == body.count(r"\begin{" + env + "}")
    chapter_starts = [i for i, line in enumerate(output) if line.startswith("## ")]
    assert chapter_starts
    chapters = []
    chapter_sections = []
    for number, start in enumerate(chapter_starts, 1):
        end = chapter_starts[number] if number < len(chapter_starts) else len(output)
        title = output[start][3:]
        file_name = f"{name}-{number:02d}.md"
        file_id = f"{name}-Chapter-{number}"
        chapters.append({"id": file_id, "title": title, "file": f"converted/{file_name}", "category": f"{chinese} · 正文章节", "icon": "fas fa-bookmark"})
        chapter_text = output[start:end]
        sections = []
        for heading_line in chapter_text:
            if re.match(r"^#{3,5} ", heading_line):
                sections.append((len(heading_line) - len(heading_line.lstrip("#")), heading_line.lstrip("# ")))
        chapter_sections.append(sections)
        if number > 1:
            chapter_text = [f"[← 上一章](../viewer.html?md={name}-Chapter-{number-1})", ""] + chapter_text
        chapter_text.extend(["", f"[目录与前言](../viewer.html?md={name})"])
        if number < len(chapter_starts):
            chapter_text[-1] += f" · [下一章 →](../viewer.html?md={name}-Chapter-{number+1})"
        (OUTPUT / file_name).write_text("\n".join(chapter_text).strip() + "\n", encoding="utf-8")
    introduction = output[:8] + ["", "## 章节目录", ""]
    for number, entry in enumerate(chapters, 1):
        introduction.extend([
            '<details class="chapter-outline">',
            f'<summary>第 {number} 章 · {escape(entry["title"])}</summary>',
            f'<a class="chapter-read" href="../viewer.html?md={entry["id"]}">阅读本章 →</a>',
            "<ul>",
        ])
        for section_number, (level, title) in enumerate(chapter_sections[number - 1], 1):
            href = f'../viewer.html?md={entry["id"]}#section-{section_number}'
            introduction.append(f'<li class="outline-level-{level}"><a href="{href}">{escape(title)}</a></li>')
        introduction.extend(["</ul>", "</details>", ""])
    foreword = [line for line in output[8:chapter_starts[0]] if line.strip() != "**前言**"]
    introduction.extend(["", "## 前言", ""] + foreword)
    output_path = OUTPUT / f"{name}.md"
    output_path.write_text("\n".join(introduction).strip() + "\n", encoding="utf-8")
    print(f"{output_path.relative_to(ROOT)}: {len(chapters)} chapters, {headings} headings, {sum(block_counts.values())} content blocks, {figure_count} diagrams")
    return chapters


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "figures").mkdir(exist_ok=True)
    chapter_entries = []
    for book in BOOKS:
        chapter_entries.extend(convert(*book))
    directory_path = OUTPUT.parent / "directory.json"
    directory = json.loads(directory_path.read_text(encoding="utf-8"))
    entries = [entry for entry in directory["files"] if "-Chapter-" not in entry["id"]]
    for name, _, chinese, _ in BOOKS:
        main_entry = next(entry for entry in entries if entry["id"] == name)
        main_entry["title"] = f"{chinese}讲义 · 目录与前言"
        main_entry["description"] = "由原仓库 LaTeX 正文转换，点击目录阅读完整章节"
        position = entries.index(main_entry) + 1
        chapters = [entry for entry in chapter_entries if entry["id"].startswith(name + "-Chapter-")]
        for entry in chapters:
            entry["lastModified"] = main_entry.get("lastModified")
        entries[position:position] = chapters
    directory["files"] = entries
    directory_path.write_text(json.dumps(directory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
