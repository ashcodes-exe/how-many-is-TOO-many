import cv2 
img = cv2.imread('plate.jpg', 1) # read an image in the same folder, last number = 0 will give greyscale, 1 = colour image, -1 = original

import matplotlib.pyplot as plt
plt.imshow(img)
plt.axis('on') # turn on axes showing
plt.show()
