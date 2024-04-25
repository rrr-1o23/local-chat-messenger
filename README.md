### local-chat-messenger

pythonのUDPを用いたソケット通信とfakerパッケージを使用して，クライアントサーバ間で情報をやりとりするシンプルなアプリケーション．

### 内容
udp-client.py: ユーザから入力を受け取り，その入力をサーバーに送信
```bash
person <- 架空の人物と住所をサーバから取得．
car-number <- 架空の車のナンバーをサーバから取得．
bank-account-number <- 架空の銀行口座番号をサーバから取得．
mail-address <- 架空のメールアドレスをサーバから取得
```
udp-server.py: クライアントからのメッセージを受け取り，それに対応する応答としてfakerで生成された情報をクライアントに送り返す

