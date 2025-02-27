import cv2
import matplotlib.pyplot as plt
import numpy as np


# Read the image
img = cv2.imread(r"D:\split_image\road-1072821_640.jpg")  # Replace with the path to your image

# Get the height and width of the image
h, w, _ = img.shape
half_height, half_width = h // 2, w // 2

# Split the image into four quadrants
TopLeft_quadrant = img[:half_height, :half_width]
TopRight_quadrant = img[:half_height, half_width:]
BottomLeft_quadrant = img[half_height:, :half_width]
BottomRight_quadrant = img[half_height:, half_width:]

# Display the original image and the quadrants
cv2.imshow('Original Image', img)
img, ax = plt.subplots()
cv2.imshow('Top Left Quadrant', TopLeft_quadrant)
cv2.imshow('Top Right Quadrant', TopRight_quadrant)
cv2.imshow('Bottom Left Quadrant', BottomLeft_quadrant)
cv2.imshow('Bottom Right Quadrant', BottomRight_quadrant)

cv2.waitKey(0)
cv2.destroyAllWindows()