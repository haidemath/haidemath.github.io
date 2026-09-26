(() => {
    const script = document.currentScript;
    const root = new URL('../', script.src);
    const themeKey = 'haidemath-theme';
    const savedTheme = localStorage.getItem(themeKey);
    if (savedTheme === 'dark') document.documentElement.dataset.theme = 'dark';

    const nav = document.querySelector('.navbar');
    if (!nav) return;

    // Resolve root-relative links against the actual Pages base path.
    // This supports both user sites and /repository/ project sites.
    document.querySelectorAll('a[href^="/"]').forEach(link => {
        const path = link.getAttribute('href');
        if (!path.startsWith('//')) link.href = new URL(path.slice(1), root).href;
    });

    const actions = document.createElement('div');
    actions.className = 'site-actions';
    const searchButton = document.createElement('button');
    searchButton.type = 'button';
    searchButton.className = 'site-action';
    searchButton.textContent = '搜索';
    searchButton.setAttribute('aria-label', '搜索站内资源，快捷键 /');
    const themeButton = document.createElement('button');
    themeButton.type = 'button';
    themeButton.className = 'site-action';
    const updateThemeLabel = () => {
        const dark = document.documentElement.dataset.theme === 'dark';
        themeButton.textContent = dark ? '浅色' : '深色';
        themeButton.setAttribute('aria-label', dark ? '切换到浅色主题' : '切换到深色主题');
        themeButton.setAttribute('aria-pressed', String(dark));
    };
    updateThemeLabel();
    themeButton.addEventListener('click', () => {
        const dark = document.documentElement.dataset.theme !== 'dark';
        document.documentElement.dataset.theme = dark ? 'dark' : 'light';
        localStorage.setItem(themeKey, dark ? 'dark' : 'light');
        updateThemeLabel();
    });
    actions.append(searchButton, themeButton);
    nav.append(actions);

    const overlay = document.createElement('div');
    overlay.className = 'site-search';
    overlay.hidden = true;
    overlay.innerHTML = '<div class="site-search-panel" role="dialog" aria-modal="true" aria-labelledby="site-search-title"><div class="site-search-head"><h2 id="site-search-title">搜索站内资源</h2><button type="button" class="site-action" data-close aria-label="关闭搜索">关闭</button></div><input class="site-search-input" type="search" placeholder="搜索课程、笔记、讲义、作业…" aria-label="搜索关键词"><ul class="site-search-results" aria-live="polite"></ul></div>';
    document.body.append(overlay);
    const input = overlay.querySelector('input');
    const results = overlay.querySelector('.site-search-results');
    let index = [];
    let indexPromise;

    const render = () => {
        const query = input.value.trim().toLocaleLowerCase();
        const matches = index.filter(item =>
            `${item.title} ${item.section} ${item.keywords || ''}`.toLocaleLowerCase().includes(query)
        ).slice(0, 30);
        results.replaceChildren();
        if (!matches.length) {
            const empty = document.createElement('li');
            empty.className = 'site-search-empty';
            empty.textContent = query ? '没有找到匹配的资源' : '暂无可搜索资源';
            results.append(empty);
            return;
        }
        for (const item of matches) {
            const li = document.createElement('li');
            const link = document.createElement('a');
            link.href = new URL(item.path, root).href;
            link.textContent = item.title;
            const section = document.createElement('small');
            section.textContent = item.section;
            link.append(section);
            li.append(link);
            results.append(li);
        }
    };
    const close = () => {
        overlay.hidden = true;
        document.body.style.overflow = '';
        searchButton.focus();
    };
    const open = async () => {
        overlay.hidden = false;
        document.body.style.overflow = 'hidden';
        input.focus();
        if (!indexPromise) {
            indexPromise = fetch(new URL('assets/search-index.json', root))
                .then(response => {
                    if (!response.ok) throw new Error(`HTTP ${response.status}`);
                    return response.json();
                });
        }
        try {
            index = await indexPromise;
            render();
        } catch {
            results.replaceChildren();
            const error = document.createElement('li');
            error.className = 'site-search-empty';
            error.textContent = '搜索目录加载失败，请刷新页面重试';
            results.append(error);
            indexPromise = undefined;
        }
    };
    searchButton.addEventListener('click', open);
    input.addEventListener('input', render);
    overlay.querySelector('[data-close]').addEventListener('click', close);
    overlay.addEventListener('click', event => { if (event.target === overlay) close(); });
    document.addEventListener('keydown', event => {
        if (event.key === 'Escape' && !overlay.hidden) close();
        if (event.key === '/' && overlay.hidden && !/input|textarea/i.test(document.activeElement.tagName)) {
            event.preventDefault();
            open();
        }
    });
})();
