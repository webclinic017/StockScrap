import yfinance as yf
import pandas as pd
import pprint


# Initialize TData class.
class TData:
    '''
    Technical Stock Data Scrapper using yfinance and talib module.
    Uses data from Yahoo Finance
    Returns pandas Series of prices, information of stock.

    args = period_years(int), candle_interval(int), print(boolean)
    '''
    def __init__(self, candle_interval=1, print=False):
        '''
        Initialize TData class
        '''
        self.candle_interval = candle_interval
        self.print = print

    # Info section of each stock
    def get_info(self, ticker, command="nil"):
        '''
        Get Information of stock in dictionary format
        ### Important commands to get crucial information of stock: ####
            averageVolume : Get Average Volume of Stock
            currency : Get Currency of Stock
            dividendYield : Get Dividend Yield of Stock
            forwardEps : Get Forward Earnings per Share of Stock
            forwardPE : Get Forward P/E Ratio of Stock
            industry : Get Industry of Stock
            longBusinessSummary : Get Business Summary of Stock
            longName : Get Name of Stock
            marketCap : Get Market Capitalization of Stock
            pegRatio : Get Price to Earnings Growth Ratio of Stock
            previousClose : Get Previous Close of Stock
            priceToBook : Get Price to Book Ratio of Stock
            quoteType : Get Type of Asset 
            '''

        ticker = yf.Ticker(ticker)
        if command == "nil":
            # if no command, prints out whole dictionary in a pprint format
            info = ticker.info
            if self.print == True:
                pprint.pprint(info)
        
        else:
            # else, print out value of key of dictionary
            info = ticker.info.get(f"{command}", "No such key exists. Please try again with a valid key.")
            if self.print == True:
                print(f"{command} : {info}")
        
        return info
  

    def get_data(self, ticker):
        '''
        Downloads market data from Yahoo Finance
        returns pandas DataFrame
        '''
       
        ticker = yf.Ticker(ticker)
        hist = ticker.history(period=f"max",interval=f"{self.candle_interval}d")
        if self.print == True:
            pprint.pprint(hist)
        return hist

    def get_close(self, ticker):
        '''
        Get Close market data from Yahoo Finance
        returns pandas Series
        '''
        # Get close data for stock
        ticker = yf.Ticker(f"{ticker}")
        close = ticker.history(period=f"max",interval=f"{self.candle_interval}d")['Close']
        if self.print == True:
            pprint.pprint(close)
        return close


    def get_open(self, ticker):
        '''
        Get Open market data from Yahoo Finance
        returns pandas Series
        '''
        # Get close data for stock
        ticker = yf.Ticker(f"{ticker}")
        open = ticker.history(period=f"max",interval=f"{self.candle_interval}d")['Open']
        if self.print == True:
            pprint.pprint(open)
        return open

    def get_prevclose(self, ticker):
        '''
        Get Yesterday's close value for stock
        returns float
        '''

        # Get Previous close value for stock
        ticker = yf.Ticker(f"{ticker}")
        prev_close = ticker.history(period=f"max",interval=f"{self.candle_interval}d")['Close']
        val = float(round(prev_close.iloc[-1],2))
        if self.print == True:
            pprint.pprint(val)
        return val
