import cv2
import numpy as np

image = cv2.imread("Noisy_smooke.jpg")
img = np.float64(image)

noise = np.random.randn(*img.shape) * 50
noisy_image = img + noise
noisy_image = np.uint8(np.clip(noisy_image, 0, 255))

cv2.imshow("Image with Noise", np.hstack([image, noisy_image]))
cv2.imshow("Noise", noise)

cv2.imwrite("Noisy_smooke.jpg", noisy_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
