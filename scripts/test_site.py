#!/usr/bin/env python3
"""
Final Site Testing Script
Tests links, downloads, file existence, and basic functionality
"""

import re
from pathlib import Path
from urllib.parse import urlparse
import json

def test_file_exists(filepath):
    """Check if a file exists"""
    return Path(filepath).exists()

def extract_links_from_html(html_file):
    """Extract all links from an HTML file"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all href attributes
    href_pattern = r'href=["\']([^"\']+)["\']'
    links = re.findall(href_pattern, content, re.IGNORECASE)
    
    # Find all src attributes (images, scripts, etc.)
    src_pattern = r'src=["\']([^"\']+)["\']'
    srcs = re.findall(src_pattern, content, re.IGNORECASE)
    
    return links + srcs

def test_internal_link(link, base_path):
    """Test if an internal link is valid"""
    # Remove query strings and fragments
    clean_link = link.split('?')[0].split('#')[0]
    
    # Handle relative paths
    if clean_link.startswith('/'):
        clean_link = clean_link[1:]
    elif not clean_link.startswith('http'):
        # Relative link
        if clean_link.endswith('.html'):
            return test_file_exists(clean_link)
        elif clean_link.startswith('downloads/') or clean_link.startswith('public/'):
            return test_file_exists(clean_link)
        elif clean_link.startswith('images/') or clean_link.startswith('newsletters/'):
            return test_file_exists(clean_link)
        elif clean_link.startswith('css/') or clean_link.startswith('js/'):
            return test_file_exists(clean_link)
    
    return None  # External link or special case

def test_all_pages():
    """Test all HTML pages"""
    base_path = Path('.')
    html_files = list(base_path.glob('*.html'))
    html_files = [f for f in html_files if f.name != 'template.html']
    
    results = {
        'pages_tested': 0,
        'broken_links': [],
        'missing_files': [],
        'external_links': [],
        'download_files': []
    }
    
    print("="*80)
    print("TESTING ALL HTML PAGES")
    print("="*80)
    print()
    
    for html_file in sorted(html_files):
        print(f"Testing {html_file.name}...", end=' ')
        results['pages_tested'] += 1
        
        links = extract_links_from_html(html_file)
        page_issues = []
        
        for link in links:
            # Skip special cases
            if link.startswith('mailto:') or link.startswith('tel:') or link.startswith('#'):
                continue
            
            # Check if it's an external link
            if link.startswith('http://') or link.startswith('https://'):
                results['external_links'].append((str(html_file), link))
                continue
            
            # Test internal links
            link_result = test_internal_link(link, base_path)
            if link_result is False:
                page_issues.append(link)
                results['broken_links'].append((str(html_file), link))
            elif link_result is True and (link.startswith('downloads/') or link.startswith('public/')):
                results['download_files'].append(link)
        
        if page_issues:
            print(f"⚠️  {len(page_issues)} issue(s)")
        else:
            print("✅")
    
    return results

def test_download_files():
    """Test that all download files exist"""
    print()
    print("="*80)
    print("TESTING DOWNLOAD FILES")
    print("="*80)
    print()
    
    # Files referenced in downloads.html
    download_files = [
        'public/HW_Upgrade_02_25.exe',
        'public/HW_Upgrade_12_24.exe',
        'public/HW_Install.exe',
        'public/Manual.pdf',
        'public/clicksend.exe',
        'public/bitcoin.pdf',
        'public/HW_Upgrade_2_25.exe',  # For LatestVersion.txt
        'public/LatestVersion.txt'
    ]
    
    missing = []
    for file_path in download_files:
        if test_file_exists(file_path):
            size = Path(file_path).stat().st_size
            print(f"✅ {file_path:40} ({size:,} bytes)")
        else:
            print(f"❌ {file_path:40} MISSING")
            missing.append(file_path)
    
    return missing

def test_critical_files():
    """Test critical site files"""
    print()
    print("="*80)
    print("TESTING CRITICAL FILES")
    print("="*80)
    print()
    
    critical_files = [
        'index.html',
        'about.html',
        'downloads.html',
        'contact.html',
        'faq.html',
        'css/style.css',
        'js/config.js',
        'js/header-footer.js',
        'js/sidebar.js',
        'js/blog-expand.js',
        'sitemap.xml',
        'robots.txt',
        'public/LatestVersion.txt'
    ]
    
    missing = []
    for file_path in critical_files:
        if test_file_exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} MISSING")
            missing.append(file_path)
    
    return missing

def test_blog_posts():
    """Verify blog posts exist"""
    print()
    print("="*80)
    print("TESTING BLOG POSTS")
    print("="*80)
    print()
    
    blog_path = Path('blog')
    blog_files = list(blog_path.rglob('*.html'))
    
    print(f"✅ Found {len(blog_files)} blog post files")
    
    # Check a few sample posts
    sample_posts = [
        'blog/2025/02/new-and-fixed-in-february-2025.html',
        'blog/2024/08/integrated-text-messaging.html',
        'blog/2017/02/welcome-to-the-new-handyworks-website.html'
    ]
    
    for post in sample_posts:
        if test_file_exists(post):
            print(f"✅ {post}")
        else:
            print(f"❌ {post} MISSING")
    
    return len(blog_files)

def generate_report(results, missing_downloads, missing_critical, blog_count):
    """Generate final test report"""
    print()
    print("="*80)
    print("FINAL TEST REPORT")
    print("="*80)
    print()
    
    print(f"Pages Tested:           {results['pages_tested']}")
    print(f"Blog Posts Found:        {blog_count}")
    print(f"Broken Internal Links:   {len(results['broken_links'])}")
    print(f"Missing Download Files:  {len(missing_downloads)}")
    print(f"Missing Critical Files:  {len(missing_critical)}")
    print(f"External Links Found:    {len(results['external_links'])}")
    print()
    
    if results['broken_links']:
        print("BROKEN LINKS:")
        for page, link in results['broken_links'][:10]:  # Show first 10
            print(f"  ❌ {page} → {link}")
        if len(results['broken_links']) > 10:
            print(f"  ... and {len(results['broken_links']) - 10} more")
        print()
    
    if missing_downloads:
        print("MISSING DOWNLOAD FILES:")
        for file in missing_downloads:
            print(f"  ❌ {file}")
        print()
    
    if missing_critical:
        print("MISSING CRITICAL FILES:")
        for file in missing_critical:
            print(f"  ❌ {file}")
        print()
    
    # Overall status
    all_good = (
        len(results['broken_links']) == 0 and
        len(missing_downloads) == 0 and
        len(missing_critical) == 0
    )
    
    if all_good:
        print("="*80)
        print("✅ ALL TESTS PASSED - Site is ready for deployment!")
        print("="*80)
    else:
        print("="*80)
        print("⚠️  SOME ISSUES FOUND - Review and fix before deployment")
        print("="*80)
    
    return all_good

if __name__ == '__main__':
    print("="*80)
    print("HANDYWORKS WEBSITE - FINAL TESTING")
    print("="*80)
    print()
    
    # Run tests
    results = test_all_pages()
    missing_downloads = test_download_files()
    missing_critical = test_critical_files()
    blog_count = test_blog_posts()
    
    # Generate report
    all_good = generate_report(results, missing_downloads, missing_critical, blog_count)
    
    exit(0 if all_good else 1)

