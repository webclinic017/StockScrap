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
    def __init__(self, ticker):
        '''
        Initialize TData class
        '''
        self.ticker = ticker
        pass
    

    def check_name(self):
        '''
        Check if name contains '.', change to '-'
        Returns the new name of ticker for TData class.
        # Returns str
        '''

        ticker_name = self.ticker
        if '.' in ticker_name:
            ticker_name = ticker_name.replace('.', '-')
        
        else:
            pass
    
        return ticker_name   


    # Info section of each stock
    def get_info(self, command="nil", print=False):
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
        # Rename stock for Yfinance
        ticker_name = self.check_name()

        ticker = yf.Ticker(ticker_name)
        if command == "nil":
            # if no command, prints out whole dictionary in a pprint format
            info = ticker.info
            if print == True:
                pprint.pprint(info)
        
        else:
            # else, print out value of key of dictionary
            info = ticker.info.get(f"{command}", "No such key exists. Please try again with a valid key.")
            if print == True:
                print(f"{command} : {info}")
        
        return info
  

    def get_data(self, candle_interval=1, print=False):
        '''
        Downloads market data from Yahoo Finance
        returns pandas DataFrame
        '''
        # Rename stock for Yfinance
        ticker_name = self.check_name()
       
        ticker = yf.Ticker(ticker_name)
        hist = ticker.history(period=f"max",interval=f"{candle_interval}d")
        if print == True:
            pprint.pprint(hist)
        return hist


    def get_close(self, candle_interval=1, print=False):
        '''
        Get Close market data from Yahoo Finance
        returns pandas Series
        '''
        # Rename stock for Yfinance
        ticker_name = self.check_name()

        # Get close data for stock
        ticker = yf.Ticker(f"{ticker_name}")
        close = ticker.history(period=f"max",interval=f"{candle_interval}d")['Close']
        if print == True:
            pprint.pprint(close)
        return close


    def get_open(self, candle_interval=1, print=False):
        '''
        Get Open market data from Yahoo Finance
        returns pandas Series
        '''
        # Rename stock for Yfinance
        ticker_name = self.check_name()
        
        # Get close data for stock
        ticker = yf.Ticker(f"{ticker_name}")
        open = ticker.history(period=f"max",interval=f"{candle_interval}d")['Open']
        if print == True:
            pprint.pprint(open)
        return open


    def get_prevclose(self, candle_interval=1, print=False):
        '''
        Get Yesterday's close value for stock
        returns float
        '''
        # Rename stock for Yfinance
        ticker_name = self.check_name()

        # Get Previous close value for stock
        ticker = yf.Ticker(f"{ticker_name}")
        prev_close = ticker.history(period=f"max",interval=f"{candle_interval}d")['Close']
        val = float(round(prev_close.iloc[-1],2))
        if print == True:
            pprint.pprint(val)
        return val
