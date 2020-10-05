# Tokenizer

このリポジトリでは以下が可能な環境を提供する

- 各種形態素解析ライブラリ用辞書の利用更新
  - 永続化してある辞書をマウントして利用・更新する
- WEB ブラウザを介した形態素解析処理の実行（フォーマットは独自仕様で固定）

想定するユーザー像と開発方針

- 辞書利用
  - 玄人向け
- WEB ブラウザからの利用者
  - テキストの分析に携わる人全般を想定し開発する．
    - 各種 Python ライブラリの仕様を知らないと利用できないような仕様は避ける．
    - 実務で利用する可能性が低い機能の実装は積極的には行わない．
    - 当サービスの独自仕様を知らないと利用できないような仕様は避け，出来る限り各ライブラリの仕様に準拠した利用が可能になるよう実装する．

# 使い方（ユーザー向け）

- ブラウザから

    `http://${ip}:5108` にアクセス

- Python から

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
nohup sudo docker run --rm --name tokenizer \
    -v tokenizer:/data/tokenizer \
    -v sudachipy-resources:/usr/local/lib/python3.7/dist-packages/sudachipy/resources \
    -p 5108:5108 dig/tokenizer:latest &
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
