# はじめに

普段、英語でゲームしてる時に知らない英単語がでてきたらウィンドウを切り替えて意味を調べてるのですがめんどくさくなって来たのでマウスオーバーしたら単語の意味を表示してくれるアプリを作成します。
このドキュメントはマウスオーバー翻訳のプロトタイプを作る時のメモです。

- 使用技術
- Windows10
- Docker
- Python
- pyocr
- VsCode

## 開発環境作成

早速、と行きたいところですが大学時代からずっとローカルPCに開発環境を構築していて環境の管理ができていません。  
この状態でこれから開発をしていくのは大変手間なため、仮想環境に開発環境を構築するところから始めようと思います。  
VSCodeにDevContainerというDockerをVSCode内で使える機能があるらしいのでそれを活用します。  
以下のqiitaの記事を参考にして進めていきます。  
> <https://qiita.com/Sicut_study/items/4f301d000ecee98e78c9>  
> <https://qiita.com/S4nTo/items/977d28b0eac316915702>
>
> <https://www.wantedly.com/companies/sas-com/post_articles/939491>  
> <https://learn.microsoft.com/ja-jp/training/modules/use-docker-container-dev-env-vs-code/1-introduction>

### 1.Docker Desktopのインストール

Docker DesktopにはWSL2が必要なので先にWindows Insider Programに入りました。  
その後、Docker Desktopインストーラーを起動して最後まで進めてDocker Desktopのインストール完了です。

VSCodeの拡張機能のほうが簡単っぽいからそっちでやる。

### 2.VSCodeの拡張機能インストール

DockerとDev Containersを入れる。

### 3.チュートリアルの手順通りに進める

> <https://learn.microsoft.com/ja-jp/training/modules/use-docker-container-dev-env-vs-code/1-introduction>

## プロトタイプ開発開始

### 1.