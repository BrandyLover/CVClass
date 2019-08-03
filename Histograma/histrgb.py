import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt 

img = cv.imread("H:\\GitHub\\CVClass\\Images\\colorida.jpg")
blue, green, red = cv.split(img)

plt.hist(blue.ravel(), 256, [0,256])
plt.figure()
plt.hist(green.ravel(), 256, [0,256])
plt.figure()
plt.hist(red.ravel(), 256, [0,256])

plt.show()