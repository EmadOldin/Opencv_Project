import cv2
import time
import numpy as np

img = np.zeros((100, 300, 3), dtype="uint8")
cv2.rectangle(img, (0, 33), (300, 66), (165, 207, 0), 3, cv2.LINE_AA)


mazrab_dah = [i for i in range(5,301) if i % 10 == 0]


for dah in mazrab_dah:
    cv2.rectangle(img, (dah - 5, 36), (dah, 63), (165, 0, 207), -1, cv2.LINE_AA)
    cv2.imshow("Image", img)
    cv2.waitKey(5)
    time.sleep(1.0)


cv2.waitKey(0)
cv2.destroyAllWindows()
