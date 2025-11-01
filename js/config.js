// Configuration file for DRY principle
// Single source of truth for cache busting and other settings
window.HandyWorksConfig = {
    version: '20250129v2',
    cacheBust: true,
    
    // Header configuration
    header: {
        title: 'HandyWorks',
        subtitle: 'Chiropractic Office Management software',
        navigation: [
            { href: 'blog.html', text: 'BLOG' },
            { href: 'downloads.html', text: 'UPGRADES & DOWNLOADS' },
            { href: 'about.html', text: 'ABOUT HANDYWORKS' },
            { href: 'partners.html', text: 'PARTNERS' },
            { href: 'contact.html', text: 'CONTACT US' },
            { href: 'legacy.html', text: 'LEGACY' }
        ]
    },
    
    // Footer configuration
    footer: {
        copyright: '&copy; 2025 HandyWorks Software. All rights reserved.'
    },
    
    // Get cache busted URL for a file
    getCacheBustedUrl: function(filePath) {
        return this.cacheBust ? `${filePath}?v=${this.version}` : filePath;
    }
};