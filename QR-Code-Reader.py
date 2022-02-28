import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread("qr-code.png")
informations = decode(img)

for info in informations:
    data = info.data.decode()
    data = data.split()
    print(data)
    data = list(data)
    print(len(data))



    pts = np.array([info.polygon], np.int32).reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, (0, 255, 0), 5, cv2.LINE_AA)

    pts2 = info.rect
    print(pts2)

    cv2.putText(img, f"{data[3:5]}", (pts2[0], pts2[1]+10),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(img, f"{data[5:7]}", (pts2[0], pts2[1]+60),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

