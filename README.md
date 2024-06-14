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