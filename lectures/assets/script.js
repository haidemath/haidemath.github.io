// This file contains JavaScript code that handles the loading and rendering of the Markdown files.

document.addEventListener("DOMContentLoaded", function() {
    const markdownContainer = document.getElementById("markdown-content");

    function loadMarkdown(file) {
        fetch(file)
            .then(response => {
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                return response.text();
            })
            .then(text => {
                markdownContainer.innerHTML = marked(text);
            })
            .catch(error => {
                console.error("There was a problem with the fetch operation:", error);
            });
    }

    const markdownFiles = [
        { title: "Introduction", file: "markdown/introduction.md" },
        { title: "Error Analysis", file: "markdown/error-analysis.md" },
        { title: "Interpolation", file: "markdown/interpolation.md" },
        { title: "Numerical Integration", file: "markdown/numerical-integration.md" },
        { title: "Linear Systems", file: "markdown/linear-systems.md" }
    ];

    const nav = document.getElementById("markdown-nav");
    markdownFiles.forEach(item => {
        const link = document.createElement("a");
        link.href = "#";
        link.textContent = item.title;
        link.addEventListener("click", function() {
            loadMarkdown(item.file);
        });
        nav.appendChild(link);
    });

    // Load the first markdown file by default
    loadMarkdown(markdownFiles[0].file);
});