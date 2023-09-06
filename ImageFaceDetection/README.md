# Face Detection using OpenCV

This project uses OpenCV's pre-trained Haar cascades to detect faces in an image. It draws a box around faces in the image and closes with any key press.

I intend to extend this a bit to capture features and poses and save them to another file, this is a basic implementation to start.

## Setup

**Install OpenCV**

   Install the OpenCV library using pip:

   ```
   pip install opencv-python
   ```

## Usage

1. Place the image you want to detect faces in, in the project directory and rename it to `image.jpg` or modify the script to target your image's filename.

2. Run the script:

   ```
   python face_detect.py
   ```

   The script will display the image with rectangles drawn around detected faces. Press any key to close the image window.
