import cv2 as cv
# import matplotlib.pyplot as plt
img = cv.imread("opncvdata/scr.png", cv.IMREAD_GRAYSCALE)
print(img)
cv.imshow("dsasad", img)
cv.waitKey(0)

