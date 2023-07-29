from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def make_bright_spots_green(image_path, threshold=200):
    # Load the image
    img = Image.open(image_path)

    # Convert the image to grayscale
    img_gray = img.convert("L")

    # Convert the grayscale image to a NumPy array for easier manipulation
    img_array = np.array(img_gray)

    # Find bright spots based on the threshold (adjust the threshold value as needed)
    bright_spots = img_array > threshold

    # Set the color of bright spots to green
    green_color = np.array([0, 255, 0], dtype=np.uint8)

    # Flatten the image and boolean arrays
    img_array_flat = img_array.flatten()
    bright_spots_flat = bright_spots.flatten()

    # Set the color of bright spots to green in the flattened array
    img_array_flat[bright_spots_flat] = green_color[0]

    # Reshape the modified flat array back to the original image shape
    img_array_modified = img_array_flat.reshape(img_array.shape)

    # Convert the modified NumPy array back to an Image object
    green_img = Image.fromarray(img_array_modified)

    # Display the modified image without saving
    plt.imshow(green_img)
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    image_path = "/Users/abasaltbahrami/My Drive/VisualStudio/MF_Cell_Analysis/A7R5_B0uT_t30min_Noco_40x_5_nucleus.czi.png_files/actin.png"
    make_bright_spots_green(image_path)
