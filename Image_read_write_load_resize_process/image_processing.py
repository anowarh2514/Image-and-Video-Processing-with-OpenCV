import cv2

img = cv2.imread("galaxy.jpg",-1)
print(img)
print(img.shape)
print(img.ndim)

# cv2.imshow("Galaxy",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# resize_image = cv2.resize(img,(400,500))
resize_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2.5)))
cv2.imshow("Galaxy",resize_image)
cv2.imwrite("Galaxy_resize.jpg",resize_image)
cv2.waitKey(0)
cv2.destroyAllWindows()