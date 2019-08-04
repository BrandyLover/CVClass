import numpy as np 
from matplotlib import pyplot as plt
import cv2 as cv

img = cv.imread("~//Github//CVStudy//Images//Cinza.jpg")
plt.hist(np.ravel(img), 256, [0,256])
plt.show()
cv.imshow("Teste", img)
