import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


def detect_circles(image_path, dp, minDist, param1, param2, minRadius, maxRadius):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image_height, image_width = image.shape
    blurred = cv2.GaussianBlur(image, (9, 9), 2)
    circles = cv2.HoughCircles(
        blurred, cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius
    )

    total_image_area = image_height * image_width
    if circles is not None:
        circles = np.uint16(np.around(circles))
        total_contour_area = 0
        for circle in circles[0, :]:
            center = (circle[0], circle[1])
            radius = circle[2]
            cv2.circle(image, center, radius, (0, 255, 0), 2)
            circle_area = np.pi * radius ** 2
            total_contour_area += circle_area

        percentage_covered = (total_contour_area / total_image_area) * 100
        result_label.config(
            text=f"Confidence for {os.path.basename(image_path)}: {percentage_covered:.2f}%")
    else:
        result_label.config(
            text=f"No circles detected in {os.path.basename(image_path)}.")

    # Display the processed image in the Tkinter app
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(image)
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img


def browse_image():
    global image_filename
    image_filename = filedialog.askopenfilename()
    image_path_label.config(text="Image: " + os.path.basename(image_filename))


def detect_button_callback():
    dp = float(dp_entry.get())
    minDist = float(minDist_entry.get())
    param1 = float(param1_entry.get())
    param2 = float(param2_entry.get())
    minRadius = int(minRadius_entry.get())
    maxRadius = int(maxRadius_entry.get())

    detect_circles(image_filename, dp, minDist, param1,
                   param2, minRadius, maxRadius)


# Create the main application window
app = tk.Tk()
app.title("Circle Detection App")

# Create and pack the widgets
browse_button = tk.Button(app, text="Browse Image", command=browse_image)
browse_button.pack()

image_path_label = tk.Label(app, text="Image:")
image_path_label.pack()

dp_label = tk.Label(app, text="dp:")
dp_label.pack()
dp_entry = tk.Entry(app)
dp_entry.pack()

minDist_label = tk.Label(app, text="minDist:")
minDist_label.pack()
minDist_entry = tk.Entry(app)
minDist_entry.pack()

param1_label = tk.Label(app, text="param1:")
param1_label.pack()
param1_entry = tk.Entry(app)
param1_entry.pack()

param2_label = tk.Label(app, text="param2:")
param2_label.pack()
param2_entry = tk.Entry(app)
param2_entry.pack()

minRadius_label = tk.Label(app, text="minRadius:")
minRadius_label.pack()
minRadius_entry = tk.Entry(app)
minRadius_entry.pack()

maxRadius_label = tk.Label(app, text="maxRadius:")
maxRadius_label.pack()
maxRadius_entry = tk.Entry(app)
maxRadius_entry.pack()

detect_button = tk.Button(app, text="Detect Circles",
                          command=detect_button_callback)
detect_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

# Label to display the processed image
image_label = tk.Label(app)
image_label.pack()

# Set default values
default_dp = 1.0
default_minDist = 10.0
default_param1 = 15.0
default_param2 = 15.0
default_minRadius = 4
default_maxRadius = 20

# Set initial values for entry fields
dp_entry.insert(0, default_dp)
minDist_entry.insert(0, default_minDist)
param1_entry.insert(0, default_param1)
param2_entry.insert(0, default_param2)
minRadius_entry.insert(0, default_minRadius)
maxRadius_entry.insert(0, default_maxRadius)


def reset_default_values():
    dp_entry.delete(0, tk.END)
    minDist_entry.delete(0, tk.END)
    param1_entry.delete(0, tk.END)
    param2_entry.delete(0, tk.END)
    minRadius_entry.delete(0, tk.END)
    maxRadius_entry.delete(0, tk.END)

    dp_entry.insert(0, default_dp)
    minDist_entry.insert(0, default_minDist)
    param1_entry.insert(0, default_param1)
    param2_entry.insert(0, default_param2)
    minRadius_entry.insert(0, default_minRadius)
    maxRadius_entry.insert(0, default_maxRadius)


reset_button = tk.Button(app, text="Reset Defaults",
                         command=reset_default_values)
reset_button.pack()

# Start the main event loop
app.mainloop()
