import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog


def detect_circles(image_path, dp, minDist, param1, param2, minRadius, maxRadius):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image_height, image_width = image.shape
    blurred = cv2.GaussianBlur(image, (9, 9), 2)
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist,
                               param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

    total_image_area = image_height * image_width
    if circles is not None:
        total_contour_area = 0
        for circle in circles[0, :]:
            center = (circle[0], circle[1])
            radius = circle[2]
            cv2.circle(image, center, radius, (0, 255, 0), 2)
            circle_area = np.pi * radius ** 2
            total_contour_area += circle_area

        percentage_covered = (total_contour_area / total_image_area) * 100
        result_label.config(
            text=f"Confidence for {image_filename}: {percentage_covered:.2f}%")
    else:
        result_label.config(text=f"No circles detected in {image_filename}.")


def browse_image():
    global image_filename
    image_filename = filedialog.askopenfilename()
    image_path_label.config(text="Image: " + image_filename)


def detect_button_callback():
    dp = float(dp_entry.get())
    minDist = float(minDist_entry.get())
    param1 = float(param1_entry.get())
    param2 = float(param2_entry.get())
    minRadius = int(minRadius_entry.get())
    maxRadius = int(maxRadius_entry.get())

    detect_circles(image_filename, dp, minDist, param1,
                   param2, minRadius, maxRadius)


app = tk.Tk()
app.title("Circle Detection App")

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

app.mainloop()
