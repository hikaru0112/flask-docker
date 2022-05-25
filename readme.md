# flask_template
Flaskの環境をDockerで簡単構築できるアプリケーションです。

## デフォルトのイメージ名

アプリケーションイメージ： app
データベースイメージ： DB

### DockerImage
* mysql:8.0-oracle
* Python:3

Flaskなどについてはpipに依存するため不定

## 実行方法


```bash
docker-compose up --build
```
をターミナルで実行することでwebサーバーとDBサーバーが自動的に立ち上がります。

[localhost:5001](localhost:5001)が接続先URLです。（環境によって適度にポートなどを変更してください。)

## 実行フォルダの指定について

`.env`ファイル内の`FLASK_APP`環境変数で指定してください。

## DBについて

DB(イメージ名)のcliにて
```bash
mysql -u admin -p
#パスワード
pass
```
でcliを使用することができます。

ビルド時に自動で`./initdb.d/init.sql`が読み込まれ自動でテーブルが生成されます。

テーブルを使用したい場合は適度に変更してください。

## .envについて
gitのパブリックリポジトリなどに上げる際は.gitignoreに追加してください

### 各変数の説明

`MYSQL_USER=` mysqlが自動で生成してくれるユーザー

`MYSQL_DATABASE`mysqlが自動で生成してくれるデータベース

`MYSQL_PASSWORD` mysqlが自動で生成してくれるユーザーのパスワード

`MYSQL_ROOT_PASSWORD` mysqlのrootのパスワード

`DATABASE_HOST`DBのホスト名（イメージ名に依存します)

`FLASK_APP` Flaskで使用するファイルの指定

`FLASK_ENV` flaskへの引数
