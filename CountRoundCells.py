import cv2
import numpy as np
import os

# Path to the directory containing the images
images_directory = "/Users/abasaltbahrami/My Drive/InCor - Brazil/TestConflu/"

# Get a list of all image files in the directory
image_files = [file for file in os.listdir(
    images_directory) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

for image_file in image_files:
    # Load the image
    image_path = os.path.join(images_directory, image_file)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(image, (9, 9), 2)

    # Detect circles using Hough Circle Transform
    circles = cv2.HoughCircles(
        blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=10, param1=20, param2=15, minRadius=5, maxRadius=15
    )

    # Convert circles to integers
    circles = np.uint16(np.around(circles))

    # Create a copy of the original image to draw contours on
    image_with_contours = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    # Draw contours and count circles
    if circles is not None:
        num_circles = len(circles[0])
        for circle in circles[0, :]:
            center = (circle[0], circle[1])
            radius = circle[2]

            # Draw the circle's contour
            cv2.circle(image_with_contours, center, radius, (0, 255, 0), 2)

        print(f"Number of circles detected in {image_file}: {num_circles}")
    else:
        print(f"No circles detected in {image_file}.")

    # Display the image with contours
    cv2.imshow(f"Image with Contours - {image_file}", image_with_contours)
    cv2.waitKey(0)

# Close all windows when done
cv2.destroyAllWindows()
