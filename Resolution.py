import numpy as np
import cv2

img = cv2.imread("sozy.png")

gaussian = cv2.GaussianBlur(img, (25, 25), 0)
#averaging = cv2.blur(img, (21, 21))
#median = cv2.medianBlur(img, 5)
#bilateral = cv2.bilateralFilter(img, 9, 350, 350)

cv2.imshow("Original image", img)
cv2.imshow("Gaussian", gaussian)
#cv2.imshow("Averaging", averaging)
#cv2.imshow("Median", median)
#cv2.imshow("Bilateral", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()