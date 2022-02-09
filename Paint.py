import cv2
import numpy as np

draw = False

def nothing(x):
    pass


def brush(event, x, y, flags, param):

    global draw, r, g, b, size

    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True

    elif event == cv2.EVENT_MOUSEMOVE:

        if draw == True:
            cv2.circle(img, (x, y), size, (b, g, r), -1, cv2.LINE_AA)

    elif event == cv2.EVENT_LBUTTONUP:
        draw = False


img = np.zeros((480, 640, 3), dtype="uint8")
img[:] = 255

cv2.namedWindow("Paper")
cv2.setMouseCallback("Paper", brush)

cv2.namedWindow("setting")
cv2.createTrackbar("Blue", "setting", 0, 255, nothing)
cv2.createTrackbar("Green", "setting", 0, 255, nothing)
cv2.createTrackbar("Red", "setting", 0, 255, nothing)
cv2.createTrackbar("Size", "setting", 3, 12, nothing)


while True:

    b = cv2.getTrackbarPos("Blue", "setting")
    g = cv2.getTrackbarPos("Green", "setting")
    r = cv2.getTrackbarPos("Red", "setting")
    size = cv2.getTrackbarPos("Size", "setting")

    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break

    # clear Image
    elif key == ord("r"):
        img[:] = 255

    # save Image
    elif key == ord("s"):
        cv2.imwrite("Paper.png", img)
        
    cv2.imshow("Paper", img)


cv2.destroyAllWindows()
