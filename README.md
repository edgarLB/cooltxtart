# cooltxtart
An image processing pipeline that transforms uploaded images into stylized ASCII art.

## Backend Workflow

 - Segments the subject using Mediapipe
 - Converts pixel data to ASCII characters based on luminance
 - Render ASCII back to images using Pillow
 - Generates two variants:
	 1. full ASCII
	 2. background removed ASCII

## API Endpoint
### POST /convert
Converts uploaded image to ASCII art.  
**Request:** Uploaded image  
Generated images are saved in app/temp/
 - uuid_full.png
 - uuid_no_bg.png

## Project Status
- Backend pipeline complete
- ASCII + effects complete
- Frontend UI: upcoming
