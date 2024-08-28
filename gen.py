import os
import requests

# Directory containing the static HTML files
static_dir = "static"

# URL of the API
api_url = "https://fetcharch.vercel.app/logs"

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
    <p>&copy; 2024 Network Xcophtew.  All rights reserved.</p>
</footer>
'''

# Meta tag and script tag to be added
meta_tag = '<meta name="google-adsense-account" content="ca-pub-5283042537011987">'
script_tag = '''
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5283042537011987"
     crossorigin="anonymous"></script>
'''

# Function to inject content into HTML files
def inject_content(html_file, logs_content=None):
    with open(os.path.join(static_dir, html_file), "r") as file:
        content = file.read()

    # Insert meta tag and script tag into <head>
    if '<head>' in content:
        head_end_index = content.find('</head>')
        if head_end_index != -1:
            # Insert meta tag and script tag before </head>
            content = content[:head_end_index] + meta_tag + '\n' + script_tag + '\n' + content[head_end_index:]
    
    # Generate the latest navigation HTML
    nav_html = generate_nav_html()

    # Insert navigation and footer
    content = content.replace("<!-- NAVIGATION_PLACEHOLDER -->", nav_html)
    content = content.replace("<!-- FOOTER_PLACEHOLDER -->", footer_html)

    # Inject logs content if provided
    if logs_content and html_file == "logs.html":
        content = content.replace('<div id="logs-content"></div>', logs_content)

    # Write the updated content back to the file
    with open(os.path.join(static_dir, html_file), "w") as file:
        file.write(content)

# Fetch logs data from the API
def fetch_logs():
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        articles = data["documents"][0]["articles_log"]
        return articles
    else:
        return "Failed to load logs."

# Process each HTML file in the static directory and inject content
html_files = [f for f in os.listdir(static_dir) if f.endswith('.html')]

# Add "Website Logs" page to the navigation
for html_file in html_files:
    inject_content(html_file)

# Inject logs content into the logs page
logs_content = fetch_logs()
inject_content("logs.html", logs_content)
