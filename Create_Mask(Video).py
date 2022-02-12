import cv2
import numpy as np


def nothing(x):
    pass

frame = cv2.VideoCapture(0)


cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("US", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 0, 255, nothing)

while True:
    result, img = frame.read()

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("LH", "Tracking")
    ls = cv2.getTrackbarPos("LS", "Tracking")
    lv = cv2.getTrackbarPos("LV", "Tracking")

    uh = cv2.getTrackbarPos("UH", "Tracking")
    us = cv2.getTrackbarPos("US", "Tracking")
    uv = cv2.getTrackbarPos("UV", "Tracking")

    lower = np.array([lh, ls, lv])

    upper = np.array([uh, us, uv])

    mask = cv2.inRange(img_hsv, lower, upper)

    result_img = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("img", img)
    cv2.imshow("img_hsv", img_hsv)
    cv2.imshow("mask", mask)
    cv2.imshow("result_img", result_img)

    if cv2.waitKey(1) & 0xFF == 27:
        break


frame.release()
cv2.destroyAllWindows()
