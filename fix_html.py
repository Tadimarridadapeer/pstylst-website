import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the broken arrow character
content = content.replace('+\'', '→')
content = content.replace('', '')

# Remove empty p tags
content = re.sub(r'<p[^>]*></p>\n*', '', content)
content = re.sub(r'<p[^>]*>\s*</p>\n*', '', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
