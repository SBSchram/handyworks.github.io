// Header and Footer inclusion for DRY principle
(function() {
    'use strict';
    
    // Function to initialize header and footer
    function initHeaderFooter() {
        console.log('Initializing header and footer...');
        
        // Create header HTML
        const headerHTML = `
            <div class="header-container">
                <div class="site-title">
                    <h1>HandyWorks</h1>
                    <p>Chiropractic Office Management Software</p>
                </div>
            </div>
            <nav>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="about.html">About</a></li>
                    <li><a href="features.html">Features</a></li>
                    <li><a href="downloads.html">Downloads</a></li>
                    <li><a href="story.html">Story</a></li>
                    <li><a href="contact.html">Contact</a></li>
                    <li><a href="faq.html">FAQ</a></li>
                    <li><a href="blog.html">Blog</a></li>
                </ul>
            </nav>
        `;

        // Create footer HTML
        const footerHTML = `
            <p>&copy; 2025 HandyWorks Software. All rights reserved.</p>
        `;

        // Insert header
        const header = document.querySelector('header');
        if (header) {
            header.innerHTML = headerHTML;
            console.log('Header inserted successfully');
        } else {
            console.error('Header element not found');
        }

        // Insert footer
        const footer = document.querySelector('footer');
        if (footer) {
            footer.innerHTML = footerHTML;
            console.log('Footer inserted successfully');
        } else {
            console.error('Footer element not found');
        }

        // Add active class to current page navigation item
        const currentPage = window.location.pathname.split('/').pop() || 'index.html';
        const navLinks = document.querySelectorAll('nav a');
        navLinks.forEach(link => {
            if (link.getAttribute('href') === currentPage) {
                link.classList.add('active');
            }
        });
        
        console.log('Header and footer initialization complete');
    }
    
    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initHeaderFooter);
    } else {
        // DOM is already ready
        initHeaderFooter();
    }
})();
