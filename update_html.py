import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Tailwind config update
content = re.sub(
    r'colors: \{[\s\S]*?brand: \{[\s\S]*?\}[\s\S]*?\}',
    "colors: {\n                        brand: {\n                            black: '#000000',\n                            white: '#FFFFFF',\n                            honeysuckle: '#D65076'\n                        }\n                    }",
    content
)

# 2. Global color class replacements
content = content.replace('bg-brand-ivory', 'bg-white')
content = content.replace('bg-brand-sand', 'bg-white')
content = content.replace('bg-brand-black', 'bg-black')
content = content.replace('text-brand-black', 'text-black')
content = content.replace('text-brand-gray', 'text-brand-honeysuckle')
content = content.replace('border-brand-border', 'border-black')
content = content.replace('text-gray-600', 'text-black')
content = content.replace('text-gray-400', 'text-white')
content = content.replace('text-gray-300', 'text-white')
content = content.replace('border-gray-800', 'border-white')
content = content.replace('bg-gray-200', 'bg-brand-honeysuckle')
content = content.replace('hover:bg-gray-800', 'hover:bg-brand-honeysuckle')

# Make borders and lines more minimal or honeysuckle
# content = content.replace('border-black', 'border-black/20') # soften borders slightly, or keep them sharp. Let's keep strict black:
# content = content.replace('border-black/20', 'border-black')
# content = content.replace('bg-brand-border', 'bg-black')
content = content.replace('bg-brand-border', 'bg-brand-honeysuckle')

# 3. Text reductions
# Hero
content = content.replace('Discover what suits you, visualize your style, and build looks around you.', 'Discover, visualize, and build.')
# Idea
content = re.sub(r'<div class="space-y-6[\s\S]*?</div>', '<div class="space-y-6 text-lg font-light leading-relaxed"><p>Not just a trend, but a reflection of you.</p></div>', content, count=1)
# Vision/Mission
content = content.replace('To make personal styling intelligent, visual, and accessible — helping everyone understand what suits them and express their individuality with confidence.', 'Make styling intelligent, visual, and accessible.')
content = content.replace('To combine personal insights, styling intelligence, visual exploration, and wardrobe organization into one personalized experience that helps people discover, create, and plan styles that truly work for them.', 'Combine insights and organization into one personalized experience.')

# Features text
content = re.sub(r'<ul class="space-y-4[\s\S]*?</ul>', '', content)
content = content.replace('A personalized, daily look built from what you own, optimized for the current weather.', 'A daily look built from what you own.')
content = content.replace('Understand your face shape and discover styling directions that complement your features.', 'Discover styles that complement your features.')
content = content.replace('A deep dive into your visual identity—including your optimal color palette, contrast levels, and body architecture.', 'Your optimal colors and body architecture.')
content = content.replace('Turn the clothes you already own into a digital wardrobe and discover combinations from your own collection.', 'Your closet, reimagined digitally.')
content = content.replace('Never forget a great outfit combination. Save looks you love and assign them to specific days or events in your planner.', 'Save looks and assign them to future events.')

# How it works text
content = content.replace('Build your personal profile and provide the information needed for personalized styling.', '')
content = content.replace('Explore appearance insights and Style DNA.', '')
content = content.replace('Check your current look, explore outfits, hairstyles, and styling inspirations.', '')
content = content.replace('Build your digital wardrobe and discover combinations using what you already own.', '')
content = content.replace('Save useful looks and associate them with future dates or occasions.', '')

# Why P'STYLST text
content = content.replace('Styling guidance is built around the individual.', '')
content = content.replace('Explore styling possibilities through visual experiences.', '')
content = content.replace('Use your own wardrobe, save looks, and plan what to wear.', '')
content = content.replace('More personal. More visual. More practical.', 'Personal. Visual. Practical.')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
