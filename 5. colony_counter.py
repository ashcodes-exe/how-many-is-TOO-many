import cv2
import matplotlib.pyplot as plt
image_grey = cv2.imread('img_2.tif', 0)

ret, thresh1 = cv2.threshold(image_grey, 140, 255, cv2.THRESH_BINARY) # converts to grayscale binary: black & white

image_edged = cv2.Canny(image_grey, 50, 100)
contours, hierarchy = cv2.findContours(image_edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # shows density of colonies

cnt_areas = [cv2.contourArea(c) for c in contours]
cnt_areas_selected = [i for i in cnt_areas if i>5 and i<50]

print("Number of bacterial colonies:", len(cnt_areas_selected))
