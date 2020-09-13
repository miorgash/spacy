import pandas as pd
import spacy

def tokenize(file_path):
    try:
        df = pd.read_csv(file_path)
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='cp932')
    ids = df.iloc[:, 0]
    texts = df.iloc[:, 1]

    return {id_: _tokenize(text) for id_, text in zip(ids, texts)}

def _tokenize(text):
    nlp = spacy.load('ja_ginza')
    doc = nlp(text)

    tokenized = []
    for sent in doc.sents:
        for token in sent:
            tokenized.append([
                token.text,
                token.lemma_,
                token.pos_,
                token.tag_,
                token.dep_
            ])
    return tokenized
