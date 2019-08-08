import cv2 as cv

img1 = cv.imread("H:\GitHub\CVStudy\Addition\\batman.png")

img2 = cv.imread("H:\GitHub\CVStudy\Addition\Superman.png")

imgResultado = cv.addWeighted(img1,0.8, img2, 1, 0)

cv.imshow("Imagem resultado", imgResultado )
cv.waitKey(0)
cv.destroyAllWindows()