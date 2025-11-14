#!/usr/bin/env python3
"""
Generate HTML Files from Extracted WordPress Content

Converts extracted Markdown files to HTML pages with proper structure,
navigation, and styling.
"""

import re
import json
from pathlib import Path
from datetime import datetime
from html import escape

def markdown_to_html(markdown_text):
    """Convert basic Markdown to HTML."""
    if not markdown_text:
        return ''
    
    html = markdown_text
    
    # Headers
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    
    # Bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    
    # Italic
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    
    # Links
    html = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', html)
    
    # Paragraphs (lines not starting with HTML tags)
    lines = html.split('\n')
    result = []
    in_para = False
    
    for line in lines:
        line = line.strip()
        if not line:
            if in_para:
                result.append('</p>')
                in_para = False
            continue
        
        # If line doesn't start with HTML tag, wrap in paragraph
        if not line.startswith('<'):
            if not in_para:
                result.append('<p>')
                in_para = True
            result.append(line)
        else:
            if in_para:
                result.append('</p>')
                in_para = False
            result.append(line)
    
    if in_para:
        result.append('</p>')
    
    html = '\n'.join(result)
    
    # Lists
    html = re.sub(r'^\- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(<li>.*?</li>)', r'<ul>\1</ul>', html, flags=re.DOTALL)
    
    return html

def get_html_template(title, content, current_page=''):
    """Generate HTML page template."""
    
    # Determine active nav item
    nav_items = [
        {'href': 'index.html', 'text': 'HOME'},
        {'href': 'blog.html', 'text': 'BLOG'},
        {'href': 'downloads.html', 'text': 'UPGRADES & DOWNLOADS'},
        {'href': 'about.html', 'text': 'ABOUT HANDYWORKS'},
        {'href': 'partners.html', 'text': 'PARTNERS'},
        {'href': 'contact.html', 'text': 'CONTACT US'},
        {'href': 'legacy.html', 'text': 'LEGACY'}
    ]
    
    nav_html = '\n                    '.join([
        f'<li><a href="{item["href"]}"{" class=\"active\"" if current_page == item["href"] else ""}>{item["text"]}</a></li>'
        for item in nav_items
    ])
    
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape(title)} - HandyWorks</title>
    <link rel="stylesheet" href="css/style.css?v=20250129v1">
    <script src="js/config.js?v=20250129v1"></script>
    <script src="js/header-footer.js?v=20250129v1" defer></script>
</head>
<body>
    <header>
        <!-- Header content will be inserted by header-footer.js -->
    </header>
    
    <main>
        {content}
    </main>
    
    <footer>
        <!-- Footer content will be inserted by header-footer.js -->
    </footer>
</body>
</html>'''

def generate_blog_post_html(post_file, output_dir):
    """Generate HTML for a single blog post."""
    
    with open(post_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse front matter
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else 'Untitled'
    
    date_match = re.search(r'\*\*Date:\*\* (.+)', content)
    date_str = date_match.group(1) if date_match else ''
    
    categories_match = re.search(r'\*\*Categories:\*\* (.+)', content)
    categories = categories_match.group(1) if categories_match else ''
    
    excerpt_match = re.search(r'\*\*Excerpt:\*\* (.+)', content)
    excerpt = excerpt_match.group(1) if excerpt_match else ''
    
    # Extract body content (after ---)
    body_match = re.search(r'---\n\n(.*)', content, re.DOTALL)
    body = body_match.group(1) if body_match else content
    
    # Convert to HTML
    body_html = markdown_to_html(body)
    
    # Create HTML content
    html_content = f'''
        <article class="blog-post">
            <header class="post-header">
                <h1>{escape(title)}</h1>
                <div class="post-meta">
                    <time datetime="{date_str}">{date_str}</time>
                    {f'<span class="categories">{categories}</span>' if categories else ''}
                </div>
            </header>
            <div class="post-content">
                {body_html}
            </div>
        </article>
    '''
    
    # Generate filename
    post_date = datetime.strptime(date_str, '%Y-%m-%d') if date_str else datetime.now()
    year = post_date.year
    month = f"{post_date.month:02d}"
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[-\s]+', '-', slug)[:50]
    filename = f"{slug}.html"
    
    # Create output path
    output_path = output_dir / str(year) / month
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Write HTML file
    html = get_html_template(title, html_content, 'blog.html')
    with open(output_path / filename, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return {
        'title': title,
        'date': date_str,
        'url': f'blog/{year}/{month}/{filename}',
        'categories': categories
    }

def generate_blog_index(posts_data, output_file, excerpts_file='blog_excerpts.json'):
    """Generate blog archive/index page with excerpts."""
    
    import json
    
    # Load excerpts
    excerpts = {}
    if Path(excerpts_file).exists():
        with open(excerpts_file, 'r', encoding='utf-8') as f:
            excerpts = json.load(f)
    
    # Sort posts by date (newest first)
    posts_data.sort(key=lambda x: x['date'], reverse=True)
    
    # Group by year
    posts_by_year = {}
    for post in posts_data:
        year = post['date'][:4] if post['date'] else 'Unknown'
        if year not in posts_by_year:
            posts_by_year[year] = []
        posts_by_year[year].append(post)
    
    # Generate HTML
    content = '<h1>HandyWorks Blog</h1>\n        <p>Latest updates, features, and news about HandyWorks software.</p>\n        \n        <section class="blog-posts">'
    
    for year in sorted(posts_by_year.keys(), reverse=True):
        content += f'\n            <h2>{year}</h2>'
        for post in filtered_years[year]:
            # Get excerpt
            excerpt_key = post['url'].replace('blog/', '')
            excerpt = excerpts.get(excerpt_key, '')
            
            content += f'''
            <article class="blog-post-summary">
                <h3><a href="{post['url']}">{escape(post['title'])}</a></h3>
                <p class="post-date">{post['date']}</p>
                {f'<p class="post-categories">{post["categories"]}</p>' if post['categories'] else ''}
                {f'<div class="post-excerpt">{escape(excerpt)}</div>' if excerpt else ''}
            </article>'''
    
    content += '\n        </section>'
    
    html = get_html_template('Blog - HandyWorks', content, 'index.html')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Generated blog index: {output_file}")

def main():
    """Main generation function."""
    
    base_path = Path('.')
    extracted_path = base_path / 'extracted_content'
    blog_path = base_path / 'blog'
    
    print("="*60)
    print("GENERATING HTML FILES")
    print("="*60)
    print()
    
    # Generate blog posts
    print("📝 Generating blog posts...")
    posts_data = []
    
    posts_dir = extracted_path / 'posts'
    if posts_dir.exists():
        for post_file in posts_dir.rglob('*.md'):
            try:
                post_info = generate_blog_post_html(post_file, blog_path)
                posts_data.append(post_info)
            except Exception as e:
                print(f"⚠️  Error processing {post_file}: {e}")
        
        print(f"✅ Generated {len(posts_data)} blog post HTML files")
    
    # Generate blog index
    print("\n📑 Generating blog index...")
    blog_index = base_path / 'index.html'  # Homepage is now the blog
    if posts_data:
        generate_blog_index(posts_data, blog_index)
    
    print("\n" + "="*60)
    print("✅ HTML generation complete!")
    print("="*60)

if __name__ == '__main__':
    main()

