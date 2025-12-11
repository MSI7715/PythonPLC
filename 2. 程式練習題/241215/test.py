import cv2
import numpy as np

img = cv2.imread('point_card.png')
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lowRange = np.array([0, 123, 100])
highRange = np.array([5, 255, 255])

mask = cv2.inRange(hsvImg, lowRange, highRange)

"""
#侵蝕與膨脹
kernel = np.ones((3, 3), np.uint8)
erodeImg = cv2.erode(mask, kernel)
cv2.imshow("erode", erodeImg)
cv2.imshow('mask', mask)
newMask = cv2.dilate(erodeImg, kernel)
cv2.imshow("new mask", newMask)
"""

#中位數模糊
newMask = cv2.medianBlur(mask, 3)
cv2.imshow("mask", mask)
cv2.imshow("new mask", newMask)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for cnt in contours:
    (x, y, w, h) = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 3)
cv2.imshow("NewImage", img)
cv2.waitKey(0)