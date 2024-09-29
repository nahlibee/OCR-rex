import spacy
from gliner_spacy.pipeline import GlinerSpacy

def eraseCap(line):
    for i in range(len(line)):
        if ord(line[i])>=65 and ord(line[i])<=90:
            a=a[i:-1]
            break
def ner(a):

    nlp=spacy.load("en_core_web_sm")
    nlp.add_pipe("gliner_spacy",config={"labels":["person","adress","date","id"]})



    a=a[45:-3]
    for i in range(len(a)):
        if ord(a[i])>=65 and ord(a[i])<=90:
            b=i
            break
    a=a[b:-1]


    doc=nlp(a)



    for ent in doc.ents:
        print(ent.text,ent.label_)



    for ent in doc.ents:
        if ent.label_== "person":
            print( ent.text)
            a = a.replace(ent.text, "")
            name=ent.text
            break
    for ent in doc.ents:
        if ent.label_== "date":
            print( ent.text)
            a = a.replace(ent.text, "")
            dob=ent.text
            
            break

    for ent in doc.ents:
        if ent.label_== "id":
            print( ent.text)
            a = a.replace(ent.text, "")
            id=ent.text
            break

    print(a)
    for i in a :
        if (i.isupper()==False and i !=" "):
        
            a=a.replace(i,"")
    a=a[5:-8]
    print(a)
    adress=a


    print("name is:",name,"born in:",dob,"resides in",adress)
    return None



if __name__ =="__main__":
    ner("ROYAUME DU MAROC CARTE NATIONALE D'IDENTITE Lellailoglasla YAHYA EL NAHLI Ne le 08.09.1996 a HAY AL WIFAQ HAY AL WIFAQ FES Valable jusqu'au 17.11.2024 aleli gl pll JG7652 MH.")