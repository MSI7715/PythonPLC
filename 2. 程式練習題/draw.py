import cv2

img = cv2.imread('picture/Lenna.jpg')
center = (150, 160)
radius = 10
color = (255, 0, 0)
thickness = 3
new_image = cv2.circle(img, center, radius, color, thickness)

p1 = (100, 80)
p2 = (150, 100)
thickness = 2
color = (0, 255, 0)
new_image = cv2.rectangle(img, p1, p2, color, thickness)

text = 'red'
position = (100, 75)
color = (0, 0, 255)
size = 2
new_image = cv2.putText(img, text, position, cv2.FONT_HERSHEY_COMPLEX, size, color)

cv2.imshow("New Image", new_image)
cv2.waitKey(0)