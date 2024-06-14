

#### 内容
**udp-client.py:** ユーザから入力を受け取り，その入力をサーバーに送信

`person` <- 架空の人物と住所をサーバから取得.  
`car-number` <- 架空の車のナンバーをサーバから取得.  
`bank-account-number` <- 架空の銀行口座番号をサーバから取得.  
`mail-address` <- 架空のメールアドレスをサーバから取得.  

**udp-server.py:** クライアントからのメッセージを受け取り，それに対応する応答としてfakerで生成された情報をクライアントに送り返す


# Local Massaging System

#### 使用技術
<p style="display: inline">
<img src="https://img.shields.io/badge/-Linux-212121.svg?logo=linux&style=popout">
<img src="https://img.shields.io/badge/-Python-FFC107.svg?logo=python&style=popout">
<img src="https://img.shields.io/badge/-Faker-007ec6.svg?logo=python&style=popout">
</p>

&nbsp;

## 概要
PythonのUDPを用いたソケット通信とfakerライブラリを使用して，クライアントサーバ間で情報をやりとりするシンプルなアプリケーションです．fakerはPythonのパッケージで，様々な種類のデータを生成することができます．クライアントからの要求に応じた偽データをサーバーで生成し，クライアントに送り返します．

&nbsp;

## 環境構築
#### 開発環境
| OS・言語・ライブラリ | バージョン |
| :------- | :------ |
| Ubuntu | 22.04.4 LTS |
| Python | 3.10.12 |
| faker | 25.8.0 |
<br>

#### Fakerのインストール手順
- **Ubuntu**
```bash
UbuntuにFakerをインストール
$ sudo apt update
$ pip install faker

ffmpegのインストール確認
$ faker -version
```

​&nbsp;