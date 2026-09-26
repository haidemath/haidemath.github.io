# 海德数学

面向海德学院数学专业同学的学习资料站。网站由 HTML、CSS、JavaScript、Markdown 和 PDF 组成，直接发布在 GitHub Pages；论坛使用 Giscus，不需要应用服务器或数据库。

## 内容结构

| 目录 | 内容 |
| --- | --- |
| `courses/` | 课程参考资料 |
| `notes/` | 按学期整理的课程笔记与 PDF |
| `lectures/` | Markdown 专题讲义及在线阅读器 |
| `homework/` | 每周作业 |
| `forum/` | GitHub Discussions 支持的 Giscus 讨论区 |
| `tools/` | 数学工具与学习资源 |
| `assets/` | 公共外观、站内搜索和搜索目录 |

复分析与实分析讲义可在 `lectures/` 的 Markdown 阅读器中按原书章节阅读。正文由两个上游仓库的 LaTeX 源文件生成，公式、定理、练习和示意图均在章节页面展示。原仓库文件按原目录复制到 `lectures/markdown/imports/`，可从“原仓库文件清单”查看；`imports/manifest.json` 记录来源提交和每个文件的 SHA-256，发布前检查会核对原始文件没有被修改。运行 `python scripts/build_analysis_markdown.py` 可重建章节 Markdown。

## 本地预览

在仓库根目录运行：

```sh
python -m http.server 8000
```

访问 `http://localhost:8000/`。请通过 HTTP 预览；直接打开 `file://` 页面时，浏览器可能禁止读取 JSON 和 Markdown。讲义目录的本地自动发现功能如有需要，可单独运行 `python lectures/markdown/serve.py`。

## 更新资料

1. 将资料放入对应目录，并从栏目页添加有效链接。尚未上线的课程请显示“资料整理中”，不要保留空链接。
2. 新增讲义时，同时更新 `lectures/markdown/directory.json`。`id` 用于阅读器地址中的 `md` 参数，`file` 可指向阅读器同目录、`converted/` 或 `imports/` 下的 `.md` 文件。
3. 新增希望被全站搜索找到的资源时，更新 `assets/search-index.json`。搜索只索引这份清单，不会读取或上传 PDF 内容。
4. 发布前运行 `python scripts/check_site.py`，检查站内链接、搜索目录和讲义目录。

站点支持深浅色主题、键盘 `/` 打开搜索、`Esc` 关闭搜索。外部 SharePoint 链接的可访问性需要单独核对。

## 反馈与许可

资料如有错误，请提交 [Issue](https://github.com/haidemath/haidemath.github.io/issues/new)。网站代码使用 [MIT 许可](LICENSE)。`lectures/markdown/imports/` 中的两个原仓库保留各自的 `License`，适用其原有的 LPPL 1.3c 许可；其他课程资料请分别核对来源与使用权限。

