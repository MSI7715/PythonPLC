import cv2
img = cv2.imread('picture\Lenna.jpg')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('picture\save.png', img1)