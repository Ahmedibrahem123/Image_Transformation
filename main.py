# import required packages
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# read image
image = cv.imread('image2.jpg')
cv.imshow('Original', image)
plt.imshow(image)
plt.axis('off')
plt.title("First")
plt.show()

# convert to gray scale
grayscale = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', grayscale)
plt.imshow(grayscale)
plt.axis('off')
plt.title("second")
plt.show()
'''# using equalization histogram
equ = cv.equalizeHist(image)
res = np.hstack((image, equ))
cv.imwrite('NEW2.jpg',res)
plt.imshow(image)
plt.axis('off')
plt.title("third")
plt.show()'''