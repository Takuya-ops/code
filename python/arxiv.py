import requests
import os
from datetime import datetime

# arXivのAPIエンドポイントと検索キーワード
API_ENDPOINT = "http://export.arxiv.org/api/query?search_query="
KEYWORD = "Machine Learning"
# ダウンロードするファイルの保存先ディレクトリ
SAVE_DIR = "~/desktop/paper"


def download_pdf(url, save_path):
    response = requests.get(url)
    with open(save_path, "wb") as file:
        file.write(response.content)


def main():
    # arXiv APIから論文情報を取得
    response = requests.get(API_ENDPOINT + KEYWORD)
    # 結果を解析してPDFのURLを見つける（ここでは簡単のため最初の論文のみ）
    # 実際にはXML解析などが必要になります
    paper_id = response.text.split('id="')[1].split('"')[0]
    pdf_url = f"http://arxiv.org/pdf/{paper_id}.pdf"

    # 現在の日付をファイル名に使用
    current_date = datetime.now().strftime("%Y-%m-%d")
    save_path = os.path.join(SAVE_DIR, f"{paper_id}_{current_date}.pdf")

    # PDFをダウンロードして保存
    download_pdf(pdf_url, save_path)
    print(f"Downloaded: {save_path}")


if __name__ == "__main__":
    main()
