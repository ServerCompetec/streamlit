import cv2

img = cv2.imread("imagens/DKC3.jpg")

cv2.imshow("Imagem Original", img)

cv2.waitKey(0)

cv2.destroyAllWindows()