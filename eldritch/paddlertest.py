import cv2
from paddleocr import PaddleOCR, draw_ocr
import matplotlib.pyplot as plt

# Load image
img_path = r'C:\Users\yahya\Desktop\ocrscan\ressources\inputs\OIP.jpeg'
img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Initialize PaddleOCR for Arabic
ocr_arabic = PaddleOCR(lang='arabic')

# Initialize PaddleOCR for Latin (French)
ocr_french = PaddleOCR(lang='en')

# Perform OCR for Arabic
result_arabic = ocr_arabic.ocr(img)
boxes_arabic = [res[0] for res in result_arabic[0]]
texts_arabic = [res[1][0] for res in result_arabic[0]]
scores_arabic = [res[1][1] for res in result_arabic[0]]

# Perform OCR for French
result_french = ocr_french.ocr(img)
boxes_french = [res[0] for res in result_french[0]]
texts_french = [res[1][0] for res in result_french[0]]
scores_french = [res[1][1] for res in result_french[0]]

# Combine results
boxes = boxes_arabic + boxes_french
texts = texts_arabic + texts_french
scores = scores_arabic + scores_french

# Use a font file that supports both Arabic and French
font_path = r'C:\Windows\Fonts\arial.ttf'  # Replace with the path to the Noto Sans font file

# Visualize OCR results with annotations
annotated_img = draw_ocr(img, boxes, texts, scores, font_path=font_path)

# Display the annotated image
plt.figure(figsize=(10, 10))
plt.imshow(annotated_img)
plt.axis('off')
plt.show()