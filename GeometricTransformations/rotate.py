import cv2 as cv
import numpy as np

imgOriginal = cv.imread("H:\\GitHub\\CVStudy\\Images\\einstein.jpg", 0)
totalLinhas,totalColunas = imgOriginal.shape

mat = cv.getRotationMatrix2D((totalColunas/2, totalLinhas/2), 45, 1)

imgRotate = cv.warpAffine(imgOriginal, mat, (totalColunas, totalLinhas))

cv.imshow("Imagem Rotacionada", imgRotate)
cv.waitKey(0)
