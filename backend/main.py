import os.path

import cv2
import numpy as np
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uuid

from starlette.requests import Request
from starlette.staticfiles import StaticFiles

from app.services.ascii_convert import make_ascii
from app.services.subject_mask import make_mask
from app.services.to_image import make_images

app = FastAPI()

ENV = os.getenv('ENV', 'dev')

if ENV == 'production':
    allowed_origins = ['https://cooltxt.art',
                       'https://www.cooltxt.art']
else:
    allowed_origins = ['http://localhost:5173',
                       'http://127.0.0.1:5173']

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST'],
    allow_headers=['*'],
)

TEMP_DIR = os.path.join('app', 'temp')
os.makedirs(TEMP_DIR, exist_ok=True)

app.mount('/temp', StaticFiles(directory=TEMP_DIR), name='temp')

@app.post('/convert',
          summary='convert uploaded image to ASCII art')
async def convert(res: Request, file: UploadFile = File(...)):
    job_id = str(uuid.uuid4())

    content = await file.read()
    np_arr = np.array(bytearray(content), dtype='uint8')
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # resize if necessary
    if (img.shape[0] > 75) or (img.shape[1] > 75):
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
    full_path, no_bg_path = make_images(img = img,
                ascii_text_full= text,
                ascii_text_no_bg = no_bg_text,
                output_name = job_id
                )

    base_url = str(res.base_url)

    return {
        'full': base_url + 'temp/' + os.path.basename(full_path),
        'no_bg': base_url + 'temp/' + os.path.basename(no_bg_path)
        }


