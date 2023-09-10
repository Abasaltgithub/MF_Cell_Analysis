import cv2
import os

# Directory containing the images
directory_path = '/Users/abasaltbahrami/Downloads/Cell_2023/CTR/'

# Get a list of all files in the directory whose names include "Actin" and end with ".tif"
image_files = [f for f in os.listdir(
    directory_path) if "Actin" in f and f.endswith('.tif')]

for image_file in image_files:
    # Construct the full path to the image
    image_path = os.path.join(directory_path, image_file)

    # Load the image
    original_image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding to create a binary image
    _, binary_image = cv2.threshold(gray_image, 1, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(
        binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize a variable to store the total area outside
    total_area_outside = 0

    # Iterate through the contours
    for contour in contours:
        # Calculate the area of each contour and add it to the total area outside
        area = cv2.contourArea(contour)
        total_area_outside += area

    # Calculate the total area inside by subtracting the outside area from the total area of the image
    total_area_inside = (
        gray_image.shape[0] * gray_image.shape[1]) - total_area_outside

    # Print the total area inside for each image
    print(
        f"Total Area Inside Object in {image_file}: {total_area_inside} pixels")

    # Optional: Draw the external contours on the original image for visualization
    external_contours = [
        contour for contour in contours if cv2.contourArea(contour) > 0]
    cv2.drawContours(original_image, external_contours, -1,
                     (0, 0, 255), 2)  # Draw external contours in red

    # Display the original image with external contours
    cv2.imshow(f'Image with External Contours ({image_file})', original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
