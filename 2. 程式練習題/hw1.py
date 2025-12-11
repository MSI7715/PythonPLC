import cv2

list_pic = ['picture\Lenna.jpg', 'picture\save.png']
for new_img in list_pic:
    new_images = cv2.imread(new_img)
    p1 = (100, 80)
    p2 = (150, 100)
    thickness = 2
    color = (0, 255, 0)
    new_images = cv2.rectangle(new_images, p1, p2, color, thickness)
    cv2.imwrite('picture/rectangle_' + new_img, new_images)
    cv2.imshow(new_img, new_images)    
cv2.waitKey(0)