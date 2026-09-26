"""Regenerate reader indexes for the verbatim imported source repositories."""

import json
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
IMPORTS = ROOT / "lectures/markdown/imports"
manifest = json.loads((IMPORTS / "manifest.json").read_text(encoding="utf-8"))

titles = {
    "Complex-Analysis-Notes": ("复分析原仓库文件", "Complex-Analysis-Notes"),
    "Real-Analysis-Notes": ("实分析原仓库文件", "Real-Analysis-Notes"),
}
reader_links = {
    "Complex-Analysis-Notes": [
        ("阅读完整讲义", "Complex-Analysis-Notes"),
        ("阅读小测 1", "Complex-Analysis-Quiz-1"),
        ("阅读小测 2", "Complex-Analysis-Quiz-2"),
        ("阅读小测解答", "Complex-Analysis-Quiz-Answers"),
    ],
    "Real-Analysis-Notes": [
        ("阅读完整讲义", "Real-Analysis-Notes"),
    ],
}

for source in manifest["sources"]:
    directory = source["directory"]
    title, output_name = titles[directory]
    lines = [
        f"# {title}",
        "",
        "以下文件从原仓库逐字节复制，文件名和子目录保持不变。此页仅提供阅读导航。",
        "",
        f"- 原仓库：[{source['repository']}]({source['repository']})",
        f"- 来源提交：`{source['commit']}`",
        f"- 文件数：{len(source['files'])}",
        "",
        "## 阅读入口",
        "",
    ]
    for label, file_id in reader_links[directory]:
        lines.append(f"- [{label}](viewer.html?md={file_id})")
    lines.extend(["", "## 原始文件", ""])
    for relative in source["files"]:
        url = quote(f"imports/{directory}/{relative}", safe="/")
        lines.append(f"- [{relative}](<{url}>)")
    lines.append("")
    output = IMPORTS.parent / f"{output_name}-Catalog.md"
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {output.relative_to(ROOT)}")
