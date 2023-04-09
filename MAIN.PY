import spacy
from spacy.tokens import DocBin

nlp = spacy.load("en_core_web_lg")
ruler = nlp.add_pipe("span_ruler", name="ruler")

patterns = [{"label": "Effective Date", "pattern": [
    {"ENT_TYPE": "DATE", "OP": "{4,}"},
    {"TEXT": '('},
    {"TEXT": 'the'},
    {"TEXT": '"'},
    {"TEXT": 'Effective'},
    {"TEXT": 'Date'},
    {"TEXT": '"'},
    {"TEXT": ')'}
]}]

ruler.add_patterns(patterns)

# range 100-510 for the train folder, range 0-100 for the dev folder (split however you want).
for i in range(100, 510):

    text_open = open(f"inputfiles/ ({i}).txt", "r", encoding='utf8')
    text = text_open.read()
    doc = nlp(text)

    db = DocBin()
    for span in doc.spans["ruler"]:
            print(span.text, span.label_)

    text_open.close()


    db.add(doc)
    db.to_disk(f"./train/{i}.spacy")


