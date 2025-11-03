import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import os

BASE_DIR = os.path.dirname(__file__)

fontSize = 20
fontPath = os.path.join(BASE_DIR, '../assets/fonts/consolas.ttf')
font = ImageFont.truetype(fontPath, fontSize)
spacing_factor = 1.2

def make_images(img, ascii_text_full, ascii_text_no_bg, output_name):
    lines_full = ascii_text_full.split('\n')
    lines_no_bg = ascii_text_no_bg.split('\n')


    max_width = max(len(line) for line in lines_full)
    image_width = math.floor(max_width * fontSize * spacing_factor)
    image_height = math.floor(len(lines_full) * fontSize * spacing_factor)

    result_full = Image.new('RGBA', (image_width, image_height), color=(0, 0, 0, 0))
    result_no_bg = Image.new('RGBA', (image_width, image_height), color=(0, 0, 0, 0))
    glow_full = Image.new('RGBA', (image_width, image_height), (0, 0, 0, 0))
    glow_no_bg = Image.new('RGBA', (image_width, image_height), (0, 0, 0, 0))

    draw_full = ImageDraw.Draw(result_full)
    draw_no_bg = ImageDraw.Draw(result_no_bg)
    draw_glow_full = ImageDraw.Draw(glow_full)
    draw_glow_no_bg = ImageDraw.Draw(glow_no_bg)

    for i, line in enumerate(lines_full):
        for j, char in enumerate(line):
            # BGR to RGB
            color = (img[i][j][2], img[i][j][1], img[i][j][0])

            x = j * fontSize * spacing_factor
            y = i * fontSize * spacing_factor

            # Full photo
            draw_full.text((x, y), char, font=font, fill=color)
            draw_glow_full.text((x, y), char, font=font, fill=color, stroke_width=1, stroke_fill=color)

            # No background photo
            if  lines_no_bg[i][j] != ' ':
                draw_no_bg.text((x, y), char, font=font, fill=color)
                draw_glow_no_bg.text((x, y), char, font=font, fill=color, stroke_width=1, stroke_fill=color)

    def apply_glow(base_img, glow_img):
        background = Image.new('RGBA', base_img.size, color='black')

        # soft blur
        glow_img.putalpha(50)
        glow_img = glow_img.filter(ImageFilter.GaussianBlur(radius=1))
        background.paste(glow_img, (0,0), glow_img)

        # tight blur
        glow_img.putalpha(110)
        glow_img = glow_img.filter(ImageFilter.GaussianBlur(radius=2))
        background.paste(glow_img, (0,0), glow_img)

        # sharp text
        background.paste(base_img, (0,0), base_img)


        # glow 1
        glow_img.putalpha(250)
        glow_img = glow_img.filter(ImageFilter.GaussianBlur(radius=6))
        background = ImageChops.add(background, glow_img)

        # glow 2
        glow_img.putalpha(100)
        glow_img = glow_img.filter(ImageFilter.GaussianBlur(radius=15))
        background = ImageChops.add(background, glow_img)

        return background

    final_full = apply_glow(result_full, glow_full)
    final_no_bg = apply_glow(result_no_bg, glow_no_bg)

    final_full_path = os.path.join(BASE_DIR, f'../temp/{output_name}_full.png')
    final_no_bg_path = os.path.join(BASE_DIR, f'../temp/{output_name}_no_bg.png')

    final_full.save(final_full_path)
    final_no_bg.save(final_no_bg_path)

