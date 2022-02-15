import cv2
import numpy as np
import matplotlib.pyplot as plt
 
original = cv2.imread('img4.jpg', 1)

image = cv2.resize(original, (512, 512))

#Convolving the "Image" wrt kernel_1 and kernel_2

k1 = np.array(([-1, -2, -1], [0, 0, 0], [1, 2, 1]), np.float32)

k2 = np.array(([-1, 0, 1], [-2, 0, 2], [-1, 0, 1]), np.float32)

image1 = np.absolute(cv2.filter2D(image, -1, k1))

image2 = np.absolute(cv2.filter2D(image, -1, k2))

image_output = cv2.add(image1, image2)

cv2.imshow('The Original Image', original)
cv2.imshow('resized image', image) 
cv2.imshow('image_1', image1)
cv2.imshow('image_2', image2)
cv2.imshow('output image', image_output)

cv2.waitKey(0)

cv2.destroyAllwindows()