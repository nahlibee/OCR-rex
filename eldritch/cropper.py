import cv2

# Read the image
img_path = r'C:\Users\yahya\Desktop\OCR rex\ressources\inputs\cin5.jpg'
img = cv2.imread(img_path)
 
x=int(img.shape[0]/4)
y=int(img.shape[1]-img.shape[1]/10)


# Define the coordinates for the cropping box (startY:endY, startX:endX)
# [rows, columns] 
crop = img[x::, 0:y]  

# Crop the image


# Show the cropped image
#cv2.imshow("Cropped Image", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the cropped image
cv2.imwrite("cropped_image.jpg", crop)