#!/usr/bin/env python3
"""
Extract Excerpts from Blog Posts

Generates excerpts (first paragraph or 200 words) from blog post HTML files
for display in blog listings.
"""

import re
from pathlib import Path
from html import unescape

def extract_excerpt_from_html(html_file, max_words=200):
    """Extract excerpt from blog post HTML file."""
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find post content
    content_match = re.search(r'<div class="post-content">(.*?)</div>', content, re.DOTALL)
    if not content_match:
        return None
    
    post_content = content_match.group(1)
    
    # Remove HTML tags but keep text
    text = re.sub(r'<[^>]+>', ' ', post_content)
    text = re.sub(r'\s+', ' ', text)
    text = unescape(text).strip()
    
    # Get first paragraph or first max_words
    words = text.split()
    
    if len(words) <= max_words:
        excerpt = text
    else:
        # Find a good breaking point (sentence end)
        excerpt_words = words[:max_words]
        excerpt_text = ' '.join(excerpt_words)
        
        # Try to end at a sentence
        last_period = excerpt_text.rfind('.')
        last_exclamation = excerpt_text.rfind('!')
        last_question = excerpt_text.rfind('?')
        
        break_point = max(last_period, last_exclamation, last_question)
        
        if break_point > max_words * 0.7:  # If we found a sentence end reasonably close
            excerpt = excerpt_text[:break_point + 1]
        else:
            excerpt = excerpt_text + '...'
    
    return excerpt.strip()

def generate_excerpts_json(blog_dir='blog', output_file='blog_excerpts.json'):
    """Generate JSON file with all blog post excerpts."""
    
    import json
    
    blog_path = Path(blog_dir)
    excerpts = {}
    
    # Find all blog post HTML files
    for html_file in blog_path.rglob('*.html'):
        excerpt = extract_excerpt_from_html(html_file)
        if excerpt:
            # Use relative path as key
            rel_path = str(html_file.relative_to(blog_path))
            excerpts[rel_path] = excerpt
    
    # Save to JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(excerpts, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Extracted {len(excerpts)} excerpts to {output_file}")
    return excerpts

if __name__ == '__main__':
    generate_excerpts_json()

