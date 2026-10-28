import cv2 
img = cv2.imread('plate.jpg', 1) # read an image in the same folder, last number = 0 will give greyscale, 1 = colour image, -1 = original

cv2.imshow("Plate", img) # show the image

cv2.waitKey(0)
cv2.destroyAllWindows()
