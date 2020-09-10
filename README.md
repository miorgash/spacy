# 使い方（ユーザー向け）

ブラウザまたは API で利用する．

## ブラウザから

1. `http://${ip}:5108` にアクセス
2. テキストを入力

## Python から

```python
import request
...
```


# メンテナンス（管理者向け）
## 起動

```bash
nohup sudo docker &
```

## 辞書更新

他の人の解析結果にも影響するため注意

- 



---

# Overview

- RUN

```console
sudo docker run --rm --name spacy \
    -v nlp-data:/nlp-data \
    -v ${PWD}/resources/sudachi.json:/usr/local/lib/python3.7/dist-packages/sudachipy/resources/sudachi.json \
    -v ${PWD}/resources/user.csv:/usr/local/lib/python3.7/dist-packages/sudachipy/resources/user.csv \
    -v ${PWD}/resources/user.dic:/usr/local/lib/python3.7/dist-packages/sudachipy/resources/user.dic \
    -p 5108:5108 dig/spacy:latest
```

- Build user dict

```console
cd /usr/local/lib/python3.7/dist-packages/sudachipy/resources
sudachipy ubuild -s ../../sudachidict_core/resources/system.dic user.csv
```

[Sudachi/user\_dict.md](https://github.com/WorksApplications/Sudachi/blob/develop/docs/user_dict.md)参照

# Point

- ユーザー辞書は永続化し，コンテナ生成の都度マウントする
- spacy から利用される辞書はコンテナ生成の都度 sudachi.json に以下の通り追記し指定する

```json
{
    ...,
    "userDict" : ["user.dic"]
    ...
}
```


# sudachipy コマンドラインからユーザー辞書を使う方法
```console
$ pwd
/usr/local/lib/python3.7/dist-packages/sudachipy/resources
$ sudachipy -r sudachi.json user.csv
```

# Python からユーザー辞書を使う方法
ginza から読み込まれるデフォルトの sudachi.json (\*) に以下を追記
```json
{
    ...,
    "userDict" : ["任意のユーザー辞書の相対パス"]
    ...
}
```
\* /usr/local/lib/python3.7/dist-packages/sudachipy/resources/sudachi.json 

```python
import spacy
nlp = spacy.load('ja_ginza')
doc = nlp('小林製薬')
for sent in doc.sents:
    for token in sent:
        print(token.orth_, token.tag_)
# 舞台藝術 名詞-普通名詞-一般
# に 助詞-格助詞
# 興味 名詞-普通名詞-一般
# が 助詞-格助詞
# あり 動詞-非自立可能
# ます 助動詞
# 。 補助記号-句点
# 芸術大学 名詞-固有名詞-一般
# に 助詞-格助詞
# 通っ 動詞-一般
# て 助詞-接続助詞
# おり 動詞-非自立可能
# まし 助動詞
# た 助動詞
# の 助詞-準体助詞
# で 助動詞
# 。 補助記号-句点
```

# Knowledge

- ginza v3.3.1 は利用見送り
  - sudachipy\_tokenizer 使いたかったが最新の辞書と合わなかった
  - 以下で sudachidict を参照しており，現在の sudachidict\_core など接尾辞を伴う命名と異なるためエラーが発生．
    - "/usr/local/lib/python3.7/dist-packages/sudachipy/config.py", line 56, in create\_default\_link\_for\_sudachidict\_core

