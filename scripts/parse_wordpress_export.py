#!/usr/bin/env python3
"""
Parse WordPress XML Export and Extract Content

Extracts:
- All blog posts (with full content, dates, categories)
- All pages (with full content)
- Media references
- Saves to organized structure
"""

import xml.etree.ElementTree as ET
import json
import os
import re
from datetime import datetime
from collections import defaultdict
from pathlib import Path

def parse_wordpress_export(xml_file):
    """Parse WordPress XML export and extract content."""
    
    print(f"Parsing {xml_file}...")
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # WordPress namespace
    namespaces = {
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'excerpt': 'http://wordpress.org/export/1.2/excerpt/',
        'wp': 'http://wordpress.org/export/1.2/',
        'dc': 'http://purl.org/dc/elements/1.1/'
    }
    
    # Storage
    posts = []
    pages = []
    media = []
    categories = defaultdict(list)
    
    # Find channel element (contains all items)
    channel = root.find('channel')
    if channel is None:
        print("Error: No channel element found")
        return None
    
    # Find all items
    items = channel.findall('item')
    print(f"Found {len(items)} items total")
    
    for item in items:
        # Get post type
        post_type_elem = item.find('wp:post_type', namespaces)
        if post_type_elem is None:
            continue
            
        post_type = post_type_elem.text
        
        # Get basic info
        title_elem = item.find('title')
        title = title_elem.text if title_elem is not None else 'No Title'
        
        post_name_elem = item.find('wp:post_name', namespaces)
        post_name = post_name_elem.text if post_name_elem is not None else ''
        
        post_date_elem = item.find('wp:post_date', namespaces)
        post_date = post_date_elem.text if post_date_elem is not None else ''
        
        status_elem = item.find('wp:status', namespaces)
        status = status_elem.text if status_elem is not None else ''
        
        # Get content
        content_elem = item.find('content:encoded', namespaces)
        content = content_elem.text if content_elem is not None else ''
        
        # Get excerpt
        excerpt_elem = item.find('excerpt:encoded', namespaces)
        excerpt = excerpt_elem.text if excerpt_elem is not None else ''
        
        # Get categories
        item_categories = []
        for cat in item.findall('category'):
            domain = cat.get('domain', '')
            if domain == 'category':
                item_categories.append(cat.text)
        
        # Store based on type
        item_data = {
            'title': title,
            'post_name': post_name,
            'post_date': post_date,
            'status': status,
            'content': content,  # Full content
            'excerpt': excerpt,
            'categories': item_categories
        }
        
        if post_type == 'post':
            posts.append(item_data)
            for cat in item_categories:
                categories[cat].append(title)
        elif post_type == 'page':
            pages.append(item_data)
        elif post_type == 'attachment':
            # Get attachment URL
            attachment_url_elem = item.find('wp:attachment_url', namespaces)
            attachment_url = attachment_url_elem.text if attachment_url_elem is not None else ''
            
            media.append({
                'title': title,
                'post_name': post_name,
                'attachment_url': attachment_url,
                'post_date': post_date
            })
    
    return {
        'posts': posts,
        'pages': pages,
        'media': media,
        'categories': dict(categories)
    }

def sanitize_filename(text):
    """Create a safe filename from text."""
    # Remove special characters, replace spaces with hyphens
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.lower()[:100]  # Limit length

def print_summary(data):
    """Print summary of extracted content."""
    
    print("\n" + "="*60)
    print("WORDPRESS EXPORT CONTENT SUMMARY")
    print("="*60)
    
    print(f"\n📝 BLOG POSTS: {len(data['posts'])}")
    print("-" * 60)
    for post in sorted(data['posts'], key=lambda x: x['post_date'], reverse=True)[:10]:
        date_str = post['post_date'][:10] if post['post_date'] else 'No date'
        status = f" [{post['status']}]" if post['status'] != 'publish' else ''
        print(f"  • {date_str} - {post['title']}{status}")
    if len(data['posts']) > 10:
        print(f"  ... and {len(data['posts']) - 10} more")
    
    print(f"\n📄 PAGES: {len(data['pages'])}")
    print("-" * 60)
    for page in sorted(data['pages'], key=lambda x: x['title'] or ''):
        status = f" [{page['status']}]" if page['status'] != 'publish' else ''
        print(f"  • {page['title'] or 'No Title'}{status}")
    
    print(f"\n🖼️  MEDIA FILES: {len(data['media'])}")
    print("-" * 60)
    print(f"  (Media references found)")
    
    print(f"\n📂 CATEGORIES: {len(data['categories'])}")
    print("-" * 60)
    for cat, posts in sorted(data['categories'].items()):
        print(f"  • {cat}: {len(posts)} posts")
    
    print("\n" + "="*60)

def save_content(data, output_dir='extracted_content'):
    """Save extracted content to organized directories."""
    
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # Save JSON inventory
    inventory_file = output_path / 'content_inventory.json'
    # Create serializable version (remove content for JSON)
    inventory = {
        'posts': [{k: v for k, v in p.items() if k != 'content'} for p in data['posts']],
        'pages': [{k: v for k, v in p.items() if k != 'content'} for p in data['pages']],
        'media': data['media'],
        'categories': data['categories']
    }
    with open(inventory_file, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, indent=2, ensure_ascii=False)
    print(f"✅ Inventory saved to: {inventory_file}")
    
    # Save posts as individual files
    posts_dir = output_path / 'posts'
    posts_dir.mkdir(exist_ok=True)
    
    for post in data['posts']:
        if post['status'] != 'publish':
            continue
            
        # Parse date
        try:
            post_date = datetime.strptime(post['post_date'][:19], '%Y-%m-%d %H:%M:%S')
            year = post_date.year
            month = f"{post_date.month:02d}"
        except:
            year = 'unknown'
            month = '00'
        
        # Create year/month directory
        post_path = posts_dir / str(year) / month
        post_path.mkdir(parents=True, exist_ok=True)
        
        # Create filename
        filename = sanitize_filename(post['title']) or 'untitled'
        filename = f"{filename}.md"
        filepath = post_path / filename
        
        # Write markdown file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {post['title']}\n\n")
            f.write(f"**Date:** {post['post_date'][:10]}\n\n")
            if post['categories']:
                f.write(f"**Categories:** {', '.join(post['categories'])}\n\n")
            if post['excerpt']:
                f.write(f"**Excerpt:** {post['excerpt']}\n\n")
            f.write("---\n\n")
            f.write(post['content'])
    
    print(f"✅ Saved {len([p for p in data['posts'] if p['status'] == 'publish'])} blog posts to {posts_dir}/")
    
    # Save pages as individual files
    pages_dir = output_path / 'pages'
    pages_dir.mkdir(exist_ok=True)
    
    for page in data['pages']:
        if page['status'] != 'publish':
            continue
        
        filename = sanitize_filename(page['title']) or 'untitled'
        filename = f"{filename}.md"
        filepath = pages_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {page['title'] or 'No Title'}\n\n")
            f.write("---\n\n")
            f.write(page['content'] or '')
    
    print(f"✅ Saved {len([p for p in data['pages'] if p['status'] == 'publish'])} pages to {pages_dir}/")
    
    return output_path

if __name__ == '__main__':
    xml_file = 'handyworks.WordPress.2025-10-29.xml'
    
    try:
        data = parse_wordpress_export(xml_file)
        if data:
            print_summary(data)
            output_path = save_content(data)
            print(f"\n✅ Content extraction complete!")
            print(f"   All content saved to: {output_path}/")
        
    except FileNotFoundError:
        print(f"❌ Error: {xml_file} not found")
        print("   Make sure you're in the handyworks-website directory")
    except Exception as e:
        import traceback
        print(f"❌ Error parsing XML: {e}")
        traceback.print_exc()
