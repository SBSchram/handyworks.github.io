#!/usr/bin/env python3
"""
Cleanup Directory - Remove Unnecessary Files

Carefully identifies and removes files that are no longer needed after
migration and organization.
"""

import shutil
from pathlib import Path
import json

def get_file_size(path):
    """Get file size in a readable format."""
    try:
        size = path.stat().st_size
        if size < 1024:
            return f"{size} B"
        elif size < 1024 * 1024:
            return f"{size / 1024:.1f} KB"
        else:
            return f"{size / (1024 * 1024):.1f} MB"
    except:
        return "Unknown"

def analyze_directory(base_path):
    """Analyze directory and identify files to remove."""
    
    base = Path(base_path)
    
    # Files/directories to KEEP (essential)
    keep_patterns = [
        'index.html',
        'about.html',
        'blog.html',
        'contact.html',
        'downloads.html',
        'faq.html',
        'features.html',
        'legacy.html',
        'partners.html',
        'story.html',
        'newsletters.html',
        'css/',
        'js/',
        'blog/',
        'newsletters/',
        'downloads/',
        'images/',
        'scripts/',
        '.git/',
        '.gitignore',
        'README.md',
        'handyworks.WordPress.2025-10-29.xml',  # Keep as backup/reference
    ]
    
    # Files/directories to REMOVE (no longer needed)
    remove_items = []
    
    # Check tmb/ directory (WordPress backup - already extracted)
    tmb_path = base / 'tmb'
    if tmb_path.exists():
        size = sum(f.stat().st_size for f in tmb_path.rglob('*') if f.is_file())
        remove_items.append({
            'path': str(tmb_path),
            'type': 'directory',
            'reason': 'WordPress backup - content already extracted and organized',
            'size': get_file_size(tmb_path) if tmb_path.is_file() else f"{size / (1024*1024):.1f} MB"
        })
    
    # Check extracted_content/ (Markdown files - HTML already generated)
    extracted_path = base / 'extracted_content'
    if extracted_path.exists():
        # Keep content_inventory.json, but can remove individual post/page files
        posts_path = extracted_path / 'posts'
        if posts_path.exists():
            remove_items.append({
                'path': str(posts_path),
                'type': 'directory',
                'reason': 'Markdown blog posts - HTML versions generated in blog/',
                'size': 'N/A'
            })
        pages_path = extracted_path / 'pages'
        if pages_path.exists():
            remove_items.append({
                'path': str(pages_path),
                'type': 'directory',
                'reason': 'Markdown pages - can be regenerated from XML if needed',
                'size': 'N/A'
            })
    
    # Check for test/debug files
    test_files = ['test.html', 'debug.html']
    for test_file in test_files:
        test_path = base / test_file
        if test_path.exists():
            remove_items.append({
                'path': str(test_path),
                'type': 'file',
                'reason': 'Test/debug file - not needed for production',
                'size': get_file_size(test_path)
            })
    
    # Check for old build artifacts
    build_files = ['build-cache-bust.js']  # build.js might be needed
    for build_file in build_files:
        build_path = base / build_file
        if build_path.exists():
            remove_items.append({
                'path': str(build_path),
                'type': 'file',
                'reason': 'Old build script - functionality replaced',
                'size': get_file_size(build_path)
            })
    
    # Check for .DS_Store files (macOS)
    ds_store_files = list(base.rglob('.DS_Store'))
    for ds_file in ds_store_files:
        remove_items.append({
            'path': str(ds_file),
            'type': 'file',
            'reason': 'macOS system file - not needed',
            'size': get_file_size(ds_file)
        })
    
    return remove_items

def print_cleanup_plan(remove_items):
    """Print cleanup plan for review."""
    
    print("\n" + "="*60)
    print("CLEANUP PLAN")
    print("="*60)
    print()
    
    if not remove_items:
        print("✅ No files identified for removal - directory is clean!")
        return
    
    total_size = 0
    
    print("Files/Directories to Remove:")
    print("-" * 60)
    
    for item in remove_items:
        print(f"\n{item['type'].upper()}: {item['path']}")
        print(f"  Reason: {item['reason']}")
        print(f"  Size: {item['size']}")
    
    print("\n" + "="*60)
    print(f"Total items to remove: {len(remove_items)}")
    print("="*60)

def perform_cleanup(remove_items, dry_run=True):
    """Perform the cleanup (with dry-run option)."""
    
    if dry_run:
        print("\n🔍 DRY RUN MODE - No files will be deleted")
        print("   Review the plan above, then run with --execute to remove files")
        return
    
    print("\n🗑️  REMOVING FILES...")
    print("-" * 60)
    
    removed = 0
    errors = 0
    
    for item in remove_items:
        path = Path(item['path'])
        
        if not path.exists():
            print(f"⚠️  Skipping (not found): {path}")
            continue
        
        try:
            if path.is_file():
                path.unlink()
                print(f"✅ Removed file: {path}")
            elif path.is_dir():
                shutil.rmtree(path)
                print(f"✅ Removed directory: {path}")
            removed += 1
        except Exception as e:
            print(f"❌ Error removing {path}: {e}")
            errors += 1
    
    print("\n" + "="*60)
    print(f"✅ Removed: {removed} items")
    if errors > 0:
        print(f"⚠️  Errors: {errors} items")
    print("="*60)

def main():
    """Main cleanup function."""
    
    import sys
    
    dry_run = '--execute' not in sys.argv
    
    print("="*60)
    print("DIRECTORY CLEANUP ANALYSIS")
    print("="*60)
    
    remove_items = analyze_directory('.')
    print_cleanup_plan(remove_items)
    
    if remove_items:
        perform_cleanup(remove_items, dry_run=dry_run)
        
        if dry_run:
            print("\n💡 To actually remove these files, run:")
            print("   python3 scripts/cleanup_directory.py --execute")
    else:
        print("\n✅ Directory is already clean!")

if __name__ == '__main__':
    main()

