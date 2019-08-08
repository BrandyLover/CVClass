import cv2 as cv
import numpy as np

img = cv.imread("H:\GitHub\CVStudy\Images\einstein.jpg")
totLin, totCol = img.shape[:2]

matriz = np.float32([[1,0,100],[0,1,100]])
imgDeslo = cv.warpAffine(img, matriz, (totCol,totLin))

cv.imshow("Imagem Deslocada", imgDeslo)
cv.waitKey(0)