from Fin_Data import Fin_Data
from Fin_Extract import Fin_Extract

class FData(Fin_Data, Fin_Extract):
    '''
    # Financial Data Scrapper Made by Gavin Loo 2021.
    Uses data from MarketWatch.com

    Args = ticker, PATH
    
    How it works:
        Initialize FData Class using ticker and PATH for GoogleChromeDriver
        ----------
        Able to get pandas DataFrames of Key Data, Income Statement, Balance Sheet and Cash Flow Statements
        ----------
        You are able to get:
        ----------
        Key Data: 
            Get Current Price, Open Price, Day Range, 52 Week Range, Market Cap, Shares Outstanding, Public Float, BEta, Rev Per Employee, P/E Ratio, EPS, Yield, Dividend, Ex-Dividend Rate, Short Interest, % of Float Shorted, Average Volume
        ----------
        Profile:
            Industry, Sector
        ----------
        Financials:
            Income Statement:
            Balance Sheet:
                Assets, Liabilities & Shareholders' Equity
            Cash Flow:
                Operating Activities, Investing Activities, Financing Activities
        ----------

    '''

    # Initializes FData class inherits __init__ args
    def __init__(self, ticker, PATH = 'C:\Program Files (x86)\chromedriver.exe'):
        Fin_Data.__init__(self, ticker, PATH = 'C:\Program Files (x86)\chromedriver.exe')
        Fin_Extract.__init__(self,ticker, PATH = 'C:\Program Files (x86)\chromedriver.exe')
    

### Example ### 
stock = FData('MSFT')
df = stock.income_statement()
rev = stock.select_item(df, item='Sales/Revenue')
prc = stock.select_item(df, item='Sales Growth')
array = stock.cell_true_val(rev)
array2 = stock.cell_true_val(prc)

print(array)
print(array2)
stock.driver_end()



