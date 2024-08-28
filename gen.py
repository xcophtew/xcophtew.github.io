import os

# Directory containing the static HTML files
static_dir = "static"

# Generate navigation HTML dynamically based on existing HTML files
def generate_nav_html():
    html_files = [f for f in os.listdir(static_dir) if f.endswith('.html')]
    nav_links = [{"name": os.path.splitext(file)[0].capitalize(), "url": file} for file in html_files]
    nav_html = "<nav><ul>"
    for link in nav_links:
        nav_html += f'<li><a href="{link["url"]}">{link["name"]}</a></li>'
    nav_html += "</ul></nav>"
    return nav_html

# Generate footer HTML
footer_html = '''
<footer>
    <p>&copy; 2024 Network Xcophtew. All rights reserved.</p>
</footer>
'''

# Meta tag and script tag to be added
meta_tag = '<meta name="google-adsense-account" content="ca-pub-5283042537011987">'
script_tag = '''
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5283042537011987"
     crossorigin="anonymous"></script>
'''

# Font preconnect and stylesheet link
font_preload = '''
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200..1000;1,200..1000&family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap" rel="stylesheet">
'''

# Function to inject content into HTML files
def inject_content(html_file):
    with open(os.path.join(static_dir, html_file), "r") as file:
        content = file.read()

    # Generate the latest navigation HTML
    nav_html = generate_nav_html()

    # Insert meta tag, script tag, and font preloading into <head>
    if '<head>' in content:
        head_end_index = content.find('</head>')
        if head_end_index != -1:
            content = content[:head_end_index] + meta_tag + '\n' + script_tag + '\n' + font_preload + '\n' + '<link rel="stylesheet" href="static/style.css">' + '\n' + content[head_end_index:]
    
    # Insert navigation and footer
    content = content.replace("<!-- NAVIGATION_PLACEHOLDER -->", nav_html)
    content = content.replace("<!-- FOOTER_PLACEHOLDER -->", footer_html)

    # Write the updated content back to the file
    with open(os.path.join(static_dir, html_file), "w") as file:
        file.write(content)

# Process each HTML file in the static directory
html_files = [f for f in os.listdir(static_dir) if f.endswith('.html')]

for html_file in html_files:
    inject_content(html_file)
