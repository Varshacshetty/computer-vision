import cv2
import numpy as np

# Reading the image
image = cv2.imread(r'D:\rotation\images.jfif')
 
# dividing height and width by 2 to get the center of the image
height, width = image.shape[:2]
# get the center coordinates of the image to create the 2D rotation matrix
center = (width/2, height/2)
 
# using cv2.getRotationMatrix2D() to get the rotation matrix
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=45, scale=1)
 
# rotate the image using cv2.warpAffine
rotated_image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))

# get tx and ty values for translation
# you can specify any value of your choice
tx, ty = width / 4, height / 4
 
# create the translation matrix using tx and ty, it is a NumPy array 
translation_matrix = np.array([
    [1, 0, tx],
    [0, 1, ty]
], dtype=np.float32)
# apply the translation to the image
translated_image = cv2.warpAffine(src=image, M=translation_matrix, dsize=(width, height))

# Desired width
new_width = 800

# Calculate the aspect ratio
aspect_ratio = height / width
new_height = int(new_width * aspect_ratio)

# Resize the image
scale_image = cv2.resize(image, (new_width, new_height))

 
cv2.imshow('Original image', image)
cv2.imshow('scaled image',scale_image)
cv2.imshow('Rotated image', rotated_image)
cv2.imshow('Translated image', translated_image)
# wait indefinitely, press any key on keyboard to exit
cv2.waitKey(0)
# save the rotated image to disk
cv2.imwrite('Original image', image)
cv2.imwrite('scaled image',scale_image)
cv2.imwrite('rotated_image.jpg', rotated_image)
cv2.imwrite("translated_image.jpg", translated_image);