# Image to PDF Merger
A simple Python utility to convert a folder full of images (in PNG or JPG format) into a single PDF file.

## Features
- Converts all images in a specified directory into a single PDF.
- Maintains the original resolution of the images.
- Automatically orders images based on their filenames for inclusion in the PDF.
- Supports both PNG and JPG/JPEG formats.

## Usage
Install the required dependencies; `Pillow` and `reportLab`

```
pip install -r requirements.txt
```

Run the script

```
python merge.py
```

You will be prompted for the directory containing your images and the name of your output pdf.
