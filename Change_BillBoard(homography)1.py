import cv2
import numpy as np


# work with mouse
def draw_circle(event, x, y, flags, param):
    global points, image
    if event == cv2.EVENT_LBUTTONDBLCLK:
        points.append([x, y])
        cv2.circle(image_copy, (x, y), 5, (0, 0, 255), -1, cv2.LINE_AA)


def perspective(image, points):
    (tl, tr, br, bl) = points
    width = np.sqrt(((tl[1] - tr[1]) ** 2) + ((tl[0] - tr[0]) ** 2))
    height = np.sqrt(((tl[1] - bl[1]) ** 2) + ((tl[0] - bl[0]) ** 2))

    src = np.float32([points])
    dst = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
    M = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(image, M, (int(width), int(height)))
    return result, width, height, dst, src




points = []
image = cv2.imread("billboard2.jpg")
image_copy = image.copy()
image2 = cv2.imread("hacker.jpg")

cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_circle)


while True:
    cv2.imshow("image", image_copy)

    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord("h"):
        if len(points) == 4:
            result, width, height, dst, src = perspective(image, points)
            cv2.imshow("final", result)

            image2 = cv2.resize(image2, (int(width), int(height)))
            cv2.imshow("Image2 Resized", image2)

            points2 = np.array([[int(points[0][0]), int(points[0][1])], [int(points[1][0]), int(points[1][1])],
                                [int(points[2][0]), int(points[2][1])],[int(points[3][0]), int(points[3][1])]],
                               dtype="int32")

            cv2.polylines(image_copy, [points2], True, (0, 255, 0), 3, cv2.LINE_AA)

################################################################################################
            M, mask = cv2.findHomography(dst, src, cv2.RANSAC, 1)
            height, width, channel = image.shape

            img = cv2.warpPerspective(image2, M, (width, height))

            mask2 = np.zeros(image.shape, dtype="uint8")

            goshe2 = np.int32(points2)
            channel2 = image.shape[2]
            ignare_mask_color2 = (255,) * channel2
            cv2.fillConvexPoly(mask2, goshe2, ignare_mask_color2)

            mask2 = cv2.bitwise_not(mask2)

            masked_image2 = cv2.bitwise_and(image, mask2)

            final = cv2.bitwise_or(img, masked_image2)
            cv2.imshow("final", final)
            cv2.imwrite("Banner_Picture.png", final)

cv2.destroyAllWindows()