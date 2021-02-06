from Stock_Data import Stock_Data

ticker_list = [
    'GOOG',
    'AAPL',
    'NVDA',
    'AMZN',
    'NFLX'
]

for ticker in ticker_list:
    stock = Stock_Data(ticker)
    stock.download()


