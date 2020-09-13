# 使い方（ユーザー向け）

ブラウザまたは API から利用

## ブラウザから

`http://${ip}:5108` にアクセス

## Python から

```python
import request
# coming soon
```


# メンテナンス（管理者向け）
## 起動

ユーザー辞書は永続化し，コンテナ生成の都度マウントする

```console
SUDACHI_HOME=/usr/local/lib/python3.7/dist-packages/sudachipy
nohup sudo docker run --rm --name spacy \
    -v nlp-data:/nlp-data \
    -v ${PWD}/resources/sudachi.json:${SUDACHI_HOME}/resources/sudachi.json \
    -v ${PWD}/resources/user.csv:${SUDACHI_HOME}/resources/user.csv \
    -v ${PWD}/resources/user.dic:${SUDACHI_HOME}/resources/user.dic \
    -p 5108:5108 dig/spacy:latest &
```

## 辞書更新

他の人の解析結果にも影響するため注意  
詳細は [Sudachi/user\_dict.md](https://github.com/WorksApplications/Sudachi/blob/develop/docs/user_dict.md) 参照

```console
cd /usr/local/lib/python3.7/dist-packages/sudachipy/resources
sudachipy ubuild -s ../../sudachidict_core/resources/system.dic user.csv
```
