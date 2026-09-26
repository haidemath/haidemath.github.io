# 讲义目录维护

阅读器在线上只从 `directory.json` 获取讲义清单。每条记录的 `id` 应唯一，`file` 可指向同目录内的 `.md` 文件，或 `imports/` 下的 `.md`、`.pdf` 原版文件。`title`、`category`、`description`、`tags` 用于展示和检索。

添加讲义时，先放入 Markdown 文件，再更新目录。`directory-manager.html` 可帮助生成 JSON，但浏览器无法直接写回仓库；下载后仍需将文件放回本目录。

在仓库根目录运行 `python scripts/check_site.py` 核对目录、搜索条目和站内链接。完整步骤见本目录 [README](README.md)。
