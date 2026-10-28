# How-many-is-TOO-many
A colony counter using contouring and edge-detection (ImageJ who?)

# CFU Counter

A step-by-step computer vision pipeline for counting bacterial colonies from a 
plate image, built while learning OpenCV. Kept as five sequential files to show 
the actual build process, from loading and viewing an image, to final automated 
colony counting.

While tools like ImageJ and Fiji do this easily, I wanted to see if this could be done from a root-level without a GUI's help. 

## What each step does
1. **Load and display**: reading and showing a plate image with OpenCV
2. **Display with matplotlib**: an alternative way to visualize the same image
3. **Colour conversion**: converting BGR to HSV color space
4. **Inspect pixel data**: viewing the raw pixel matrix and image shape
5. **Colony counter**: grayscale thresholding, Canny edge detection, contour 
   extraction, and area-based filtering to isolate and count colonies

## Built with
Python, OpenCV, Matplotlib

## Before you run
pip install opencv-python matplotlib
