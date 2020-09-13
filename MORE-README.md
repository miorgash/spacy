# more readme

## sudachipy コマンドラインからユーザー辞書を使う方法

```console
$ pwd
/usr/local/lib/python3.7/dist-packages/sudachipy/resources
$ sudachipy -r sudachi.json user.csv
```

## Python からユーザー辞書を使う方法

ginza から読み込まれるデフォルトの sudachi.json (\*) に以下を追記
\* /usr/local/lib/python3.7/dist-packages/sudachipy/resources/sudachi.json 

```json
{
    ...,
    "userDict" : ["任意のユーザー辞書の相対パス"]
    ...
}
```

例

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

## 技術選定の履歴

- ginza v3.3.1 は利用見送り
  - sudachipy\_tokenizer 使いたかったが最新の辞書と合わなかった
  - 以下で sudachidict を参照しており，現在の sudachidict\_core など接尾辞を伴う命名と異なるためエラーが発生．
    - "/usr/local/lib/python3.7/dist-packages/sudachipy/config.py", line 56, in create\_default\_link\_for\_sudachidict\_core

