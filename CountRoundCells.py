import cv2
import numpy as np

# Path to the specific image
image_path = "/Users/abasaltbahrami/My Drive/InCor - Brazil/TestConflu/1.png"

# Parameters
brightness_threshold = 150
min_radius = 10
max_radius = 50


def count_bright_round_cells(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply adaptive thresholding to segment bright areas
    _, thresholded = cv2.threshold(
        blurred, brightness_threshold, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(
        thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize the count of bright round cells
    bright_round_cell_count = 0

    # Iterate through the contours
    for contour in contours:
        # Approximate the contour as a circle
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)

        if perimeter == 0:
            continue

        circularity = (4 * np.pi * area) / (perimeter * perimeter)

        # Check circularity and size of the contour
        if min_radius**2 * np.pi <= area <= max_radius**2 * np.pi and circularity > 0.7:
            bright_round_cell_count += 1

    # Draw contours on the original image
    image_with_contours = image.copy()
    cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)

    return bright_round_cell_count, image_with_contours


# Load the image
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Count cells and get contours
count, image_with_contours = count_bright_round_cells(image)

# Display images
cv2.imshow("Image with Contours", image_with_contours)
print(f"Image: 1.png, Number of bright round cells: {count}")

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
