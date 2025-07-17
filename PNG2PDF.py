#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PNG→PDF 一括変換ツール

指定フォルダ内のすべてのPNGをPDFに変換し、出力フォルダに保存します。
省略時:
  PNG_DIR = C:/pyPDF/png
  PDF_DIR = C:/pyPDF/pdf
"""
import argparse
import logging
import sys
from pathlib import Path
from PIL import Image

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="指定フォルダ内のPNGをPDFに変換して出力フォルダへ保存します。",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "png_dir",
        nargs="?",
        type=Path,
        default=Path("C:/pyPDF/png"),
        metavar="PNG_DIR",
        help="変換元PNGフォルダのパス（デフォルト: C:/pyPDF/png）"
    )
    parser.add_argument(
        "pdf_dir",
        nargs="?",
        type=Path,
        default=Path("C:/pyPDF/pdf"),
        metavar="PDF_DIR",
        help="出力先PDFフォルダのパス（デフォルト: C:/pyPDF/pdf）"
    )
    return parser.parse_args()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    args = parse_args()
    png_dir: Path = args.png_dir
    pdf_dir: Path = args.pdf_dir

    if not png_dir.is_dir():
        logging.error(f"入力フォルダが見つかりません: {png_dir}")
        sys.exit(1)

    pdf_dir.mkdir(parents=True, exist_ok=True)
    png_files = sorted(png_dir.glob("*.png"))

    if not png_files:
        logging.warning("⚠ PNGファイルが見つかりませんでした。")
        sys.exit(0)

    total = len(png_files)
    for idx, png_path in enumerate(png_files, start=1):
        pdf_path = pdf_dir / f"{png_path.stem}.pdf"
        try:
            with Image.open(png_path) as img:
                img.convert("RGB").save(pdf_path)
            logging.info(f"[{idx}/{total}] ✅ {png_path.name} → {pdf_path.name}")
        except Exception as e:
            logging.error(f"[{idx}/{total}] ❌ {png_path.name}: {e}")


if __name__ == "__main__":
    main()
