import os
from html.parser import HTMLParser

# Name of your HTML file
html_file = "about.html"

# Check if file exists
if not os.path.exists(html_file):
    print(f"❌ '{html_file}' not found in the current folder: {os.getcwd()}")
    exit()

# Read HTML content
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# HTML Parser to check for tags
class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)

parser = MyHTMLParser()
parser.feed(content)

required_tags = ["html", "head", "body", "title", "style"]
missing_tags = [tag for tag in required_tags if tag not in parser.tags]

if missing_tags:
    print(f"❌ Missing HTML tags: {', '.join(missing_tags)}")
else:
    print("✅ All main HTML tags are present.")

# Check for <a href=""> links
links = [attr[1] for tag, attrs in parser.get_starttag_texts() if tag=="a" for attr in attrs if attr[0]=="href"]
if links:
    print("✅ Links found in <a> tags:")
    for link in links:
        print(f"   - {link}")
else:
    print("⚠️ No links found in <a> tags.")

# Check for internal CSS
if "<style" in content and "</style>" in content:
    print("✅ Internal CSS is present.")
else:
    print("⚠️ No internal CSS found.")

# Open file in default browser
import webbrowser
print(f"Opening '{html_file}' in your default browser...")
webbrowser.open_new_tab(f"file://{os.path.abspath(html_file)}")

