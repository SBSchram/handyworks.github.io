#!/usr/bin/env python3
"""
Update Blog Listing with Excerpts

Adds excerpts to blog post listings in index.html
"""

import json
import re
from pathlib import Path
from html import escape

def update_index_with_excerpts(index_file='index.html', excerpts_file='blog_excerpts.json'):
    """Update index.html to include excerpts in blog listings."""
    
    # Load excerpts
    with open(excerpts_file, 'r', encoding='utf-8') as f:
        excerpts = json.load(f)
    
    # Read index.html
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all blog post entries
    pattern = r'(<article class="blog-post-summary">.*?<p class="post-categories">.*?</p>)(\s*</article>)'
    
    def add_excerpt(match):
        article_start = match.group(1)
        article_end = match.group(2)
        
        # Extract URL from the article
        url_match = re.search(r'href="([^"]+)"', article_start)
        if not url_match:
            return match.group(0)
        
        url = url_match.group(1)
        # Convert URL to excerpt key (remove blog/ prefix)
        excerpt_key = url.replace('blog/', '')
        excerpt = excerpts.get(excerpt_key, '')
        
        if excerpt:
            excerpt_html = f'\n                <div class="post-excerpt">{escape(excerpt)}</div>'
            return article_start + excerpt_html + article_end
        else:
            return match.group(0)
    
    # Replace all blog entries
    updated_content = re.sub(pattern, add_excerpt, content, flags=re.DOTALL)
    
    # Write back
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"✅ Updated {index_file} with excerpts")

if __name__ == '__main__':
    update_index_with_excerpts()

