import cv2
import numpy as np

img = np.zeros((200, 400, 3), dtype="uint8")

def nothing(x):
    print(x)

cv2.namedWindow("Color")

cv2.createTrackbar("B", "Color", 0, 255, nothing)
cv2.createTrackbar("G", "Color", 0, 255, nothing)
cv2.createTrackbar("R", "Color", 0, 255, nothing)


while True:
    cv2.imshow("Color", img)

    b = cv2.getTrackbarPos("B", "Color")
    g = cv2.getTrackbarPos("G", "Color")
    r = cv2.getTrackbarPos("R", "Color")

    img[:] = [b, g, r]

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()