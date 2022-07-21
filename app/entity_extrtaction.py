from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

def entity_extraction(example:str):
    tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
    model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

    nlp = pipeline("ner", model=model, tokenizer=tokenizer)

    ner_results = nlp(example)

    texts_entities = {}
    for t in ner_results:
        if t['word'] in texts_entities:
            continue
        texts_entities[t['word']] = t['entity']

    return texts_entities
    
'''
example = "I am Alice."
entity_extraction(example)
'''