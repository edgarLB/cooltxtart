import cv2

characters = ' _.,-=+:;cba!?0123456789$W#@Ñ'

filePath = '../temp/test.jpg'
img = cv2.imread(filePath, cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)

asciiText = ''


for row in range(img.shape[0]):
    for col in range(img.shape[1]):
        b, g, r = img[row][col]

        # determine character based on the luminance of the pixel
        luminance = (0.299 * r) + (0.587 * g) + (0.114 * b)
        charIndex = int(luminance / 255 * (len(characters) - 1))

        asciiText += characters[charIndex]
    asciiText += '\n'


# print(asciiText)
