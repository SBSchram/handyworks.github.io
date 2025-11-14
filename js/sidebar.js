// Sidebar Component
// Creates consistent sidebar with newsletters, search, and pages navigation

(function() {
    'use strict';
    
    function createSidebar() {
        const sidebar = document.createElement('aside');
        sidebar.className = 'sidebar';
        
        sidebar.innerHTML = `
            <div class="sidebar-section">
                <h3>Newsletters</h3>
                <ul class="sidebar-list">
                    <li><a href="newsletters.html">View All Newsletters</a></li>
                    <li><a href="newsletters/W_17.pdf" target="_blank">Winter 2017</a></li>
                    <li><a href="newsletters/W_16.pdf" target="_blank">Winter 2016</a></li>
                    <li><a href="newsletters/W_15.pdf" target="_blank">Winter 2015</a></li>
                    <li><a href="newsletters/W_14.pdf" target="_blank">Winter 2014</a></li>
                    <li><a href="newsletters/W_13.pdf" target="_blank">Winter 2013</a></li>
                    <li><a href="newsletters/W_12.pdf" target="_blank">Winter 2012</a></li>
                    <li><a href="newsletters/W_11.pdf" target="_blank">Winter 2011</a></li>
                    <li><a href="newsletters/W_10.pdf" target="_blank">Winter 2010</a></li>
                    <li><a href="newsletters/W_09.pdf" target="_blank">Winter 2009</a></li>
                    <li><a href="newsletters/W_08.pdf" target="_blank">Winter 2008</a></li>
                </ul>
            </div>
            
            <div class="sidebar-section">
                <form class="search-form" id="blog-search-form">
                    <input type="text" placeholder="Search ..." name="search" id="blog-search-input">
                </form>
            </div>
            
            <div class="sidebar-section">
                <h3>Pages</h3>
                <ul class="sidebar-list">
                    <li><a href="about.html">About Us</a></li>
                    <li><a href="contact.html">Contact Us</a></li>
                    <li><a href="faq.html">FAQ</a></li>
                    <li><a href="features.html">Features</a></li>
                    <li><a href="partners.html">Partners</a></li>
                    <li><a href="story.html">The HandyWorks Story</a></li>
                    <li><a href="downloads.html">Upgrades & Downloads</a></li>
                    <li><a href="legacy.html">Legacy</a></li>
                </ul>
            </div>
        `;
        
        return sidebar;
    }
    
    function initSidebar() {
        const main = document.querySelector('main');
        if (!main) return;
        
        // Check if sidebar already exists
        if (document.querySelector('.sidebar')) return;
        
        // Check if page should have sidebar
        const currentPage = window.location.pathname.split('/').pop() || 'index.html';
        const pagesWithSidebar = ['index.html', 'blog.html', 'downloads.html', 'about.html'];
        
        if (pagesWithSidebar.includes(currentPage)) {
            // Wrap main content in content-wrapper if not already
            let contentWrapper = document.querySelector('.content-wrapper');
            if (!contentWrapper) {
                contentWrapper = document.createElement('div');
                contentWrapper.className = 'content-wrapper';
                
                // Move main content into wrapper
                const mainContent = document.createElement('div');
                mainContent.className = 'main-content';
                
                while (main.firstChild) {
                    mainContent.appendChild(main.firstChild);
                }
                
                contentWrapper.appendChild(mainContent);
                main.appendChild(contentWrapper);
            }
            
            // Add sidebar
            const sidebar = createSidebar();
            contentWrapper.appendChild(sidebar);
            
            // Initialize search functionality
            initSearch();
        }
    }
    
    function initSearch() {
        const searchInput = document.getElementById('blog-search-input');
        const searchForm = document.getElementById('blog-search-form');
        
        if (!searchInput || !searchForm) return;
        
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            performSearch(searchInput.value);
        });
        
        // Real-time search as user types (optional)
        searchInput.addEventListener('input', function() {
            if (this.value.length >= 2) {
                performSearch(this.value);
            } else {
                clearSearch();
            }
        });
    }
    
    function performSearch(query) {
        if (!query || query.trim().length < 2) {
            clearSearch();
            return;
        }
        
        const searchTerm = query.toLowerCase().trim();
        const blogEntries = document.querySelectorAll('.blog-post-summary');
        
        blogEntries.forEach(entry => {
            const title = entry.querySelector('h3 a')?.textContent?.toLowerCase() || '';
            const excerpt = entry.querySelector('.post-excerpt')?.textContent?.toLowerCase() || '';
            const date = entry.querySelector('.post-date')?.textContent?.toLowerCase() || '';
            
            const matches = title.includes(searchTerm) || 
                          excerpt.includes(searchTerm) || 
                          date.includes(searchTerm);
            
            if (matches) {
                entry.style.display = '';
                entry.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            } else {
                entry.style.display = 'none';
            }
        });
        
        // Show/hide year headers based on visible entries
        const yearHeaders = document.querySelectorAll('.blog-posts h2');
        yearHeaders.forEach(header => {
            let hasVisibleEntries = false;
            let nextElement = header.nextElementSibling;
            
            while (nextElement && nextElement.tagName !== 'H2') {
                if (nextElement.classList.contains('blog-post-summary') && 
                    nextElement.style.display !== 'none') {
                    hasVisibleEntries = true;
                    break;
                }
                nextElement = nextElement.nextElementSibling;
            }
            
            header.style.display = hasVisibleEntries ? '' : 'none';
        });
    }
    
    function clearSearch() {
        const blogEntries = document.querySelectorAll('.blog-post-summary');
        blogEntries.forEach(entry => {
            entry.style.display = '';
        });
        
        const yearHeaders = document.querySelectorAll('.blog-posts h2');
        yearHeaders.forEach(header => {
            header.style.display = '';
        });
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initSidebar);
    } else {
        initSidebar();
    }
})();

