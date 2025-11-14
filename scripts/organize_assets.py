#!/usr/bin/env python3
"""
Organize HandyWorks Website Assets

Moves and organizes all assets from scattered locations into a clean,
standard website directory structure.
"""

import shutil
import os
from pathlib import Path
from collections import defaultdict

def create_directory_structure(base_path):
    """Create the standard website directory structure."""
    
    directories = [
        'blog',
        'newsletters',
        'downloads',
        'images',
        'images/logos',
        'images/screenshots',
        'images/legacy',
        'css',
        'js',
        'scripts',
        'assets'
    ]
    
    for directory in directories:
        (base_path / directory).mkdir(parents=True, exist_ok=True)
    
    print("✅ Created directory structure")

def organize_newsletters(source_dir, dest_dir):
    """Organize newsletter PDFs with readable names."""
    
    source = Path(source_dir)
    dest = Path(dest_dir)
    
    if not source.exists():
        print(f"⚠️  Newsletter source not found: {source_dir}")
        return 0
    
    # Newsletter mapping (W_XX = Winter, S_XX = Summer)
    # We'll need to map these to actual years based on file dates or manual mapping
    copied = 0
    
    for pdf_file in source.glob('*.pdf'):
        # Copy with original name for now (we can rename later if needed)
        dest_file = dest / pdf_file.name
        shutil.copy2(pdf_file, dest_file)
        copied += 1
    
    print(f"✅ Copied {copied} newsletters to {dest_dir}/")
    return copied

def organize_downloads(source_dir, dest_dir):
    """Organize software download files."""
    
    source = Path(source_dir)
    dest = Path(dest_dir)
    
    if not source.exists():
        print(f"⚠️  Downloads source not found: {source_dir}")
        return 0
    
    copied = 0
    
    for file in source.iterdir():
        if file.is_file():
            dest_file = dest / file.name
            shutil.copy2(file, dest_file)
            copied += 1
    
    print(f"✅ Copied {copied} download files to {dest_dir}/")
    return copied

def organize_images(source_dir, dest_dir):
    """Organize images from WordPress uploads."""
    
    source = Path(source_dir)
    dest = Path(dest_dir)
    
    if not source.exists():
        print(f"⚠️  Images source not found: {source_dir}")
        return 0
    
    # Count files
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg'}
    copied = 0
    skipped = 0
    
    # Walk through uploads directory
    for root, dirs, files in os.walk(source):
        for file in files:
            file_path = Path(root) / file
            ext = file_path.suffix.lower()
            
            if ext in image_extensions:
                # Skip WordPress-generated thumbnails (files with dimensions in name)
                if re.search(r'-\d+x\d+\.', file):
                    skipped += 1
                    continue
                
                # Determine category
                if 'logo' in file.lower() or 'hwlogo' in file.lower():
                    dest_path = dest / 'logos' / file
                elif 'screenshot' in file.lower() or 'capture' in file.lower():
                    dest_path = dest / 'screenshots' / file
                elif any(x in str(root) for x in ['2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008']):
                    dest_path = dest / 'legacy' / file
                else:
                    dest_path = dest / file
                
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Avoid duplicates
                if not dest_path.exists():
                    shutil.copy2(file_path, dest_path)
                    copied += 1
    
    print(f"✅ Copied {copied} images to {dest_dir}/ (skipped {skipped} thumbnails)")
    return copied

def organize_other_files(source_dir, dest_dir):
    """Organize other useful files from public directory."""
    
    source = Path(source_dir)
    dest = Path(dest_dir)
    
    if not source.exists():
        print(f"⚠️  Source not found: {source_dir}")
        return 0
    
    # Files to copy
    useful_files = {
        'HandyWorks.pdf': 'downloads/',
        'meridian-clock.jpg': 'images/',
        'CIP_jpg.jpg': 'images/',
    }
    
    copied = 0
    
    for filename, subdir in useful_files.items():
        source_file = source / filename
        if source_file.exists():
            dest_path = dest / subdir / filename
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_file, dest_path)
            copied += 1
    
    print(f"✅ Copied {copied} other files")
    return copied

def main():
    """Main organization function."""
    
    base_path = Path('.')
    
    print("="*60)
    print("ORGANIZING HANDYWORKS WEBSITE ASSETS")
    print("="*60)
    print()
    
    # Create directory structure
    create_directory_structure(base_path)
    print()
    
    # Organize newsletters
    print("📰 Organizing newsletters...")
    organize_newsletters('tmb/public/Newlstters', 'newsletters')
    print()
    
    # Organize downloads
    print("💾 Organizing downloads...")
    organize_downloads('tmb/public/Downloads', 'downloads')
    print()
    
    # Organize images
    print("🖼️  Organizing images...")
    organize_images('tmb/wp-content/uploads', 'images')
    print()
    
    # Organize other files
    print("📄 Organizing other files...")
    organize_other_files('tmb/public', base_path)
    print()
    
    print("="*60)
    print("✅ Asset organization complete!")
    print("="*60)

if __name__ == '__main__':
    import re
    main()

