import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<span class="text-brand-border">.*?</span>', '<span class="text-brand-honeysuckle">&#8594;</span>', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
