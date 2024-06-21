#Import required dependencies
import shutil
import fitz
import os
from PIL import Image
#Define path to PDF file
file_path = 'gpt4all.pdf'

#Open PDF file
pdf_file = fitz.open(file_path)

#Calculate number of pages in PDF file
page_nums = len(pdf_file)

#Create empty list to store images information
images_list = []

#Extract all images information from each page
for page_num in range(page_nums):
    page_content = pdf_file[page_num]
    images_list.extend(page_content.get_images())

#print(images_list)
#Raise error if PDF has no images
if len(images_list)==0:
    raise ValueError(f'No images found in {file_path}')

# Clear existing images in the 'images/' folder
folder_path = 'images/'
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print(f"Failed to delete {file_path}. Reason: {e}")

#Save all the extracted images
for i, image in enumerate(images_list, start=1):
    #Extract the image object number
    xref = image[0]
    #Extract image
    base_image = pdf_file.extract_image(xref)
    #Store image bytes
    image_bytes = base_image['image']
    #Store image extension
    image_ext = base_image['ext']
    #Generate image file name
    image_name = str(i) + '.' + image_ext
    #Save image
    with open(os.path.join('images/', image_name) , 'wb') as image_file:
        image_file.write(image_bytes)
        image_file.close()