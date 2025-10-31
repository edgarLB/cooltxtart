import cv2

from app.services.ascii_convert import make_ascii
from services.subject_mask import make_mask
from services.to_image import make_images

def main():

    file_path = 'temp/test.jpg'
    img = cv2.imread(file_path, cv2.IMREAD_COLOR)

    max_size = 75
    longer_side = max(img.shape[0], img.shape[1])
    scale = 0

    if longer_side > max_size:
        scale = max_size / longer_side
    elif longer_side < max_size:
        scale = longer_side / max_size

    img = cv2.resize(img, (0, 0), fx=scale, fy=scale)

    # segment
    mask = make_mask(img)

    # ascii
    text, noBG_text = make_ascii(img, mask)

    # image
    make_images(img = img,
               ascii_text_full= text,
               ascii_text_no_bg = noBG_text,
               output_name = "test"
               )




if __name__ == '__main__':
    main()