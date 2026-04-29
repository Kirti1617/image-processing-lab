import cv2
import numpy as np

img = cv2.imread(r'C:\Users\kirti\OneDrive\Desktop\KRMU\image processing lab\im.jpeg', 0)
kernel = np.ones((5,5), np.uint8)

dilation = cv2.dilate(img, kernel, iterations=1)
erosion = cv2.erode(img, kernel, iterations=1)

cv2.imshow("Dilation", dilation)
cv2.imshow("Erosion", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()