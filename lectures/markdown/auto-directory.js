/**
 * 自动目录生成脚本
 * 用于GitHub Pages等静态网站，自动扫描Markdown文件并生成目录
 */

class AutoDirectoryGenerator {
    constructor() {
        this.markdownFiles = [];
        this.baseUrl = window.location.origin + window.location.pathname.replace(/[^/]*$/, '');
    }

    /**
     * 自动发现并加载Markdown文件
     */
    async discoverMarkdownFiles() {
        try {
            // 优先从手动维护的目录文件加载（最快）
            console.log('🚀 尝试加载手动维护的目录文件...');
            const manualDirectory = await this.loadManualDirectory();
            if (manualDirectory && manualDirectory.length > 0) {
                this.markdownFiles = manualDirectory;
                console.log(`✅ 手动目录: 成功加载 ${this.markdownFiles.length} 个文档`);
                return this.markdownFiles;
            }

            // 回退：尝试本地环境的API发现（中等速度）
            if (this.isLocalEnvironment()) {
                console.log('🔍 回退到API自动发现...');
                const localFiles = await this.discoverLocalFiles();
                if (localFiles && localFiles.length > 0) {
                    this.markdownFiles = localFiles;
                    console.log(`✅ API发现: 成功获取 ${this.markdownFiles.length} 个文档`);
                    return this.markdownFiles;
                }
            }

            // 最后回退：模式匹配发现（最慢）
            console.log('🔍 回退到模式匹配自动发现...');
            await this.autoDiscoverFiles();
            console.log(`✅ 模式匹配: 最终获取 ${this.markdownFiles.length} 个文档`);
            
            return this.markdownFiles;
        } catch (error) {
            console.error('❌ 发现文件失败:', error);
            return [];
        }
    }

    /**
     * 检查是否为本地开发环境
     */
    isLocalEnvironment() {
        return window.location.hostname === 'localhost' || 
               window.location.hostname === '127.0.0.1' || 
               window.location.hostname === '';
    }

    /**
     * 在本地环境中真实读取目录内容
     */
    async discoverLocalFiles() {
        try {
            // 尝试使用增强的服务器端点
            const response = await fetch('./api/files');
            if (response.ok) {
                const data = await response.json();
                if (data.success && data.files) {
                    console.log(`🎉 成功从服务器API获取到 ${data.files.length} 个文件`);
                    return this.processServerFiles(data.files);
                }
            }
        } catch (error) {
            console.log('无法从服务器API获取文件列表，使用模式匹配方法:', error.message);
        }

        // 回退到增强的模式匹配
        return await this.enhancedAutoDiscover();
    }

    /**
     * 处理服务器返回的文件列表
     */
    processServerFiles(serverFiles) {
        return serverFiles.map(file => ({
            id: this.getFileId(file.file),
            title: file.title,
            file: file.file,
            lastModified: file.lastModified,
            category: this.getCategoryFromTitle(file.title),
            icon: this.getIconFromTitle(file.title),
            content: file.preview || '',
            size: file.size
        })).sort((a, b) => a.title.localeCompare(b.title, 'zh-CN'));
    }

    /**
     * 从文件路径获取文件ID
     */
    getFileId(filePath) {
        return filePath.replace(/^.*\//, '').replace(/\.md$/, '');
    }

    /**
     * 增强的自动发现（扫描当前目录中所有可能的文件）
     */
    async enhancedAutoDiscover() {
        console.log('🔍 使用增强扫描模式发现文件...');
        
        // 通过分析当前页面或已知信息获取文件列表
        const result = [];
        
        // 尝试通过错误页面反向工程获取文件列表
        const testFiles = await this.scanForExistingFiles();
        
        for (const file of testFiles) {
            try {
                const response = await fetch(`${file}.md`);
                if (response.ok) {
                    const content = await response.text();
                    const title = this.extractTitleFromContent(content, file);
                    
                    result.push({
                        id: file,
                        title: title,
                        file: `${file}.md`,
                        lastModified: response.headers.get('Last-Modified') || new Date().toISOString(),
                        category: this.getCategoryFromTitle(title),
                        icon: this.getIconFromTitle(title),
                        content: content.substring(0, 200) + '...'
                    });
                    
                    console.log(`✅ 发现文件: ${file}.md - ${title}`);
                }
            } catch (error) {
                // 文件不存在
            }
        }
        
        return result.sort((a, b) => a.title.localeCompare(b.title, 'zh-CN'));
    }

    /**
     * 扫描已存在的文件
     */
    async scanForExistingFiles() {
        // 首先扫描当前目录中确实存在的文件
        const definitelyExists = [];
        const possibleFiles = [
            'Set-Theory',
            'MathJax-Test', 
            'LaTeX-Test',
            'Simple-Cases-Test',
            'Real-Analysis',
            'Complex-Analysis',
            'Linear-Algebra',
            'Abstract-Algebra',
            'Topology',
            'Differential-Geometry',
            'Number-Theory',
            'Probability-Theory',
            'Mathematical-Statistics',
            'Functional-Analysis',
            'Measure-Theory',
            'Calculus',
            'Advanced-Calculus',
            'Numerical-Analysis'
        ];

        // 并行检查文件存在性（提高速度）
        const checks = possibleFiles.map(async (file) => {
            try {
                const response = await fetch(`${file}.md`, { method: 'HEAD' });
                return response.ok ? file : null;
            } catch {
                return null;
            }
        });

        const results = await Promise.all(checks);
        return results.filter(file => file !== null);
    }

    /**
     * 加载手动维护的目录文件
     */
    async loadManualDirectory() {
        try {
            const response = await fetch('./directory.json', { cache: 'no-store' });
            if (response.ok) {
                const data = await response.json();
                
                // 验证目录文件格式
                if (!data.files || !Array.isArray(data.files)) {
                    console.warn('⚠️ 目录文件格式不正确');
                    return null;
                }

                console.log(`📁 目录文件信息: ${data.title || '数学笔记目录'}`);
                console.log(`📅 最后更新: ${data.lastUpdate || '未知'}`);
                
                // 处理文件列表
                const processedFiles = data.files.map(file => ({
                    id: file.id,
                    title: file.title,
                    file: file.file,
                    lastModified: file.lastModified || new Date().toISOString(),
                    category: file.category || '其他',
                    icon: file.icon || this.getIconFromTitle(file.title),
                    description: file.description || '',
                    tags: file.tags || []
                }));

                return processedFiles;
            }
        } catch (error) {
            console.log('📄 未找到手动目录文件，将尝试其他方式');
        }
        return null;
    }

    /**
     * 尝试加载预定义的目录文件（旧版本兼容）
     */
    async loadPredefinedDirectory() {
        try {
            const response = await fetch('../directory.json');
            if (response.ok) {
                const data = await response.json();
                return data.map(file => ({
                    id: file.file.split('/').pop().replace('.md', ''),
                    title: file.title,
                    file: file.file,
                    lastModified: file.lastModified || new Date().toISOString(),
                    category: this.getCategoryFromTitle(file.title),
                    icon: this.getIconFromTitle(file.title)
                }));
            }
        } catch (error) {
            console.log('📄 无法加载旧版预定义目录');
        }
        return null;
    }

    /**
     * 自动发现Markdown文件 (改进版本)
     */
    async autoDiscoverFiles() {
        // 首先尝试读取当前目录中实际存在的文件
        const knownFiles = [
            'Set-Theory',
            'MathJax-Test', 
            'LaTeX-Test',
            'Simple-Cases-Test'
        ];

        // 扩展的数学笔记文件名模式
        const commonPatterns = [
            'Real-Analysis', 
            'Complex-Analysis',
            'Linear-Algebra',
            'Abstract-Algebra',
            'Topology',
            'Differential-Geometry',
            'Number-Theory',
            'Probability-Theory',
            'Mathematical-Statistics',
            'Functional-Analysis',
            'Measure-Theory',
            'Calculus',
            'Advanced-Calculus',
            'Numerical-Analysis',
            'Optimization',
            'Graph-Theory',
            'Combinatorics',
            'Logic',
            'Category-Theory'
        ];

        // 合并已知文件和常见模式
        const allPatterns = [...new Set([...knownFiles, ...commonPatterns])];

        for (const pattern of allPatterns) {
            try {
                const response = await fetch(`${pattern}.md`);
                if (response.ok) {
                    const content = await response.text();
                    const title = this.extractTitleFromContent(content, pattern);
                    
                    this.markdownFiles.push({
                        id: pattern,
                        title: title,
                        file: `${pattern}.md`,
                        lastModified: response.headers.get('Last-Modified') || new Date().toISOString(),
                        category: this.getCategoryFromTitle(title),
                        icon: this.getIconFromTitle(title),
                        content: content.substring(0, 200) + '...' // 预览内容
                    });
                    
                    console.log(`✅ 发现文件: ${pattern}.md - ${title}`);
                }
            } catch (error) {
                // 文件不存在，忽略
                console.log(`❌ 文件不存在: ${pattern}.md`);
            }
        }

        // 按标题排序
        this.markdownFiles.sort((a, b) => a.title.localeCompare(b.title, 'zh-CN'));
        
        console.log(`📚 总共发现 ${this.markdownFiles.length} 个Markdown文件`);
    }

    /**
     * 从Markdown内容中提取标题
     */
    extractTitleFromContent(content, fallbackName) {
        // 尝试从第一个# 标题中提取
        const titleMatch = content.match(/^#\s+(.+)$/m);
        if (titleMatch) {
            return titleMatch[1].trim();
        }

        // 尝试从HTML title标签中提取
        const htmlTitleMatch = content.match(/<title>([^<]+)<\/title>/i);
        if (htmlTitleMatch) {
            return htmlTitleMatch[1].trim();
        }

        // 使用文件名作为回退
        return this.formatFileName(fallbackName);
    }

    /**
     * 格式化文件名为可读标题
     */
    formatFileName(fileName) {
        return fileName
            .replace(/[-_]/g, ' ')
            .replace(/\b\w/g, l => l.toUpperCase())
            .replace(/\s+/g, ' ')
            .trim();
    }

    /**
     * 根据标题获取分类
     */
    getCategoryFromTitle(title) {
        const categories = {
            '实分析': ['实分析', 'Real Analysis', '实函数', '测度'],
            '复分析': ['复分析', 'Complex Analysis', '复变函数', '解析函数'],
            '代数学': ['代数', 'Algebra', '群论', '环论', '域论', '线性代数'],
            '几何学': ['几何', 'Geometry', '拓扑', 'Topology', '微分几何'],
            '概率论': ['概率', 'Probability', '统计', 'Statistics', '随机过程'],
            '数论': ['数论', 'Number Theory', '整数', '素数'],
            '集合论': ['集合', 'Set Theory', '基础数学']
        };

        for (const [category, keywords] of Object.entries(categories)) {
            if (keywords.some(keyword => title.includes(keyword))) {
                return category;
            }
        }
        return '其他';
    }

    /**
     * 根据标题获取图标
     */
    getIconFromTitle(title) {
        if (title.includes('定理') || title.includes('理论') || title.includes('Theory')) return 'fas fa-flask';
        if (title.includes('例题') || title.includes('练习') || title.includes('习题')) return 'fas fa-calculator';
        if (title.includes('证明') || title.includes('Proof')) return 'fas fa-check-circle';
        if (title.includes('分析') || title.includes('Analysis')) return 'fas fa-chart-line';
        if (title.includes('代数') || title.includes('Algebra')) return 'fas fa-square-root-alt';
        if (title.includes('几何') || title.includes('Geometry')) return 'fas fa-shapes';
        if (title.includes('概率') || title.includes('统计') || title.includes('Probability')) return 'fas fa-dice';
        if (title.includes('集合') || title.includes('Set')) return 'fas fa-layer-group';
        return 'fas fa-file-text';
    }

    /**
     * 生成目录JSON (用于开发者手动维护)
     */
    generateDirectoryJson() {
        const directory = this.markdownFiles.map(file => ({
            file: file.file,
            title: file.title,
            lastModified: file.lastModified,
            category: file.category
        }));

        return JSON.stringify(directory, null, 2);
    }

    /**
     * 检查文件是否存在
     */
    async fileExists(fileName) {
        try {
            const response = await fetch(fileName, { method: 'HEAD' });
            return response.ok;
        } catch {
            return false;
        }
    }

    /**
     * 生成文件管理信息
     */
    getManagementInfo() {
        return {
            totalFiles: this.markdownFiles.length,
            categories: [...new Set(this.markdownFiles.map(f => f.category))],
            lastUpdate: new Date().toISOString(),
            files: this.markdownFiles.map(f => ({
                name: f.file,
                title: f.title,
                category: f.category
            }))
        };
    }

    /**
     * 获取目录管理界面数据
     */
    getDirectoryManagementData() {
        return {
            totalFiles: this.markdownFiles.length,
            categories: [...new Set(this.markdownFiles.map(f => f.category))],
            lastUpdate: new Date().toISOString(),
            files: this.markdownFiles,
            usage: {
                manual: '手动维护模式 - 快速加载',
                api: '本地API模式 - 自动发现',
                pattern: '模式匹配模式 - 兼容模式'
            }
        };
    }

    /**
     * 生成新的目录JSON文件内容
     */
    generateDirectoryJsonContent(includeAllDiscovered = false) {
        const directoryData = {
            title: "数学笔记目录",
            description: "手动维护的Markdown文件目录 - 快速加载模式",
            lastUpdate: new Date().toISOString(),
            files: this.markdownFiles.map(file => ({
                id: file.id,
                title: file.title,
                file: file.file,
                category: file.category,
                icon: file.icon,
                description: file.description || `${file.title}的学习笔记`,
                tags: file.tags || [file.category],
                lastModified: file.lastModified
            })),
            categories: [
                {
                    id: "real-analysis",
                    name: "实分析",
                    icon: "fas fa-chart-line",
                    color: "#3498db"
                },
                {
                    id: "complex-analysis", 
                    name: "复分析",
                    icon: "fas fa-infinity",
                    color: "#9b59b6"
                },
                {
                    id: "algebra",
                    name: "代数学", 
                    icon: "fas fa-square-root-alt",
                    color: "#e74c3c"
                },
                {
                    id: "geometry",
                    name: "几何学",
                    icon: "fas fa-shapes", 
                    color: "#f39c12"
                },
                {
                    id: "probability",
                    name: "概率论",
                    icon: "fas fa-dice",
                    color: "#27ae60"
                },
                {
                    id: "test-docs",
                    name: "测试文档",
                    icon: "fas fa-flask",
                    color: "#95a5a6"
                }
            ],
            usage: {
                note: "要添加新文档，请将文件信息添加到files数组中",
                example: {
                    id: "example-file",
                    title: "示例文档标题", 
                    file: "example-file.md",
                    category: "实分析",
                    icon: "fas fa-file-text",
                    description: "文档描述",
                    tags: ["标签1", "标签2"],
                    lastModified: "2025-06-29T00:00:00.000Z"
                }
            }
        };

        return JSON.stringify(directoryData, null, 2);
    }

    /**
     * 添加新文档到目录
     */
    addDocumentToDirectory(docInfo) {
        const newDoc = {
            id: docInfo.id || docInfo.file.replace('.md', ''),
            title: docInfo.title,
            file: docInfo.file,
            category: docInfo.category || '其他',
            icon: docInfo.icon || this.getIconFromTitle(docInfo.title),
            description: docInfo.description || `${docInfo.title}的学习笔记`,
            tags: docInfo.tags || [docInfo.category],
            lastModified: docInfo.lastModified || new Date().toISOString()
        };

        // 避免重复添加
        const existingIndex = this.markdownFiles.findIndex(f => f.id === newDoc.id);
        if (existingIndex >= 0) {
            this.markdownFiles[existingIndex] = newDoc;
            console.log(`📝 更新文档: ${newDoc.title}`);
        } else {
            this.markdownFiles.push(newDoc);
            console.log(`➕ 添加文档: ${newDoc.title}`);
        }

        // 重新排序
        this.markdownFiles.sort((a, b) => a.title.localeCompare(b.title, 'zh-CN'));
        
        return newDoc;
    }
}

// 导出给主应用使用
window.AutoDirectoryGenerator = AutoDirectoryGenerator;
