import cv2
import numpy as np

def nothibg(x):
    pass
#
# img = np.zeros((480, 640, 3), dtype="uint8")
# img[:] = 255
img = cv2.imread("hacker.jpg")

drawing = False
font = cv2.FONT_HERSHEY_PLAIN

def found(event, x, y, flags, param):
    global img, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.putText(img, f"{x},{y}", (x, y), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.namedWindow("Paper")
cv2.setMouseCallback("Paper", found)

while True:
    key = cv2.waitKey(1) & 0xFF
    cv2.imshow("Paper", img)

    if key == 27:
        break

cv2.destroyAllWindows()