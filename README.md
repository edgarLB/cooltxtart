# cooltxtart
An image processing pipeline that transforms uploaded images into stylized ASCII art.

## Backend Workflow
 - Segments the subject using Mediapipe
 - Converts pixel data to ASCII characters based on luminance
 - Render ASCII back to images using Pillow
 - Generates two variants:
	 1. full ASCII
	 2. background removed ASCII

## Examples
<img width="954" height="1065" alt="example1" src="https://github.com/user-attachments/assets/da9e8a1b-2301-41a4-85f5-c053b1bc3da3" />
<img width="954" height="1065" alt="example2" src="https://github.com/user-attachments/assets/48f98fcb-d125-4f16-af8b-1e7c67deca62" />
<img width="954" height="1065" alt="example3" src="https://github.com/user-attachments/assets/f80a935c-d667-4b19-92a7-41ee51c34d19" />


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
