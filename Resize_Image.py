import cv2

img = cv2.imread("smoke.jpg")

img_resize = cv2.resize(img, (600, 500))

cv2.imwrite("car.jpg", img_resize)

cv2.imshow("img_resize", img_resize)

cv2.waitKey(0)
cv2.destroyAllWindows()