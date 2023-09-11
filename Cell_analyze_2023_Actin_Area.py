import cv2
import os

# Directory containing the images
directory_path = '/Users/abasaltbahrami/Downloads/Cell_2023/CTR/'

# Get a list of all files in the directory whose names include "Actin" and end with ".tif"
image_files = [f for f in os.listdir(
    directory_path) if "Actin" in f and f.endswith('.tif')]

# Define minimum and maximum contour sizes
min_contour_size = 30000  # Adjust as needed
max_contour_size = 1000000  # Adjust as needed

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

    for contour in contours:
        # Calculate the area of the contour
        total_area_inside = cv2.contourArea(contour)

        # Check if the contour size is within the desired range
        if min_contour_size <= total_area_inside <= max_contour_size:
            # Draw contours on the original image (in blue)
            cv2.drawContours(original_image, [contour], -1, (255, 0, 0), 2)

            print(
                f"Total Area Inside Object in {image_file}: {total_area_inside} pixels")

    # Display the original image with selected contour outlines
    cv2.imshow(f'Image with Contours ({image_file})', original_image)

    # Wait for a key press (add a delay of e.g., 200 milliseconds)
    cv2.waitKey(0)

    # Close the image window when any key is pressed
    cv2.destroyAllWindows()

# Close all windows after processing all images
# cv2.destroyAllWindows()
