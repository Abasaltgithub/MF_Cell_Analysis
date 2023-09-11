import cv2
import numpy as np
import os
import csv

# Define the directory path
directory_path = '/Users/abasaltbahrami/Downloads/Cell_2023/CTR/'

# Create a list to store the data
data = []

# List all files in the directory
file_list = os.listdir(directory_path)

# Iterate through the files in the directory
for file_name in file_list:
    # Check if the file is an image and contains the name 'Tubulin'
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tif', '.tiff')) and 'Tubulin' in file_name:
        # Construct the full image path
        image_path = os.path.join(directory_path, file_name)

        # Open the image using OpenCV
        original_image = cv2.imread(image_path)

        # Convert the image to grayscale
        img_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        img_gray_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

        # Convert the grayscale image to a binary image using adaptive thresholding
        _, img_binary = cv2.threshold(
            img_gray_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Perform morphological operations to further clean up the binary image
        kernel = np.ones((3, 3), np.uint8)
        img_binary = cv2.erode(img_binary, kernel, iterations=1)
        img_binary = cv2.dilate(img_binary, kernel, iterations=1)

        # Count the number of bright pixels (white pixels) in the binary image
        bright_pixel_count = np.sum(np.array(img_binary) > 0)

        # Append the data to the list
        data.append([file_name, bright_pixel_count])

        # Display the image with contours
        cv2.imshow(f'Image with Contours ({image_path})', img_binary)

        # Print the file name and bright pixel count
        print(
            f"File Name: {file_name}, Bright Pixel Count: {bright_pixel_count}")

        # Wait for a key press (add a delay of e.g., 200 milliseconds)
        cv2.waitKey(0)

        # Close the image window when any key is pressed
        cv2.destroyAllWindows()

# Specify the CSV file path where you want to save the data
csv_file_path = '/Users/abasaltbahrami/Downloads/Cell_2023/bright_pixel_counts.csv'

# Write the data to a CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write the header
    csv_writer.writerow(['File Name', 'Bright Pixel Count'])
    csv_writer.writerows(data)

# Print a message to confirm that the data has been saved
print(f"Data has been saved to {csv_file_path}")
