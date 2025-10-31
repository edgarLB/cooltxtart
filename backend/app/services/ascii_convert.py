
characters = ' _.,-=+:;cba!?0123456789$W#@Ñ'

def make_ascii(img, mask):
    ascii_text = ''
    no_bg_ascii_text = ''

    condition = mask > 0.75

    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            b, g, r = img[row][col]

            # determine character based on the luminance of the pixel
            luminance = (0.299 * r) + (0.587 * g) + (0.114 * b)


            cha_index = int(luminance / 255 * (len(characters) - 1))

            ascii_char = characters[cha_index]

            ascii_text += ascii_char

            if condition[row, col]:
                no_bg_ascii_text += ascii_char
            else:
                no_bg_ascii_text += ' '

        ascii_text += '\n'
        no_bg_ascii_text += '\n'


    # print(ascii_text)
    return ascii_text, no_bg_ascii_text
