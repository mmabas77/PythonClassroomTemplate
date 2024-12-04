import cv2
import numpy as np


# OpenCV Python Quiz

# Welcome to the OpenCV quiz! Follow the instructions below:
#
# 1. Complete the functions in `main.py`.
# 2. Each function corresponds to a quiz question,
#    follow instruction in comment above the function
# 3. Each function accepts a cv2 image and returns a cv2 image as well
# 4. You must use the parameters provided to the function
# 5. Do not rename the functions or change the parameters.
# 6. Push your code to your GitHub repository.

# The kernel is a tuple of two integers (x,y) eg. (5,5)
# Use it as is in the function parameters without changes

# 1. Blur an Image using GaussianBlur (2 point)
def blur_image(img, kernel, sigmaX):
    pass  # Write your code here


# 2. Apply Canny, then Dilate, then Erode (3 points)
def canny_dilate_erode(img, low_threshold, high_threshold, kernel, iterations):
    pass  # Write your code here


# 3. Convert to Grayscale (2 point)
def convert_to_grayscale(img):
    # Read the image normally **then** convert it to grayscale
    # Important: Do not read the image as grayscale
    pass  # Write your code here


# 4. Draw Rectangle (1 point)
def draw_rectangle(img, start_point, end_point, color, thickness):
    pass  # Write your code here


# 5. Resize Image (2 points)
def resize_image(img, scale_percent):
    # Scale percent is integer value eg. 20,50,70 is valid
    # Important: Use INTER_AREA interpolation
    pass  # Write your code here

