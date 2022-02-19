"""
 این برنامه میاد با گرفتن 4 نقطه از کاربر(از طریق دوبار کلیک روی عکس) را گرفته
 و بخش مورد نظر را جدا میکند و یک عکس دومی هم میگیرد که آن را اندازه بخش مورد نظر میکند
"""



import cv2
import numpy as np


# در کار کردن با موس حتما از global استفاده شود
def found_locations(event, x, y, flags, param):
    global image_copy, pts
    if event == cv2.EVENT_LBUTTONDBLCLK:
        pts.append([x, y])
        cv2.circle(image_copy, (x, y), 6, (0, 0, 255), -1)


def perspective(image, points):
    (tl, tr, br, bl) = points
    width = np.sqrt(((tl[1] - tr[1]) ** 2) + ((tl[0] - tr[0]) ** 2))
    height = np.sqrt(((tl[1] - bl[1]) ** 2) + ((tl[0] - bl[0]) ** 2))

    src = np.float32([points])
    dst = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
    M = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(image, M, (int(width), int(height)))
    return result, width, height
    # return result


pts = []
image = cv2.imread("billboard1.jpg")
image_copy = image.copy()

cv2.namedWindow("Image")
cv2.setMouseCallback("Image", found_locations)



while True:
    cv2.imshow("Image", image_copy)
    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord("h"):
        if len(pts) == 4:

            # result = perspective(image, pts)
            pts2 = np.array([[int(pts[0][0]), int(pts[0][1])], [int(pts[1][0]), int(pts[1][1])], [int(pts[2][0]), int(pts[2][1])],[int(pts[3][0]), int(pts[3][1])]], dtype="int32")
            cv2.polylines(image_copy, [pts2], True, (0, 255,0), 3, cv2.LINE_AA)

            result, width, height = perspective(image, pts)
            cv2.imshow("Result", result)
#############################" For Setting New Image"##########################
            image2 = cv2.imread("car.jpg")
            image2 = cv2.resize(image2, (int(width), int(height)))
            #cv2.imshow("Image2", image2)


cv2.destroyAllWindows()
