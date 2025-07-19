from dotenv import load_dotenv
import os

load_dotenv()  # 預設會讀取當前目錄的 .env 檔案

print("ENV TEST:", os.getenv("MY_VAR"))
