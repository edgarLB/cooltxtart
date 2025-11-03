import cv2
import numpy as np
from fastapi import FastAPI, UploadFile, File
import uuid


from app.services.ascii_convert import make_ascii
from app.services.subject_mask import make_mask
from app.services.to_image import make_images

app = FastAPI()

@app.post('/convert',
          summary='convert uploaded image to ASCII art')
async def convert(file: UploadFile = File(...)):
    job_id = str(uuid.uuid4())

    content = await file.read()
    np_arr = np.array(bytearray(content), dtype="uint8")
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)


    # resize
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
    text, no_bg_text = make_ascii(img, mask)

    # image
    make_images(img = img,
                ascii_text_full= text,
                ascii_text_no_bg = no_bg_text,
                output_name = job_id
                )

    return {'status': 'complete'}


