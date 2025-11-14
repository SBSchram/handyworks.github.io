# HandyWorks Website

Professional chiropractic office management software website.

## Overview

This is a static HTML website for HandyWorks, migrated from WordPress to a modern, maintainable static site structure. The site is hosted on GitHub Pages.

## Site Structure

```
handyworks-website/
├── blog/              # Blog posts (HTML)
├── newsletters/       # Newsletter PDFs
├── downloads/         # Software downloads
├── images/            # Images (organized)
├── css/              # Stylesheets
├── js/               # JavaScript
└── scripts/          # Utility scripts
```

## Development

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/SBSchram/handyworks-website.git
   cd handyworks-website
   ```

2. Serve locally (using Python):
   ```bash
   python3 -m http.server 8000
   ```
   Then open http://localhost:8000

### Building

The site uses a simple build system (`build.js`) for generating pages with consistent header/footer.

## Deployment

The site is automatically deployed to GitHub Pages when changes are pushed to the `main` branch.

### GitHub Pages URL
- Test URL: `https://sbschram.github.io/handyworks-website/`
- Production URL: `https://www.handyworks.com` (after DNS migration)

### DNS Migration

**Current Status:** Testing on GitHub Pages (old WordPress site still live)

**Migration Steps:**
1. ✅ Site deployed to GitHub Pages
2. ⏳ Test on GitHub Pages URL
3. ⏳ Update DNS CNAME record to point to GitHub Pages
4. ⏳ Configure custom domain in GitHub Pages settings
5. ⏳ Verify SSL certificate
6. ⏳ Monitor for issues

## Content

- **Blog Posts:** 61 posts (2006-2025)
- **Pages:** 14 pages
- **Newsletters:** 43 PDF files
- **Downloads:** Software updates and installation files

## Scripts

Utility scripts in `scripts/`:
- `parse_wordpress_export.py` - Extract content from WordPress XML
- `organize_assets.py` - Organize files into proper structure
- `generate_html.py` - Generate HTML from extracted content
- `create_newsletter_archive.py` - Create newsletter archive page
- `cleanup_directory.py` - Remove unnecessary files

## License

Copyright © 2025 HandyWorks Software. All rights reserved.

