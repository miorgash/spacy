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

```console
sudo docker-compose up -d
```

```console
nohup sudo docker run --rm --name spacy \
    -v nlp-data:/nlp-data \
    -v sudachipy-resources:/usr/local/lib/python3.7/dist-packages/sudachipy/resources \
    -p 5108:5108 dig/spacy:latest &
```

メモ： volume を コンテナのコンテンツにマウントした場合，以下の優先度でコンテンツが残る

```
VOLUME（中身あり） > コンテナのコンテンツ > VOLUME（中身無し）
ホストのコンテンツ > 
```

## 辞書更新

他の人の解析結果にも影響するため注意  
詳細は [Sudachi/user\_dict.md](https://github.com/WorksApplications/Sudachi/blob/develop/docs/user_dict.md) 参照

```console
cd /usr/local/lib/python3.7/dist-packages/sudachipy/resources
sudachipy ubuild -s ../../sudachidict_core/resources/system.dic user.csv
```
