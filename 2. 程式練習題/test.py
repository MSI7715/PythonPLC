import cv2
img = cv2.imread('picture\Lenna.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image', img)
cv2.waitKey(0)