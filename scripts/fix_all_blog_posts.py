#!/usr/bin/env python3
"""
Fix All Blog Posts - Batch Processing

Applies content cleaning to all blog post HTML files.
"""

import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

from clean_wordpress_content import clean_blog_post_html_file

def fix_all_blog_posts(blog_dir='blog'):
    """
    Process all blog post HTML files and clean their content.
    
    Args:
        blog_dir: Directory containing blog posts
    """
    blog_path = Path(blog_dir)
    
    if not blog_path.exists():
        print(f"❌ Blog directory not found: {blog_dir}")
        return
    
    # Find all HTML files
    html_files = list(blog_path.rglob('*.html'))
    
    if not html_files:
        print(f"⚠️  No HTML files found in {blog_dir}")
        return
    
    print("="*60)
    print("CLEANING BLOG POSTS")
    print("="*60)
    print(f"\n📝 Found {len(html_files)} blog post files\n")
    
    success_count = 0
    error_count = 0
    
    for html_file in sorted(html_files):
        rel_path = html_file.relative_to(Path('.'))
        print(f"🔄 Processing: {rel_path}...", end=' ')
        
        if clean_blog_post_html_file(html_file):
            print("✅")
            success_count += 1
        else:
            print("❌")
            error_count += 1
    
    print("\n" + "="*60)
    print(f"✅ Successfully cleaned: {success_count} files")
    if error_count > 0:
        print(f"❌ Errors: {error_count} files")
    print("="*60)

if __name__ == '__main__':
    fix_all_blog_posts()

