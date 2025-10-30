// Header and Footer inclusion for DRY principle
// Uses configuration from config.js for single source of truth
(function() {
    'use strict';
    
    // Function to initialize header and footer
    function initHeaderFooter() {
        console.log('Initializing header and footer...');
        
        // Wait for config to be available
        if (typeof window.HandyWorksConfig === 'undefined') {
            console.error('HandyWorksConfig not found. Make sure config.js is loaded first.');
            return;
        }
        
        const config = window.HandyWorksConfig;
        
        // Create navigation HTML from config
        const navItems = config.header.navigation.map(item => 
            `<li><a href="${item.href}">${item.text}</a></li>`
        ).join('\n                    ');
        
        // Create header HTML from config
        const headerHTML = `
            <div class="header-container">
                <div class="site-title">
                    <h1>${config.header.title}</h1>
                    <p>${config.header.subtitle}</p>
                </div>
            </div>
            <nav>
                <ul>
                    ${navItems}
                </ul>
            </nav>
        `;

        // Create footer HTML from config
        const footerHTML = `
            <p>${config.footer.copyright}</p>
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
