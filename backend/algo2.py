import cv2
from paddleocr import PaddleOCR, draw_ocr
import matplotlib.pyplot as plt
import spacy
from gliner_spacy.pipeline import GlinerSpacy
import re

def reader_back(img_path):

    # Load image
    #img_path = r'C:\Users\yahya\Desktop\OCR rex\backend\back.jpg'
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #croping the image



    cv2.waitKey(0)
    cv2.destroyAllWindows()


    # Initialize PaddleOCR
    ocr = PaddleOCR(lang='en')

    # Perform OCR
    result = ocr.ocr(img)
    boxes = [res[0] for res in result[0]]
    texts = [res[1][0] for res in result[0]]
    scores = [res[1][1] for res in result[0]]
    #select only the high confidence text

    for i in range(len(scores)-1, -1, -1):
        if scores[i]<0.8:
            del boxes[i]
            del texts[i]
            del scores[i]
            
            

    '''# Combine OCR results into a single text for NER
    full_text = " ".join(texts)
    # Use a font file that supports and French
    font_path = r'C:\Windows\Fonts\arial.ttf'  # Replace with the path to the Noto Sans font file

    # Visualize OCR results with annotations
    annotated_img = draw_ocr(img, boxes, texts, scores, font_path=font_path)

    # Display the annotated image
    plt.figure(figsize=(10, 10))
    plt.imshow(annotated_img)
    plt.axis('off')
    plt.show()'''


    for i in range(len(texts)):
        if 'Adresse' in texts[i]:
            adress=texts[i][7::]
            
    #print(full_text)
    print(adress)










    '''# Load spaCy model
    nlp=spacy.load("en_core_web_sm")
    nlp.add_pipe("gliner_spacy",config={"labels":["person","adress","date","id"]})



    doc=nlp(full_text)

    """#print the detected entities
    for ent in doc.ents:
        print(ent.text,ent.label_)"""


    #extracting the entities
    for ent in doc.ents:
        if ent.label_== "person":
            
            full_text = full_text.replace(ent.text, "")
            name=ent.text
            break
    for ent in doc.ents:
        if ent.label_== "date":
            
            full_text = full_text.replace(ent.text, "")
            dob=ent.text
            
            break

    x = re.findall(r'[A-Z]{2}\d+', full_text)[0]

    #extracting the adress
    for i in full_text :
        
        if (i.isupper()==False and i !=" "):
        
            full_text=full_text.replace(i,"")

    full_text=full_text[5:-8]

    adress=full_text
    list=[str(name)]+[str(adress)]+[str(dob)]+[str(x)]
    print(list)'''
    return adress

if __name__ == "__algo2__":

  reader_back()




