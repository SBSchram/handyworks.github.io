#!/usr/bin/env node

// Cache busting build script for DRY principle
const fs = require('fs');
const path = require('path');

// Generate cache busting version based on timestamp
const version = `v${Date.now()}`;

// List of HTML files to update
const htmlFiles = [
    'index.html',
    'about.html',
    'contact.html',
    'downloads.html',
    'features.html',
    'story.html',
    'faq.html',
    'blog.html'
];

// Function to update cache busting parameters in HTML files
function updateCacheBusting(filePath) {
    try {
        let content = fs.readFileSync(filePath, 'utf8');
        
        // Update CSS cache busting
        content = content.replace(
            /href="css\/style\.css(\?v=[^"]*)?"/g,
            `href="css/style.css?v=${version}"`
        );
        
        // Update JS cache busting
        content = content.replace(
            /src="js\/header-footer\.js(\?v=[^"]*)?"/g,
            `src="js/header-footer.js?v=${version}"`
        );
        
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Updated cache busting for: ${filePath}`);
    } catch (error) {
        console.error(`Error updating ${filePath}:`, error.message);
    }
}

// Update all HTML files
console.log(`Updating cache busting to version: ${version}`);
htmlFiles.forEach(file => {
    const filePath = path.join(__dirname, file);
    if (fs.existsSync(filePath)) {
        updateCacheBusting(filePath);
    } else {
        console.warn(`File not found: ${filePath}`);
    }
});

console.log('Cache busting update complete!');
