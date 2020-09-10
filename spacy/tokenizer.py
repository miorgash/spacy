import pandas as pd
import spacy

def tokenize(file_path):
    df = pd.read_csv(file_path)
    ids = df.iloc[:, 0]
    texts = df.iloc[:, 1]

    res = {id_: _tokenize(text) for id_, text in zip(ids, texts)}

    return res

def _tokenize(text):
    nlp = spacy.load('ja_ginza')
    doc = nlp(text)

    tokenized = []
    for sent in doc.sents:
        for token in sent:
            tokenized.append(token.orth_)
            # print(token.orth_, token.tag_)
    return tokenized
