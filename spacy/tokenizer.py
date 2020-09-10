import pandas as pd
import spacy

def tokenize(file_path):
    df = pd.read_csv(file_path)
    ids_ = df.iloc[:, 0]
    texts = df.iloc[:, 1]

    id_, tokenized = _tokenize('A', '舞台藝術が好きです。音楽鑑賞よりも好きです。')
    res = {}
    res[id_] = tokenized

    return res

def _tokenize(id_, text):
    nlp = spacy.load('ja_ginza')
    doc = nlp(text)

    tokenized = []
    for sent in doc.sents:
        for token in sent:
            tokenized.append(token.orth_)
            # print(token.orth_, token.tag_)
    return id_, tokenized
