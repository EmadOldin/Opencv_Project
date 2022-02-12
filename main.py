import cv2
import numpy as np

image = cv2.imread("Noisy_smooke.jpg")
##################Blur Image##################
blur9 = cv2.blur(image, (3, 3))
blur25 = cv2.blur(image, (5, 5))
blur49 = cv2.blur(image, (7, 7))
blur121 = cv2.blur(image, (11, 11))

blurred_image = np.vstack([np.hstack([blur9, blur25]), np.hstack([blur49, blur121])])

cv2.imshow("Blurred Image", blurred_image)
cv2.imshow("Image", image)
##############################################





cv2.waitKey(0)
cv2.destroyAllWindows()
