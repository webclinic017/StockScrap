from DBExtract import DBExtract
from StockDL import StockDL
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
d = Downloader()
d.download(type_="csv", csv=r'C:\Users\Dennis Loo.000\Desktop\Value_Investing_Screener\Ticker_List\S&P500 Components.csv', DB_PATH=r'C:\Users\Dennis Loo.000\Desktop\FinData', buffer=20, from_="AEE")
# d.download(type_="string", ticker=r'GOOG', DB_PATH=r'C:\Users\Dennis Loo.000\Desktop\FinData', buffer=1)


# # data Extractor
# extract = DBExtract(DB_PATH=r'C:\Users\Dennis Loo.000\Desktop\FinData')

# for ticker in ticker_list:
#     df = extract.json_extract("view", ticker=ticker, FILE_NAME="IncomeStatement")
#     rev = extract.select_item(df, "Sales Growth").tolist()
#     print(f"{ticker} Sales Growth : {rev}")
