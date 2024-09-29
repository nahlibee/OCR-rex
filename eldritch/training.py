import spacy
from spacy.pipeline import EntityRuler
from spacy.language import Language

# Load the French language model
nlp = spacy.load('fr_core_news_sm')

# Define a function to create the EntityRuler
@Language.factory("custom_entity_ruler")
def create_entity_ruler(nlp, name):
    patterns = [
        
        {"label": "ID_NUMBER", "pattern": [{"TEXT": {"REGEX": "^[A-Z]{2}\\d+$"}}]}
    ]
    ruler = EntityRuler(nlp)
    ruler.add_patterns(patterns)
    return ruler

# Add the custom EntityRuler to the pipeline
nlp.add_pipe("custom_entity_ruler", before="ner")

# The input text
text = "ROYAUME DU MAROC CARTE NATIONALE D'IDENTITE Lellailoglasla YAHYA EL NAHLİ Ne le 08.09.1996 a HAY AL WIFAQ HAY AL WIFAQ FES Valable jusqu'au 17.11.2024 aleli gl pll JG7652 MH."

# Process the text with spaCy
doc = nlp(text)

# Extract custom entities
extracted_info = {}
for ent in doc.ents:
    if ent.label_ not in extracted_info:
        extracted_info[ent.label_] = []
    extracted_info[ent.label_].append(ent.text)

# Print the extracted information
for label, texts in extracted_info.items():
    print(f"{label}: {', '.join(texts)}")