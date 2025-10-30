import math

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
from ascii_convert import asciiText, img

outputName = 'output'

fontSize = 20
fontPath = '../assets/fonts/consolas.ttf'
font = ImageFont.truetype(fontPath, fontSize)

lines = asciiText.split('\n')

spacing_factor = 1.2
maxWidth = max(len(line) for line in lines)
imageWidth = math.floor(maxWidth * fontSize * spacing_factor)
imageHeight = math.floor(len(lines) * fontSize * spacing_factor)

result = Image.new('RGBA', (imageWidth, imageHeight), color=(0, 0, 0, 0))
draw = ImageDraw.Draw(result)

glow = Image.new('RGBA', result.size, (0, 0, 0, 0))
glowDraw = ImageDraw.Draw(glow)

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        # BGR to RGB
        color = (img[i][j][2], img[i][j][1], img[i][j][0])

        x = j * fontSize * spacing_factor
        y = i * fontSize * spacing_factor

        draw.text((x, y), char, font=font, fill=color)
        glowDraw.text((x, y), char, font=font, fill=color, stroke_width=1, stroke_fill=color)


#--------- Glow Effect Effect Compositing -----#
background = Image.new('RGBA', result.size, color='black')

# tight blur
glow.putalpha(110)
glow = glow.filter(ImageFilter.GaussianBlur(radius=2))
background.paste(glow, (0,0), glow)

# sharp text
background.paste(result, (0,0), result)

# glow
glow.putalpha(250)
glow = glow.filter(ImageFilter.GaussianBlur(radius=6))
background = ImageChops.add(background, glow)


background.save(f'../temp/{outputName}.png')