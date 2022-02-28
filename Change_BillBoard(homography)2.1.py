import cv2
import numpy as np

image = cv2.imread("car2.jpeg")
billboard = cv2.imread("billboard1.jpg")
copy_billboard = billboard.copy()


billboard_points = np.array([[260,106],[594,47],[607,306],[264,335]])
image_points = np.array([[0,0],[image.shape[1], 0],[image.shape[1], image.shape[0]],[0, image.shape[0]]])

homographyMat, mask = cv2.findHomography(image_points, billboard_points)

result1 = cv2.warpPerspective(image, homographyMat, (billboard.shape[1], billboard.shape[0]))

cv2.fillConvexPoly(copy_billboard, billboard_points, 0, 16)
cv2.imshow("copy billboard", copy_billboard)

result2 = copy_billboard + result1

cv2.namedWindow("billboard", cv2.WINDOW_NORMAL)
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.namedWindow("result1", cv2.WINDOW_NORMAL)
cv2.namedWindow("result2", cv2.WINDOW_NORMAL)


cv2.imshow("billboard", billboard)
cv2.imshow("image", image)
cv2.imshow("result1", result1)
cv2.imshow("result2", result2)

cv2.waitKey(0)

cv2.destroyAllWindows()