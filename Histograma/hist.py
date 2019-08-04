import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
<<<<<<< HEAD

img = cv.imread("H:\GitHub\CVStudy\Images\colorida.jpg")
    

plt.hist(img.ravel(), 256, [0,256])
cv.imshow("Imagem", img)
plt.show()
=======
import cv2 as cv

img = cv.imread("~//Github//CVStudy//Images//Cinza.jpg")
plt.hist(np.ravel(img), 256, [0,256])
plt.show()
cv.imshow("Teste", img)
>>>>>>> 35cab087ce8cc34ec43f25a3e9c4ba1a4da200bf
