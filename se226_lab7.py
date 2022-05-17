import cv2

image= cv2.imread('C:/Users/ardas/Desktop/jpeg_example.jpg')

cv2.imshow('Original_Image', image)

b,g,r = cv2.split(image)

cv2.imshow("Model Blue Image", b)

cv2.imshow("Model Green Image", g)

cv2.imshow("Model Red Image", r)

b[:,:] = 220

merged_image = cv2.merge([b, g, r])

cv2.imshow("Merged Image", merged_image)

cv2.waitKey(0)
