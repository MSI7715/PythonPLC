import cv2
import numpy as np

img = cv2.imread('picture/point_card.png')
hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lowRange = np.array([0, 123, 100])
highRange = np.array([5, 255, 255])
new_img = cv2.inRange(hsv_image, lowRange, highRange)
cv2.imshow("New Image", new_img)
# cv2.waitKey(0)
# 取輪廓
contours, _ = cv2.findContours(new_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    p1 = (x, y)
    p2 = (x + w, y + h)
    cv2.rectangle(img, p1, p2, (255, 0, 0), 2)
cv2.imshow("Result", img)
cv2.waitKey(0)
