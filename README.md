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

#### 実行手順
1. ターミナルでserver.pyを立ち上げます
```bash
$ python server.py
```
2. 別のターミナルでclient.pyを立ち上げる
```bash
$ python client.py
```
3. `What information do you want?`の後に欲しい偽情報のジャンルを入力<br>
`person` ← 人の名前と住所<br>
`car-number` ← 車のナンバー<br>
`bank-account-number` ← 銀行口座番号<br>
`mail-address` ← メールアドレス<br>

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
**Ubuntu**
```bash
UbuntuにFakerをインストール
$ sudo apt update
$ pip install faker

ffmpegのインストール確認
$ faker -version
```

​&nbsp;