#!/usr/bin/env node

// DRY Build Script for HandyWorks Website
const fs = require('fs');
const path = require('path');

// Configuration - Single source of truth
const config = {
    version: '20250129v1',
    pages: [
        {
            file: 'index.html',
            title: 'HandyWorks - Chiropractic Office Management Software',
            content: `
                <h1>Welcome to HandyWorks</h1>
                <p>Professional practice management software designed specifically for chiropractic offices.</p>
                
                <div class="cta">
                    <a href="downloads.html" class="button">Download Latest Version</a>
                </div>
                
                <section class="features">
                    <h3>Key Features</h3>
                    <ul>
                        <li>Patient Management</li>
                        <li>Appointment Scheduling</li>
                        <li>Billing & Insurance</li>
                        <li>Electronic Health Records</li>
                        <li>Reporting & Analytics</li>
                    </ul>
                </section>
            `
        },
        {
            file: 'about.html',
            title: 'About',
            content: `
                <h1>About HandyWorks</h1>
                <p>HandyWorks is a comprehensive practice management software designed specifically for chiropractic offices.</p>
                <p>With over 30 years of development and refinement, HandyWorks provides everything you need to manage your practice efficiently.</p>
            `
        },
        {
            file: 'contact.html',
            title: 'Contact',
            content: `
                <h1>Contact Us</h1>
                <p>Get in touch with us for support, questions, or more information about HandyWorks.</p>
                <div class="contact-details">
                    <h3>Contact Information</h3>
                    <p>Email: <a href="mailto:steve@handyworks.com">steve@handyworks.com</a></p>
                    <p>Phone: <a href="tel:888-555-0123">(888) 555-0123</a></p>
                </div>
            `
        },
        {
            file: 'downloads.html',
            title: 'Downloads',
            content: `
                <h1>Downloads</h1>
                <p>Download the latest version of HandyWorks and related documentation.</p>
                
                <section class="downloads">
                    <h2>The latest upgrade contains all prior improvements</h2>
                    <p><strong style="color: #ff0000;">(For safety, always backup your data and current version of HW before proceeding.)</strong></p>
                    
                    <h3>Recent Updates</h3>
                    <ul class="update-list">
                        <li><a href="downloads/HW_Upgrade_02_25.exe" class="button" download>02/06/2025</a> - The First 2025 update</li>
                        <li><a href="downloads/HW_Upgrade_12_24.exe" class="button" download>12/31/2024</a> - The Last 2024 update (fixes screen 3 clock issue)</li>
                    </ul>
                    
                    <h3>Downloads to help you run HandyWorks</h3>
                    <p>For new installs, look <a href="faq.html#Install">HERE</a> for instructions.</p>
                    
                    <div class="download-item">
                        <h3>Helper Files for Re-Installing HW</h3>
                        <p>Contains static elements like shortcuts, icons and manual</p>
                        <a href="downloads/HW_Install.exe" class="button" download>Download Helper Files</a>
                    </div>
                    
                    <div class="download-item">
                        <h3>Latest Upgrade Package</h3>
                        <p>Most recent version with all improvements</p>
                        <a href="downloads/HW_Upgrade_02_25.exe" class="button" download>Download Latest Upgrade</a>
                    </div>
                    
                    <div class="download-item">
                        <h3>Previous Version</h3>
                        <p>December 2024 update</p>
                        <a href="downloads/HW_Upgrade_12_24.exe" class="button" download>Download 12/24 Update</a>
                    </div>
                </section>
            `
        }
        // Add more pages as needed
    ]
};

// Template for HTML files
const htmlTemplate = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <link rel="stylesheet" href="css/style.css?v={{VERSION}}">
    <script src="js/config.js?v={{VERSION}}"></script>
    <script src="js/header-footer.js?v={{VERSION}}" defer></script>
</head>
<body>
    <header>
        <!-- Header content will be inserted by header-footer.js -->
    </header>
    
    <main>
        {{CONTENT}}
    </main>
    
    <footer>
        <!-- Footer content will be inserted by header-footer.js -->
    </footer>
</body>
</html>`;

// Function to build HTML files
function buildPages() {
    console.log(`Building pages with version: ${config.version}`);
    
    config.pages.forEach(page => {
        const html = htmlTemplate
            .replace('{{TITLE}}', page.title)
            .replace('{{VERSION}}', config.version)
            .replace('{{CONTENT}}', page.content);
        
        fs.writeFileSync(page.file, html, 'utf8');
        console.log(`Built: ${page.file}`);
    });
}

// Function to update config.js with current version
function updateConfig() {
    const configContent = `// Configuration file for DRY principle
// Single source of truth for cache busting and other settings
window.HandyWorksConfig = {
    version: '${config.version}',
    cacheBust: true,
    
    // Header configuration
    header: {
        title: 'HandyWorks',
        subtitle: 'Chiropractic Office Management Software',
        navigation: [
            { href: 'index.html', text: 'Home' },
            { href: 'about.html', text: 'About' },
            { href: 'features.html', text: 'Features' },
            { href: 'downloads.html', text: 'Downloads' },
            { href: 'story.html', text: 'Story' },
            { href: 'contact.html', text: 'Contact' },
            { href: 'faq.html', text: 'FAQ' },
            { href: 'blog.html', text: 'Blog' }
        ]
    },
    
    // Footer configuration
    footer: {
        copyright: '&copy; 2025 HandyWorks Software. All rights reserved.'
    },
    
    // Get cache busted URL for a file
    getCacheBustedUrl: function(filePath) {
        return this.cacheBust ? \`\${filePath}?v=\${this.version}\` : filePath;
    }
};`;
    
    fs.writeFileSync('js/config.js', configContent, 'utf8');
    console.log('Updated config.js');
}

// Run the build
console.log('Starting DRY build process...');
updateConfig();
buildPages();
console.log('Build complete!');
