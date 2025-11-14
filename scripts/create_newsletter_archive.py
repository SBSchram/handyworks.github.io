#!/usr/bin/env python3
"""
Create Newsletter Archive Page

Generates an HTML page listing all newsletters with readable names.
"""

from pathlib import Path
from html import escape

def map_newsletter_name(filename):
    """Map newsletter filename to readable name."""
    # W_XX = Winter, S_XX = Summer
    # Try to map to years based on common patterns
    
    if filename.startswith('W_'):
        num = filename.replace('W_', '').replace('.pdf', '')
        try:
            num_int = int(num)
            if num_int >= 0 and num_int <= 20:
                # Likely years 2000-2020
                year = 2000 + num_int
                return f"Winter {year}"
            elif num_int >= 92:
                # Likely years 1992-1999
                year = 1900 + num_int
                return f"Winter {year}"
        except:
            pass
        return f"Winter Newsletter {num}"
    
    elif filename.startswith('S_'):
        num = filename.replace('S_', '').replace('.pdf', '')
        try:
            num_int = int(num)
            if num_int >= 0 and num_int <= 99:
                # Likely years 2000-2099 or 1900-1999
                if num_int < 50:
                    year = 2000 + num_int
                else:
                    year = 1900 + num_int
                return f"Summer {year}"
        except:
            pass
        return f"Summer Newsletter {num}"
    
    return filename.replace('.pdf', '')

def create_newsletter_archive(newsletters_dir, output_file):
    """Create newsletter archive HTML page."""
    
    newsletters_path = Path(newsletters_dir)
    if not newsletters_path.exists():
        print(f"⚠️  Newsletters directory not found: {newsletters_dir}")
        return
    
    # Get all PDF files
    pdf_files = sorted(newsletters_path.glob('*.pdf'), reverse=True)
    
    if not pdf_files:
        print("⚠️  No newsletter PDFs found")
        return
    
    # Group by type (Winter/Summer)
    winter = []
    summer = []
    other = []
    
    for pdf_file in pdf_files:
        name = pdf_file.name
        readable_name = map_newsletter_name(name)
        
        if name.startswith('W_'):
            winter.append({'name': name, 'readable': readable_name})
        elif name.startswith('S_'):
            summer.append({'name': name, 'readable': readable_name})
        else:
            other.append({'name': name, 'readable': readable_name})
    
    # Generate HTML content
    content = '''
        <h1>HandyWorks Newsletters</h1>
        <p>Archive of HandyWorks newsletters and updates.</p>
        
        <section class="newsletter-archive">'''
    
    if winter:
        content += '\n            <h2>Winter Newsletters</h2>\n            <ul class="newsletter-list">'
        for item in winter:
            content += f'\n                <li><a href="newsletters/{item["name"]}" target="_blank">{escape(item["readable"])}</a></li>'
        content += '\n            </ul>'
    
    if summer:
        content += '\n            <h2>Summer Newsletters</h2>\n            <ul class="newsletter-list">'
        for item in summer:
            content += f'\n                <li><a href="newsletters/{item["name"]}" target="_blank">{escape(item["readable"])}</a></li>'
        content += '\n            </ul>'
    
    if other:
        content += '\n            <h2>Other Newsletters</h2>\n            <ul class="newsletter-list">'
        for item in other:
            content += f'\n                <li><a href="newsletters/{item["name"]}" target="_blank">{escape(item["readable"])}</a></li>'
        content += '\n            </ul>'
    
    content += '\n        </section>'
    
    # Get HTML template
    html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Newsletters - HandyWorks</title>
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
    
    # Write file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    print(f"✅ Created newsletter archive: {output_file}")
    print(f"   Found {len(winter)} winter, {len(summer)} summer, {len(other)} other newsletters")

if __name__ == '__main__':
    create_newsletter_archive('newsletters', 'newsletters.html')

