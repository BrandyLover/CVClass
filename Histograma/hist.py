import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("H:\GitHub\CVStudy\Images\colorida.jpg")
    

plt.hist(img.ravel(), 256, [0,256])
cv.imshow("Imagem", img)
plt.show()