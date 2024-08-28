import os

# Define common HTML components
nav_links = [
    {"name": "Home", "url": "index.html"},
    {"name": "About", "url": "about.html"},
    {"name": "Contact", "url": "contact.html"}
]

# Generate navigation HTML
nav_html = "<nav><ul>"
for link in nav_links:
    nav_html += f'<li><a href="{link["url"]}">{link["name"]}</a></li>'
nav_html += "</ul></nav>"

# Generate footer HTML
footer_html = """
<footer>
    <p>&copy; 2024 Network Xcophtew. All rights reserved.</p>
</footer>
"""

# Directory containing the static HTML files
static_dir = "static"

# Function to inject content into HTML files
def inject_content(html_file):
    with open(os.path.join(static_dir, html_file), "r") as file:
        content = file.read()

    # Insert navigation and footer
    content = content.replace("<!-- NAVIGATION_PLACEHOLDER -->", nav_html)
    content = content.replace("<!-- FOOTER_PLACEHOLDER -->", footer_html)

    # Write the updated content back to the file
    with open(os.path.join(static_dir, html_file), "w") as file:
        file.write(content)

# List of HTML files to process
html_files = ["index.html", "about.html", "contact.html"]

# Process each HTML file
for html_file in html_files:
    inject_content(html_file)
