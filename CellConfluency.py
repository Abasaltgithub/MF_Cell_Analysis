import cv2
import numpy as np
import os

# Path to the directory containing the images
images_directory = "/Users/abasaltbahrami/My Drive/InCor - Brazil/TestConflu/5x/"

# Get a list of all image files in the directory
image_files = [file for file in os.listdir(
    images_directory) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

for image_file in image_files:
    # Load the image
    image_path = os.path.join(images_directory, image_file)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image_height, image_width = image.shape

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(image, (9, 9), 2)

    # Detect circles using Hough Circle Transform
    circles = cv2.HoughCircles(
        blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=10, param1=20, param2=15, minRadius=5, maxRadius=15
    )

    # Convert circles to integers
    circles = np.uint16(np.around(circles))

    # Calculate total image area
    total_image_area = image_height * image_width

    if circles is not None:
        # Calculate total contour area
        total_contour_area = 0
        for circle in circles[0, :]:
            center = (circle[0], circle[1])
            radius = circle[2]

            # Draw the circle's contour on the image
            cv2.circle(image, center, radius, (0, 255, 0), 2)

            circle_area = np.pi * radius ** 2
            total_contour_area += circle_area

        # Calculate the percentage of the image covered by contours
        percentage_covered = (total_contour_area / total_image_area) * 100
        print(f"Confulecy for {image_file}: {percentage_covered:.2f}%")
    else:
        print(f"No circles detected in {image_file}.")

    # Display the image with contours and wait for key press
    cv2.imshow(f"Image with Contours - {image_file}", image)
    cv2.waitKey(0)

# Close all windows when done
cv2.destroyAllWindows()
