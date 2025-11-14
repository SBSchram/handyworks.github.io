#!/usr/bin/env python3
"""
Regenerate Blog Index from Existing HTML Files

Reads all blog post HTML files and generates the index.html with all posts.
"""

import re
import json
from pathlib import Path
from html import escape

def extract_post_info_from_html(html_file):
    """Extract post metadata from an existing HTML file."""
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    title = title_match.group(1).strip() if title_match else 'Untitled'
    title = re.sub(r'<[^>]+>', '', title)  # Remove any HTML tags
    
    # Extract date
    date_match = re.search(r'<time datetime="([^"]+)"', content)
    if not date_match:
        date_match = re.search(r'<time[^>]*>([^<]+)</time>', content)
    date_str = date_match.group(1).strip() if date_match else ''
    
    # Get URL from file path
    rel_path = html_file.relative_to(Path('blog'))
    url = f'blog/{rel_path}'
    
    return {
        'title': title,
        'date': date_str,
        'url': url.replace('\\', '/'),  # Normalize path separators
        'categories': ''
    }

def generate_blog_index_from_html_files(blog_dir='blog', output_file='index.html', excerpts_file='blog_excerpts.json'):
    """Generate blog index from existing HTML files."""
    
    # Load excerpts
    excerpts = {}
    if Path(excerpts_file).exists():
        with open(excerpts_file, 'r', encoding='utf-8') as f:
            excerpts = json.load(f)
    
    # Find all blog post HTML files
    blog_path = Path(blog_dir)
    posts_data = []
    
    for html_file in blog_path.rglob('*.html'):
        try:
            post_info = extract_post_info_from_html(html_file)
            if post_info['date']:  # Only include posts with dates
                posts_data.append(post_info)
        except Exception as e:
            print(f"⚠️  Error processing {html_file}: {e}")
    
    # Sort posts by date (newest first)
    posts_data.sort(key=lambda x: x['date'], reverse=True)
    
    # Group by year
    posts_by_year = {}
    for post in posts_data:
        year = post['date'][:4] if post['date'] else 'Unknown'
        if year not in posts_by_year:
            posts_by_year[year] = []
        posts_by_year[year].append(post)
    
    # Generate HTML content
    content_parts = ['<h1>HandyWorks Blog</h1>', 
                    '<p>Latest updates, features, and news about HandyWorks software.</p>',
                    '',
                    '<section class="blog-posts">']
    
    for year in sorted(posts_by_year.keys(), reverse=True):
        content_parts.append(f'            <h2>{year}</h2>')
        for post in posts_by_year[year]:
            # Get excerpt
            excerpt_key = post['url'].replace('blog/', '')
            excerpt = excerpts.get(excerpt_key, '')
            
            excerpt_html = f'                <div class="post-excerpt">{escape(excerpt)}</div>' if excerpt else ''
            
            content_parts.append(f'''            <article class="blog-post-summary">
                <h3><a href="{post['url']}">{escape(post['title'])}</a></h3>
                <p class="post-date">{post['date']}</p>{excerpt_html}
            </article>''')
    
    content_parts.append('        </section>')
    new_content = '\n        '.join(content_parts)
    
    # Read the existing index.html
    with open(output_file, 'r', encoding='utf-8') as f:
        existing_html = f.read()
    
    # Replace everything between <main> and </main>
    pattern = r'(<main>).*?(</main>)'
    replacement = r'\1\n        ' + new_content + '\n    \2'
    new_html = re.sub(pattern, replacement, existing_html, flags=re.DOTALL)
    
    # Write back
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    print(f"✅ Generated blog index with {len(posts_data)} posts from {len(posts_by_year)} years")
    print(f"   Years: {', '.join(sorted(posts_by_year.keys(), reverse=True))}")

if __name__ == '__main__':
    generate_blog_index_from_html_files()
