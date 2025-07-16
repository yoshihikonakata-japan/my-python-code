import os
from PIL import Image

def convert_png_to_pdf(png_folder, pdf_folder):
    """
    指定されたフォルダ内のすべてのPNGファイルをPDFに変換し、
    別のフォルダに保存します。

    Args:
        png_folder (str): PNGファイルが保存されているフォルダのパス。
        pdf_folder (str): 変換されたPDFファイルを保存するフォルダのパス。
    """
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)
        print(f"PDF保存フォルダ '{pdf_folder}' を作成しました。")

    for filename in os.listdir(png_folder):
        if filename.lower().endswith('.png'):
            png_path = os.path.join(png_folder, filename)
            # 拡張子を除いたファイル名を取得
            name_without_ext = os.path.splitext(filename)[0]
            pdf_path = os.path.join(pdf_folder, f"{name_without_ext}.pdf")

            try:
                # PNGファイルを開く
                with Image.open(png_path) as img:
                    # RGBモードに変換 (一部のPNGがCMYKなどの場合に対応)
                    if img.mode == 'RGBA':
                        img = img.convert('RGB')
                    
                    # PDFとして保存
                    img.save(pdf_path)
                print(f"'{filename}' を '{os.path.basename(pdf_path)}' に変換しました。")
            except Exception as e:
                print(f"エラー: '{filename}' の変換中に問題が発生しました - {e}")

# 設定
png_directory = r'C:\pyPDF\png'
pdf_directory = r'C:\pyPDF\pdf'

# 関数を実行
if __name__ == "__main__":
    convert_png_to_pdf(png_directory, pdf_directory)