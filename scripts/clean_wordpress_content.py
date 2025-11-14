#!/usr/bin/env python3
"""
WordPress Content Cleaner

Cleans WordPress HTML content by:
- Removing WordPress block comments
- Fixing malformed list structures
- Ensuring proper paragraph spacing
- Preserving valid HTML formatting
"""

import re
from html import escape, unescape

def clean_wordpress_content(html_content):
    """
    Clean WordPress HTML content to proper, readable HTML.
    
    Args:
        html_content: Raw HTML string with WordPress blocks
        
    Returns:
        Cleaned HTML string
    """
    if not html_content:
        return ''
    
    # Step 1: Remove all WordPress block comments
    # Remove opening and closing block comments
    html_content = re.sub(r'<!--\s*wp:[^>]*-->', '', html_content)
    html_content = re.sub(r'<!--\s*/wp:[^>]*-->', '', html_content)
    
    # Step 2: Fix malformed list structures
    # WordPress often creates nested <ul> tags inside list items
    # Pattern: <ul><li>...</li></ul> inside another <ul>
    # We need to extract the <li> content and consolidate
    
    # First, handle nested <ul> tags inside list items
    # Find patterns like: <ul><li><ul><li>content</li></ul></li></ul>
    def fix_nested_lists(match):
        inner_content = match.group(1)
        # Extract all <li> tags from nested structure
        li_matches = re.findall(r'<li>(.*?)</li>', inner_content, re.DOTALL)
        if li_matches:
            # Create a single <ul> with all <li> items
            li_items = '\n'.join([f'<li>{item.strip()}</li>' for item in li_matches])
            return f'<ul>\n{li_items}\n</ul>'
        return match.group(0)
    
    # Fix nested list structures (multiple passes may be needed)
    for _ in range(3):  # Multiple passes to handle deeply nested structures
        html_content = re.sub(
            r'<ul[^>]*>(.*?)</ul>',
            fix_nested_lists,
            html_content,
            flags=re.DOTALL
        )
    
    # Step 3: Clean up empty paragraphs
    html_content = re.sub(r'<p>\s*</p>', '', html_content)
    html_content = re.sub(r'<p>\s*<br\s*/?>\s*</p>', '', html_content)
    
    # Step 4: Ensure proper paragraph spacing
    # Add line breaks between paragraphs for readability
    html_content = re.sub(r'</p>\s*<p>', '</p>\n<p>', html_content)
    
    # Step 5: Clean up excessive whitespace
    html_content = re.sub(r'\n{3,}', '\n\n', html_content)  # Max 2 consecutive newlines
    html_content = re.sub(r'[ \t]+', ' ', html_content)  # Multiple spaces to single
    
    # Step 6: Ensure lists have proper spacing
    html_content = re.sub(r'</ul>\s*<ul>', '</ul>\n<ul>', html_content)
    html_content = re.sub(r'</p>\s*<ul>', '</p>\n<ul>', html_content)
    html_content = re.sub(r'</ul>\s*<p>', '</ul>\n<p>', html_content)
    
    # Step 7: Clean up list items - remove nested <ul> tags that might remain
    # Find <li> tags that contain <ul> tags and extract the content properly
    def fix_li_with_ul(match):
        li_content = match.group(1)
        # If the <li> contains a <ul>, extract the <ul> and its content
        ul_match = re.search(r'<ul[^>]*>(.*?)</ul>', li_content, re.DOTALL)
        if ul_match:
            # The <ul> should be outside the <li>, so extract it
            ul_content = ul_match.group(0)
            # Remove the <ul> from inside <li> and return both
            li_text = re.sub(r'<ul[^>]*>.*?</ul>', '', li_content, flags=re.DOTALL).strip()
            if li_text:
                return f'<li>{li_text}</li>\n{ul_content}'
            else:
                return ul_content
        return match.group(0)
    
    html_content = re.sub(r'<li>(.*?)</li>', fix_li_with_ul, html_content, flags=re.DOTALL)
    
    # Step 8: Final cleanup - remove any remaining nested <ul> structures
    # Consolidate adjacent <ul> tags
    html_content = re.sub(r'</ul>\s*<ul[^>]*>', '', html_content)
    
    # Step 9: Remove duplicate closing tags (like </ul></ul>)
    html_content = re.sub(r'</ul>\s*</ul>', '</ul>', html_content)
    html_content = re.sub(r'</ol>\s*</ol>', '</ol>', html_content)
    
    # Step 10: Remove WordPress figure blocks but keep images
    # Convert <figure class="wp-block-image"> to just the <img> tag
    def extract_image_from_figure(match):
        img_match = re.search(r'<img[^>]*>', match.group(0), re.IGNORECASE)
        if img_match:
            return img_match.group(0)
        return ''
    
    html_content = re.sub(
        r'<figure[^>]*>.*?</figure>',
        extract_image_from_figure,
        html_content,
        flags=re.DOTALL | re.IGNORECASE
    )
    
    # Step 11: Clean up any remaining WordPress-specific classes
    html_content = re.sub(r'\s*class="wp-[^"]*"', '', html_content)
    html_content = re.sub(r'\s*data-type="[^"]*"', '', html_content)
    html_content = re.sub(r'\s*data-id="[^"]*"', '', html_content)
    
    # Step 12: Ensure proper spacing around images
    html_content = re.sub(r'</p>\s*<img', '</p>\n<img', html_content)
    html_content = re.sub(r'<img[^>]*>\s*<p>', '<img[^>]*>\n<p>', html_content)
    
    return html_content.strip()

def clean_blog_post_html_file(html_file_path):
    """
    Clean a single blog post HTML file.
    
    Args:
        html_file_path: Path to the HTML file
        
    Returns:
        True if successful, False otherwise
    """
    from pathlib import Path
    
    try:
        file_path = Path(html_file_path)
        if not file_path.exists():
            print(f"⚠️  File not found: {html_file_path}")
            return False
        
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the post-content div
        content_match = re.search(
            r'(<div class="post-content">)(.*?)(</div>)',
            content,
            re.DOTALL
        )
        
        if not content_match:
            print(f"⚠️  No post-content found in: {html_file_path}")
            return False
        
        # Clean the content
        original_content = content_match.group(2)
        cleaned_content = clean_wordpress_content(original_content)
        
        # Replace the content
        new_content = (
            content[:content_match.start(2)] +
            '\n' + cleaned_content + '\n            ' +
            content[content_match.end(2):]
        )
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
        
    except Exception as e:
        print(f"❌ Error processing {html_file_path}: {e}")
        return False

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        # Clean a single file
        result = clean_blog_post_html_file(sys.argv[1])
        if result:
            print(f"✅ Cleaned: {sys.argv[1]}")
        else:
            print(f"❌ Failed to clean: {sys.argv[1]}")
    else:
        print("Usage: python3 clean_wordpress_content.py <html_file>")
        print("Or import and use clean_wordpress_content() function")

