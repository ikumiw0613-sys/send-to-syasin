# 画像アップロード API

FastAPIを使ったシンプルな画像アップロードアプリです。ブラウザから画像を選択し、サーバーへ保存できます。

## 必要な環境

- Python 3.13
- PowerShell

## セットアップ

プロジェクトのルートディレクトリで、仮想環境を有効化します。

```powershell
.\.venv\Scripts\Activate.ps1
```

必要なパッケージをインストールします。

```powershell
python -m pip install -r requirements.txt
```

## 起動方法

```powershell
uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload
```

起動後、ブラウザで以下のURLを開きます。

- アップロード画面: <http://127.0.0.1:8000>
- APIドキュメント: <http://127.0.0.1:8000/docs>

終了するには、起動したターミナルで `Ctrl+C` を押します。

## API

### `GET /`

画像アップロード画面を表示します。

### `POST /upload`

フォームから送信された画像を保存します。アップロードするファイルのフィールド名は `file` です。

成功時のレスポンス例:

```json
{
  "message": "uploaded",
  "filename": "image.jpg"
}
```

## ファイルの保存先

アップロードされたファイルは `src/uploads/` に保存されます。同名のファイルがある場合は上書きされます。

## プロジェクト構成

```text
.
├── README.md
├── requirements.txt
└── src/
    ├── app.py
    ├── index.html
    └── uploads/
```

## 主な依存パッケージ

- `fastapi`: APIフレームワーク
- `uvicorn`: ASGIサーバー
- `python-multipart`: ファイルアップロードのフォーム解析
