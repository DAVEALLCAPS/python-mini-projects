import os
from PIL import Image
from reportlab.pdfgen import canvas

def images_to_pdf(folder_path, output_filename):
    # Get all image files from the folder
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(('png', 'jpg', 'jpeg'))]

    # Sort the files to maintain an order
    image_files.sort()

    # Create a new PDF file with the page size of the first image
    c = canvas.Canvas(output_filename)
    
    for image_file in image_files:
        img_path = os.path.join(folder_path, image_file)
        img = Image.open(img_path)

        # Set canvas size to match the image dimensions
        width, height = img.size
        c.setPageSize((width, height))
        
        # Convert the image to RGB (to handle potential transparency in PNGs)
        img_rgb = img.convert("RGB")
        
        # Add the image to the PDF.
        c.drawImage(img_path, 0, 0, width=width, height=height)
        
        # Start a new page for the next image (if there are any)
        c.showPage()

    # Save the PDF
    c.save()

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder containing the images: ")
    output_filename = input("Enter the desired name for the output PDF file (including .pdf extension): ")
    
    images_to_pdf(folder_path, output_filename)
    print(f"PDF saved as {output_filename}")
