# HaideMath 学术笔记阅读器 - GitHub Pages 部署指南

## 📁 文件结构

```
haidemath/
├── lectures/
│   ├── markdown/
│   │   ├── viewer.html          # 主页面
│   │   ├── auto-directory.js    # 自动目录生成器
│   │   ├── directory.json       # 可选：手动维护的目录文件
│   │   ├── Set-Theory.md        # 示例：集合论笔记
│   │   ├── Real-Analysis.md     # 示例：实分析笔记
│   │   └── *.md                 # 其他 Markdown 文档
│   └── index.html              # 可选：导航页面
└── README.md
```

## 🚀 快速开始

### 1. 部署到 GitHub Pages

1. 将项目上传到 GitHub 仓库
2. 在仓库设置中启用 GitHub Pages
3. 选择 `main` 分支作为源
4. 访问 `https://your-username.github.io/your-repo/lectures/markdown/viewer.html`

### 2. 添加新文档

只需要将 `.md` 文件上传到 `lectures/markdown/` 目录：

```bash
# 本地开发
git add new-document.md
git commit -m "添加新文档: 线性代数"
git push

# 或者直接在 GitHub 网页界面上传文件
```

### 3. 推荐的文件命名

为了更好的自动分类，建议使用以下命名模式：

- `Set-Theory.md` - 集合论
- `Real-Analysis.md` - 实分析  
- `Complex-Analysis.md` - 复分析
- `Linear-Algebra.md` - 线性代数
- `Abstract-Algebra.md` - 抽象代数
- `Topology.md` - 拓扑学
- `Differential-Geometry.md` - 微分几何
- `Number-Theory.md` - 数论
- `Probability-Theory.md` - 概率论
- `Mathematical-Statistics.md` - 数理统计

## 📝 Markdown 文档格式

### 基本结构

```markdown
# 文档标题

## 章节标题

### 小节标题

普通文本内容...

数学公式：$E = mc^2$

显示公式：
$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$
```

### 特殊内容块

```markdown
\begin{definition}
这是一个定义块...
\end{definition}

\begin{theorem}
这是一个定理块...
\end{theorem}

\begin{example}
这是一个例子块...
\end{example}

\begin{proof}
这是一个证明块...
\end{proof}
```

## 🔧 自动化功能

### 自动发现文档
- 系统会自动扫描目录中的 `.md` 文件
- 从文件内容中提取标题
- 根据文件名和内容自动分类
- 匹配合适的图标

### 自动分类规则
- **实分析**: 包含 "实分析"、"Real Analysis"、"实函数"、"测度" 等关键词
- **复分析**: 包含 "复分析"、"Complex Analysis"、"复变函数" 等关键词  
- **代数学**: 包含 "代数"、"Algebra"、"群论"、"环论" 等关键词
- **几何学**: 包含 "几何"、"Geometry"、"拓扑"、"微分几何" 等关键词
- **概率论**: 包含 "概率"、"统计"、"随机过程" 等关键词

### 自动刷新
- 本地开发环境下会自动检测文件变化
- 生产环境支持手动刷新 (Ctrl+R)

## 🛠️ 高级配置

### 手动维护目录 (可选)

如果需要精确控制文档顺序和分类，可以创建 `directory.json` 文件：

```json
[
  {
    "file": "Set-Theory.md",
    "title": "集合论基础",
    "category": "基础数学",
    "lastModified": "2025-06-28T00:00:00Z"
  },
  {
    "file": "Real-Analysis.md", 
    "title": "实分析教程",
    "category": "数学分析",
    "lastModified": "2025-06-28T00:00:00Z"
  }
]
```

### 开发者工具

在浏览器控制台中可以使用以下命令：

```javascript
// 导出当前目录配置
exportConfig()

// 查看使用说明
getHelp()

// 手动刷新文件列表
refreshFiles()

// 查看文件管理信息
console.log(viewer.autoGenerator.getManagementInfo())
```

## 📱 移动端适配

- 响应式设计，自动适配手机和平板
- 触摸友好的交互界面
- 侧边栏在移动端可折叠

## 🎨 主题定制

支持以下功能：
- 深色/浅色主题切换
- 全屏阅读模式
- 自定义字体和配色

## 🔍 搜索功能

- 实时搜索文档标题
- 支持中英文搜索
- 高亮显示匹配结果

## 📊 使用统计

系统会在控制台显示：
- 当前文档总数
- 各分类文档数量
- 最后更新时间
- 文件管理信息

## 🚨 故障排除

### 文档不显示
1. 检查文件名是否正确
2. 确认文件编码为 UTF-8
3. 查看浏览器控制台错误信息

### 数学公式不渲染
1. 检查 LaTeX 语法是否正确
2. 确认使用 `$...$` 或 `$$...$$` 包围公式
3. 避免在公式中使用特殊 HTML 字符

### 自动分类不准确
1. 在文档标题中包含关键词
2. 或者手动创建 `directory.json` 文件

## 📄 许可证

MIT License - 可自由使用和修改。
