import bioformats
import javabridge
import numpy as np


def read_czi_image(file_path):
    # Start the Java Virtual Machine (JVM)
    javabridge.start_vm(class_path=bioformats.JARS)

    # Open the .czi file
    reader = bioformats.ImageReader(file_path)

    # Get the dimensions of the image
    size_x = reader.getSizeX()
    size_y = reader.getSizeY()
    size_z = reader.getSizeZ()
    size_c = reader.getSizeC()

    # Read the image data into a NumPy array
    image_data = reader.read(z=0, t=0, series=0, rescale=False)

    # Close the reader and stop the JVM
    reader.close()
    javabridge.kill_vm()

    # Reshape the data to match the dimensions (channels, height, width)
    image_data = image_data.reshape((size_c, size_y, size_x))

    return image_data


if __name__ == "__main__":
    # Replace this line with the actual path to the "1.czi" file in the Downloads folder
    czi_file_path = "/Users/abasaltbahrami/Downloads/1.czi"

    # Read the .czi file
    multi_channel_image = read_czi_image(czi_file_path)

    # Now you can work with the multi_channel_image NumPy array
    print("Shape of the multi-channel image:", multi_channel_image.shape)
    # The array contains the image data with dimensions (channels, height, width)
    # Access individual channels like: multi_channel_image[channel_index]
