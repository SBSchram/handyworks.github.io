// Configuration file for DRY principle
// Single source of truth for cache busting and other settings
window.HandyWorksConfig = {
    version: '20250129v1',
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
        return this.cacheBust ? `${filePath}?v=${this.version}` : filePath;
    }
};