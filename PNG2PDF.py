#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PNG→PDFバッチ変換ツール
"""

import logging
from pathlib import Path
from PIL import Image
import click

# ログ設定
logging.basicConfig(level=logging.INFO, format="%(message)s")

@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.argument("png_dir", type=click.Path(exists=True, file_okay=False, path_type=Path))
@click.argument("pdf_dir", type=click.Path(file_okay=False, path_type=Path))
def main(png_dir: Path, pdf_dir: Path):
    """
    指定フォルダ内の全PNGをPDFに変換し、出力フォルダへ保存します。

    \b
    Arguments:
      PNG_DIR  変換元PNGフォルダのパス
      PDF_DIR  出力先PDFフォルダのパス
    """
    pdf_dir.mkdir(parents=True, exist_ok=True)
    png_files = list(png_dir.glob("*.png"))
    if not png_files:
        logging.warning("⚠ PNGファイルが見つかりませんでした。")
        return

    with click.progressbar(png_files, label="Converting") as bar:
        for png_path in bar:
            pdf_path = pdf_dir / f"{png_path.stem}.pdf"
            try:
                with Image.open(png_path) as img:
                    # モードに関係なく RGB 変換してから保存
                    img.convert("RGB").save(pdf_path)
                logging.info(f"✅ {png_path.name} → {pdf_path.name}")
            except Exception as e:
                logging.error(f"❌ {png_path.name}: {e}")

if __name__ == "__main__":
    main()
