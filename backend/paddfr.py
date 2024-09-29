import cv2
from paddleocr import PaddleOCR, draw_ocr
import matplotlib.pyplot as plt
import spacy
from gliner_spacy.pipeline import GlinerSpacy
import re





img_path = r'C:\Users\yahya\Desktop\OCR rex\ressources\inputs\cinn.jpg'

img = cv2.imread(img_path)


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#croping the image
x=int(img.shape[0]/4)

y=int(img.shape[1]-img.shape[1]/9.5)

crop = img[x::, 0:y]  
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the cropped image
cv2.imwrite("cropped_image.jpg", crop)
img = cv2.imread("cropped_image.jpg")
# Initialize PaddleOCR
ocr = PaddleOCR(lang='en')

# Perform OCR
result = ocr.ocr(img)
boxes = [res[0] for res in result[0]]
texts = [res[1][0] for res in result[0]]
scores = [res[1][1] for res in result[0]]
#select only the high confidence text
confident=[]
for res in result[0]:
    if res[1][1]>0.7:
        confident.append(res[1][0])
        

# Combine OCR results into a single text for NER
full_text = " ".join(confident)
print(full_text)








# Use a font file that supports and French
font_path = r'C:\Windows\Fonts\arial.ttf'  # Replace with the path to the Noto Sans font file

# Visualize OCR results with annotations
annotated_img = draw_ocr(img, boxes, texts, scores, font_path=font_path)

# Display the annotated image
plt.figure(figsize=(10, 10))
plt.imshow(annotated_img)
plt.axis('off')
plt.show()

# Load spaCy model
nlp=spacy.load("en_core_web_sm")
nlp.add_pipe("gliner_spacy",config={"labels":["person","adress","date","id"]})



doc=nlp(full_text)

"""#print the detected entities
for ent in doc.ents:
    print(ent.text,ent.label_)"""


#extracting the entities
for ent in doc.ents:
    if ent.label_== "person":
        print( ent.text)
        full_text = full_text.replace(ent.text, "")
        name=ent.text
        break
for ent in doc.ents:
    if ent.label_== "date":
        print( ent.text)
        full_text = full_text.replace(ent.text, "")
        dob=ent.text
        
        break

x = re.findall(r'[A-Z]{2}\d+', full_text)
print(x)
#extracting the adress
for i in full_text :
    
    if (i.isupper()==False and i !=" "):
    
        full_text=full_text.replace(i,"")
print(full_text)
full_text=full_text[5:-8]
print(full_text)
adress=full_text
line= [str(name)]+[str(adress)]+[str(dob)]+[str(x)]

print(line)





