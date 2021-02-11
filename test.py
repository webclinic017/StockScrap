from DBExtract import DBExtract
from Download import Downloader

ticker_list = [
    'CRSR',
    'TTD',
    'ROKU',
    'FUBO',
    'ELYS',
    'WIMI',
    'U',
    'TSLA',
    'NIO',
    'XPEV',
    'BYND',
    'ENPH',
    'SEDG',
    'ETSY',
    'IZEA',
    'PLTR',
    'MSFT'
]

#Download
# d = Downloader()
# d.download(type_="string", ticker='MSFT', DB_PATH=r'C:\Users\Gavin\Desktop\FinData')


# data Extractor
extract = DBExtract()

# df = extract.json_extract("view", ticker="MSFT", FILE_NAME="IncomeStatement")

for ticker in ticker_list:
    df = extract.json_extract("view", ticker=ticker, FILE_NAME="IncomeStatement")
    rev = extract.select_item(df, "Sales Growth").tolist()
    print(f"{ticker} Sales Growth : {rev}")
