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

ユーザー辞書・アップロードされるデータを `nlp-data` コンテナで永続化する  
`nlp-data` を削除しても VOLUME は残るが `--volumes-from` でマウントすることができなくなるため注意

```console
sudo docker run --name nlp-data dig/nlp-data:latest
sudo docker run --rm --name spacy-test --volumes-from nlp-data -p 5108:5108 dig/spacy:latest
```

Docker Volume についてのメモ

- ビルド時に Dockerfile にて VOLUME コマンドを実行した場合，ビルドされるイメージに VOLUME はついてくるか？；ビルドを実施したホスト以外で，--volume-from コマンドで当該ボリュームをマウントすることは可能か？
    - 問いの立て方が間違っている；VOLUME はコンテナ起動時に作成される．

これからやること

- `dig/nlp-data` コンテナ作成
    - `sudachipy/resources` と `/nlp-data` を `VOLUME` コマンドで指定するだけのコンテナ
- `dig/spacy` Dockerfile 修正
    - `sudachipy/resources` を必要であれば削除（VOLUME vs コンテナ上のファイルだったら前者がおそらく勝つので，おそらく不要）
    - VOLUME vs コンテナ上のファイルだと前者の内容で後者が上書きされることを確認した．

## 辞書更新

他の人の解析結果にも影響するため注意  
詳細は [Sudachi/user\_dict.md](https://github.com/WorksApplications/Sudachi/blob/develop/docs/user_dict.md) 参照

```console
cd /usr/local/lib/python3.7/dist-packages/sudachipy/resources
sudachipy ubuild -s ../../sudachidict_core/resources/system.dic user.csv
```
