from PIL import Image, ImageFilter
import numpy as np
import os
from scipy import ndimage

# Define the directory path
directory_path = '/Users/abasaltbahrami/Downloads/Cell_2023/CTR/'

# List all files in the directory
file_list = os.listdir(directory_path)

# Iterate through the files in the directory
for file_name in file_list:
    # Check if the file is an image and contains the name 'Tubulin'
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tif', '.tiff')) and 'Tubulin' in file_name:
        # Construct the full image path
        image_path = os.path.join(directory_path, file_name)

        # Open the image
        img = Image.open(image_path)

        # Convert the image to grayscale
        img_gray = img.convert('L')

        # Apply Gaussian blur to reduce noise
        img_gray_blur = img_gray.filter(ImageFilter.GaussianBlur(radius=2))

        # Convert the grayscale image to a binary image using adaptive thresholding
        threshold = 254.5
        img_binary = img_gray_blur.point(lambda p: p > threshold and 255)

        # Perform morphological operations to further clean up the binary image
        img_binary = ndimage.binary_erosion(
            img_binary, structure=np.ones((3, 3))).astype(bool)
        img_binary = ndimage.binary_dilation(
            img_binary, structure=np.ones((3, 3))).astype(bool)

        # Count the number of bright pixels (white pixels) in the binary image
        bright_pixel_count = np.sum(np.array(img_binary) > 0)

        # Show the binary image (optional)
        Image.fromarray(img_binary.astype(np.uint8) * 255).show()

        # Print the number of bright pixels
        print(
            f"File: {file_name}, Number of bright pixels: {bright_pixel_count}")
