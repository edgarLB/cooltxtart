import math

from PIL import Image, ImageDraw, ImageFont
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

result = Image.new('RGB', (imageWidth, imageHeight), color='black')
draw = ImageDraw.Draw(result)

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        # BGR to RGB
        color = (img[i][j][2], img[i][j][1], img[i][j][0])

        draw.text((j * fontSize * spacing_factor, i * fontSize * spacing_factor), char, font=font, fill=color)


result.save(f'../temp/{outputName}.png')