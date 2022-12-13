# habituation_application
習慣化アプリケーション

## 動作方法

```bash
# docker-composeを使って，build
docker-compose up -d
# flaskのdocker実行
docker exec -it flask_demo /bin/bash
# flaskのサーバーを建てる
flask --debug run -h 0.0.0.0
# クライアントで確認する
curl http://127.0.0.1:5000/records
```

メモリ不足でpg_demoのSTATUSExited (137)になったら，下のコマンドでdockerコンテナを再開する．

```bash
docker start pg_demo
docker start flask_demo
```
