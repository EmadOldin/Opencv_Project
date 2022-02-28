import cv2
import numpy as np

billboard = cv2.imread("billboard3.jpg")
billboard_copy = billboard.copy()
image = cv2.imread("hadis2.jpg")

# Found points of billboard and setting image points
billboard_points = np.array([[136, 67], [490, 69], [487, 247], [138, 250]])
image_points = np.array([[0,0], [image.shape[1], 0], [image.shape[1], image.shape[0]], [0, image.shape[0]]])

# found matrix of banner and change it
matrix_location, mask = cv2.findHomography(image_points, billboard_points)
result1 = cv2.warpPerspective(image, matrix_location, (billboard.shape[1], billboard.shape[0]))

# Fill billboard with image
cv2.fillConvexPoly(billboard_copy, billboard_points, 0, 16)
result2 = billboard_copy + result1

cv2.imshow("billboard", billboard)
cv2.imshow("image", image)
cv2.imshow("result1", result1)
cv2.imshow("result2", result2)

cv2.imwrite("Banner_Picture.png", result2)


cv2.waitKey(0)
cv2.destroyAllWindows()

