# Markdown 讲义阅读器

`viewer.html` 是 GitHub Pages 上使用的静态 Markdown 阅读器。页面先读取同目录的 `directory.json`，再按其中的 `file` 字段加载 Markdown。公式由 MathJax 渲染，Markdown 由 Marked 解析，并经 DOMPurify 净化。复分析和实分析讲义按原书章节拆分，以减少单页公式量。

## 新增讲义

1. 将 UTF-8 编码的 `.md` 文件放到本目录。
2. 在 `directory.json` 的 `files` 数组中新增条目。`id` 是稳定的链接标识，`file` 是实际文件名。例如：

```json
{
  "id": "New-Lecture",
  "title": "新讲义",
  "file": "New-Lecture.md",
  "category": "专题讲义"
}
```

3. 若要从讲义首页或全站搜索直达该讲义，同步更新 `lectures/index.html` 和 `assets/search-index.json`。
4. 在仓库根目录运行 `python scripts/check_site.py`。

## 原仓库导入

`imports/Complex-Analysis-Notes/` 与 `imports/Real-Analysis-Notes/` 是来源仓库文件的逐字节副本，不在其中修改内容。`imports/manifest.json` 记录来源提交与文件哈希；`Complex-Analysis-Notes-Catalog.md` 和 `Real-Analysis-Notes-Catalog.md` 只是阅读导航，可运行 `python scripts/build_import_catalog.py` 重建。两个原仓库的 `License` 文件保存在各自目录中。

`converted/` 中的 Markdown 与示意图由 `python scripts/build_analysis_markdown.py` 从原仓库 LaTeX 正文生成。复分析共 7 章、实分析共 5 章；生成脚本也会更新 `directory.json` 中的章节入口。原始 PDF 仅留在原仓库文件中，不嵌入 Markdown 阅读器。

## 本地预览

在仓库根目录运行 `python -m http.server 8000`，访问 `http://localhost:8000/lectures/markdown/viewer.html`。`serve.py` 提供可选的本地文件发现 API；GitHub Pages 不运行这个 Python 服务，线上新增讲义必须更新 `directory.json`。

`directory-manager.html` 只能在浏览器内生成并下载新的 JSON。请用下载结果更新仓库中的 `directory.json`，再提交发布。
