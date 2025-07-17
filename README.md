# PNG2PDF

PNG→PDF 一括変換ツール

## 説明

`PNG2PDF.py` は、指定フォルダ内のPNG画像をすべてPDF形式に変換し、出力フォルダへ保存するPythonスクリプトです。引数を省略すると、以下のフォルダをデフォルトで使用します。 fileciteturn1file0

- 変換元PNGフォルダ：`C:/pyPDF/png`
- 出力先PDFフォルダ：`C:/pyPDF/pdf`

## 特長

- **一括変換**：フォルダ内の全PNGファイルをまとめて処理
- **フォルダ自動生成**：出力先フォルダが存在しない場合、自動で作成
- **ログ出力**：処理状況を `INFO`/`WARNING`/`ERROR` レベルで標準出力に表示
- **使い慣れたAPI**：`argparse` で簡単にオプション設定可能

## 必要要件

- Python 3.7 以上
- Pillow（画像操作用）

```bash
pip install Pillow
```

## 使い方

```bash
python PNG2PDF.py [PNG_DIR] [PDF_DIR]
```

### 引数

| 引数        | 内容                      | デフォルト          |
| --------- | ----------------------- | -------------- |
| `PNG_DIR` | 変換対象のPNGファイルが置かれたフォルダパス | `C:/pyPDF/png` |
| `PDF_DIR` | 変換後のPDFファイルを保存するフォルダパス  | `C:/pyPDF/pdf` |

### 実行例

1. デフォルトフォルダで変換

   ```bash
   python PNG2PDF.py
   ```

2. カスタムフォルダを指定して変換

   ```bash
   python PNG2PDF.py ./images ./output_pdfs
   ```

## ロギング内容

- 入力フォルダが見つからない場合：`ERROR` と共に終了
- PNGファイル未検出時：`WARNING` を出力し終了
- 各ファイル変換成功：`INFO` レベルで `[idx/total] ✅ ファイル名 → ファイル名` を出力
- 変換失敗時：`ERROR` レベルでエラーメッセージを出力

## ライセンス

MITライセンスのもとで公開しています。

