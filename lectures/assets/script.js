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

    function loadDirectory() {
        return fetch('directory.json')
            .then(response => {
                if (!response.ok) {
                    throw new Error("Failed to load directory.json");
                }
                return response.json();
            })
            .catch(error => {
                console.error("Error loading directory:", error);
                return [];
            });
    }

    function createNavigation(markdownFiles) {
        const nav = document.getElementById("markdown-nav");
        nav.innerHTML = ''; // Clear existing navigation
        
        markdownFiles.forEach(item => {
            const link = document.createElement("a");
            link.href = "#";
            link.textContent = item.title;
            link.addEventListener("click", function() {
                loadMarkdown(item.file);
            });
            nav.appendChild(link);
        });

        // Load the first markdown file by default if available
        if (markdownFiles.length > 0) {
            loadMarkdown(markdownFiles[0].file);
        }
    }

    // Initialize the application
    loadDirectory().then(markdownFiles => {
        createNavigation(markdownFiles);
    });
});