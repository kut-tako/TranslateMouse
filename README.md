# TranslateMouse

英単語にカーソルを合わせた状態でキーを押すと英単語の翻訳がアプリのウィンドウに表示されます。

TranslateMouseは、スクリーンショットを取り、画像内のテキストをOCR（光学式文字認識）で抽出し、翻訳するアプリケーションです。ユーザーはマウスの位置を指定して、簡単にテキストをキャプチャし、翻訳結果を得ることができます。

## 機能

- スクリーンショットを取得
- 画像内のテキストをOCRで認識
- 認識したテキストを指定した言語に翻訳
- マウスの位置をリアルタイムで追跡
- 簡単なユーザーインターフェース

## 必要条件

- Python 3.x
- 必要なライブラリ:
  - `pytesseract`
  - `Pillow`
  - `pywin32`
  - `tkinter`
  - `re`

## インストール

1. リポジトリをクローンします。

   ```bash
   git clone https://github.com/yourusername/TranslateMouse.git
   cd TranslateMouse
   ```

2. 必要なライブラリをインストールします。

   ```bash
   pip install -r requirements.txt
   ```

3. Tesseract OCRをインストールします。インストール後、Tesseractのパスを設定してください。

## 使用方法

1. アプリケーションを起動します。

   ```bash
   python -m TranslateMouse
   ```

2. ウィンドウが表示されるので、マウスを動かしてキャプチャしたいテキストの位置に移動します。

3. ショートカットキー（Shift + a）を押してスクリーンショットを取得し、OCRを実行してテキストを認識します。

4. 認識したテキストが表示され、翻訳結果が得られます。
