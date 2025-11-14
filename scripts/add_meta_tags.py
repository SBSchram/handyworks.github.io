#!/usr/bin/env python3
"""
Add SEO meta tags to all HTML pages
"""

import re
from pathlib import Path
from html import escape

# Meta descriptions for each page
META_DESCRIPTIONS = {
    'index.html': 'HandyWorks blog - Latest updates, features, and news about HandyWorks chiropractic office management software.',
    'about.html': 'Learn about HandyWorks - Chiropractic office management software developed since 1981. Trusted by chiropractors nationwide.',
    'downloads.html': 'Download HandyWorks software upgrades, installers, manuals, and helper files. Get the latest version of HandyWorks.',
    'contact.html': 'Contact HandyWorks Software. Get support, ask questions, or request information about our chiropractic office management software.',
    'faq.html': 'Frequently asked questions about HandyWorks software installation, features, and usage.',
    'features.html': 'Discover the features of HandyWorks - comprehensive chiropractic office management software for patient records, billing, and more.',
    'legacy.html': 'HandyWorks legacy information and historical updates about our chiropractic office management software.',
    'newsletters.html': 'HandyWorks newsletter archive - Browse past newsletters with updates, tips, and news about HandyWorks software.',
}

# Default meta description
DEFAULT_DESCRIPTION = 'HandyWorks - Chiropractic office management software. Patient records, billing, appointments, and more since 1981.'

# Keywords for all pages
KEYWORDS = 'HandyWorks, chiropractic software, office management, patient records, billing software, chiropractic practice management'

def add_meta_tags(html_file_path):
    """Add meta tags to an HTML file"""
    with open(html_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Get filename for meta description lookup
    filename = Path(html_file_path).name
    description = META_DESCRIPTIONS.get(filename, DEFAULT_DESCRIPTION)
    
    # Check if meta tags already exist
    if '<meta name="description"' in content:
        print(f"  ⚠️  {html_file_path} already has meta description, skipping")
        return False
    
    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    title = title_match.group(1) if title_match else 'HandyWorks'
    
    # Create meta tags
    meta_tags = f'''    <meta name="description" content="{escape(description)}">
    <meta name="keywords" content="{escape(KEYWORDS)}">
    <meta name="author" content="HandyWorks Software">
    <meta property="og:title" content="{escape(title)}">
    <meta property="og:description" content="{escape(description)}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://sbschram.github.io/handyworks-website/{filename}">
    <meta name="twitter:card" content="summary">
    <meta name="twitter:title" content="{escape(title)}">
    <meta name="twitter:description" content="{escape(description)}">'''
    
    # Insert meta tags after viewport meta tag
    viewport_pattern = r'(<meta name="viewport"[^>]*>)'
    if re.search(viewport_pattern, content):
        content = re.sub(
            viewport_pattern,
            r'\1\n' + meta_tags,
            content,
            count=1
        )
    else:
        # If no viewport, insert after charset
        charset_pattern = r'(<meta charset="[^"]*">)'
        if re.search(charset_pattern, content):
            content = re.sub(
                charset_pattern,
                r'\1\n' + meta_tags,
                content,
                count=1
            )
    
    # Write back
    with open(html_file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def process_all_html_files():
    """Process all HTML files in the directory"""
    base_path = Path('.')
    
    # Main pages
    main_pages = [
        'index.html', 'about.html', 'downloads.html', 'contact.html',
        'faq.html', 'features.html', 'legacy.html', 'newsletters.html'
    ]
    
    processed = 0
    for page in main_pages:
        page_path = base_path / page
        if page_path.exists():
            print(f"Processing {page}...", end=' ')
            if add_meta_tags(page_path):
                print("✅")
                processed += 1
            else:
                print()
    
    # Blog posts - use default description
    blog_path = base_path / 'blog'
    blog_count = 0
    if blog_path.exists():
        for html_file in blog_path.rglob('*.html'):
            print(f"Processing {html_file}...", end=' ')
            if add_meta_tags(html_file):
                print("✅")
                blog_count += 1
            else:
                print()
    
    print(f"\n✅ Processed {processed} main pages and {blog_count} blog posts")

if __name__ == '__main__':
    print("="*60)
    print("ADDING SEO META TAGS")
    print("="*60)
    process_all_html_files()
    print("="*60)

