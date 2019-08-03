import numpy as np 
from matplotlib import pyplot as plt
import cv2 

img = cv2.imread("H:\\GitHub\\CVClass\\Images\\colorida.jpg")
    

plt.hist(img.ravel(), 256, [0,256])
cv2.imshow("Imagem", img)
plt.show()