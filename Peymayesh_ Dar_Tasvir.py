import cv2
import time
import numpy as np

(window_W, window_H) = (100, 100)
stepSize = 50

img = cv2.imread("car2.jpg")
clone = img.copy()
crop = []

while True:
    for x in range(0, img.shape[0], stepSize):
        for y in range(0, img.shape[1], stepSize):
            if (x + window_W >= clone.shape[1]) or (y + window_H >= clone.shape[0]) :
                continue

            cv2.rectangle(clone, (x, y), (x + window_W, y + window_H), (255,0,0), 5)

            crop = img[x: x + window_W, y: y + window_H]

            cv2.imshow("Clone", clone)
            cv2.imshow("Crop", crop)
            time.sleep(0.25)
            clone = img.copy()
            key = cv2.waitKey(1)
            if key == 27:
                break
        if key == 27:
            break
    if key == 27:
        break

cv2.destroyAllWindows()


