import cv2
from paddleocr import PaddleOCR, draw_ocr
import matplotlib.pyplot as plt
import spacy


# Load spaCy model

nlp = spacy.load("en_core_web_sm")

# Load image

img_path = r'C:\Users\yahya\Desktop\OCR rex\ressources\inputs\cin4.jpg'
img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Initialize PaddleOCR

ocr = PaddleOCR(lang='en')

# Perform OCR

result = ocr.ocr(img)
boxes = [res[0] for res in result[0]]
texts = [res[1][0] for res in result[0]]
scores = [res[1][1] for res in result[0]]

# Combine OCR results into a single text for NER

full_text = " ".join(texts)
print(full_text)

# Process text with spaCy for NER

doc = nlp(full_text)

# Extract and categorize entities

"""entities = {
    "PERSON": [],
    "DATE": [],
    "GPE": [],  # Geographic entities (can include addresses)
}

for ent in doc.ents:
    if ent.label_ in entities:
        entities[ent.label_].append(ent.text)

# Print extracted entities

print("Names:", entities["PERSON"])
print("Dates:", entities["DATE"])
print("Addresses:", entities["GPE"])"""


# Use a font file that supports both Arabic and French

font_path = r'C:\Windows\Fonts\arial.ttf'  # Replace with the path to the Noto Sans font file

# Visualize OCR results with annotations

annotated_img = draw_ocr(img, boxes, texts, scores, font_path=font_path)

# Display the annotated image

plt.figure(figsize=(10, 10))
plt.imshow(annotated_img)
plt.axis('off')
plt.show()


def add(a,b):
    return a+b
print