import cv2
from paddleocr import PaddleOCR, draw_ocr
import matplotlib.pyplot as plt

# Load image
img_path = r'C:\Users\yahya\Desktop\ocrscan\ressources\inputs\cin1.jpg'
img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Initialize PaddleOCR for Arabic
ocr_arabic = PaddleOCR(lang='arabic')



# Perform OCR for Arabic
result_arabic = ocr_arabic.ocr(img)
boxes_arabic = [res[0] for res in result_arabic[0]]
texts_arabic = [res[1][0] for res in result_arabic[0]]
scores_arabic = [res[1][1] for res in result_arabic[0]]


# Combine results
boxes = boxes_arabic 
texts = texts_arabic 
scores = scores_arabic 

# Use a font file that supports both Arabic and French
font_path = r'C:\Windows\Fonts\arial.ttf'  # Replace with the path to the Noto Sans font file

# Visualize OCR results with annotations
annotated_img = draw_ocr(img, boxes, texts, scores, font_path=font_path)
    
# Display the annotated image
plt.figure(figsize=(10, 10))
plt.imshow(annotated_img)
plt.axis('off')
plt.show()