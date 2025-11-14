// Blog Post Expansion Script
// Loads and displays blog post content inline when clicked

(function() {
    'use strict';
    
    // Cache for loaded posts
    const postCache = {};
    
    // Initialize when DOM is ready
    function init() {
        const blogEntries = document.querySelectorAll('.blog-post-summary');
        
        blogEntries.forEach(entry => {
            const link = entry.querySelector('a');
            if (!link) return;
            
            const postUrl = link.getAttribute('href');
            if (!postUrl) return;
            
            // Prevent default navigation
            link.addEventListener('click', function(e) {
                e.preventDefault();
                togglePost(entry, postUrl);
            });
            
            // Add clickable class
            link.style.cursor = 'pointer';
        });
    }
    
    // Toggle post expansion
    function togglePost(entry, postUrl) {
        const expandedContent = entry.querySelector('.blog-post-expanded');
        
        // If already expanded, collapse it
        if (expandedContent) {
            expandedContent.remove();
            entry.classList.remove('expanded');
            return;
        }
        
        // Expand it
        entry.classList.add('expanding');
        
        // Load post content
        loadPostContent(postUrl).then(content => {
            if (content) {
                displayPost(entry, content);
            }
            entry.classList.remove('expanding');
        }).catch(error => {
            console.error('Error loading post:', error);
            entry.classList.remove('expanding');
            // Fallback: navigate to the post
            window.location.href = postUrl;
        });
    }
    
    // Load post content
    function loadPostContent(url) {
        // Check cache first
        if (postCache[url]) {
            return Promise.resolve(postCache[url]);
        }
        
        return fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to load post');
                }
                return response.text();
            })
            .then(html => {
                // Parse the HTML to extract post content
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                
                const postContent = doc.querySelector('.post-content');
                if (!postContent) {
                    throw new Error('Post content not found');
                }
                
                // Clean up the content (remove WordPress comments, etc.)
                let content = postContent.innerHTML;
                content = content.replace(/<!--\s*wp:[^>]*-->/g, '');
                content = content.replace(/<!--\s*\/wp:[^>]*-->/g, '');
                
                // Cache it
                postCache[url] = content;
                
                return content;
            });
    }
    
    // Display post content
    function displayPost(entry, content) {
        const expandedDiv = document.createElement('div');
        expandedDiv.className = 'blog-post-expanded';
        expandedDiv.innerHTML = `<div class="post-content">${content}</div>`;
        
        // Insert after the entry's content
        entry.appendChild(expandedDiv);
        entry.classList.add('expanded');
        
        // Smooth scroll to expanded content
        setTimeout(() => {
            expandedDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }, 100);
    }
    
    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();

