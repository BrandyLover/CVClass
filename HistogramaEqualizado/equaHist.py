import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plt

img = cv.imread("H:\\GitHub\\CVClass\\Images\\einstein.jpg",0)

imgEqua = cv.equalizeHist(img)

cv.imshow("Imagem Original", img)

cv.imshow("Imagem Equalizada", imgEqua)

plt.hist(img.ravel(), 256, [0,256])
plt.figure()
plt.hist(imgEqua.ravel(), 256, [0,256])
plt.show()