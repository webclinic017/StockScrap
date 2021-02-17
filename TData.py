import yfinance as yf
import pandas as pd
import pprint

class TData:
    '''
    The TData class uses yfinance module to extract technical price data for stocks.
    Attributes are:
        ticker : str
            Specifies which ticker to extract data from. (Required)
    '''
    def __init__(self, ticker):
        self.ticker = ticker
        pass
    

    def check_name(self):
        '''
        Checks if ticker name contains '.'. If it does, change to '-' for yfinance portability.
        Arguments are:
            None
        Returns: str
            Returns str of new ticker name for yfinance portability.
        '''

        ticker_name = self.ticker
        if '.' in ticker_name:
            ticker_name = ticker_name.replace('.', '-')
        
        else:
            pass
    
        return ticker_name   


    def get_info(self, command="nil", print=False):
        '''
        Gets stock data metric depending on command.
        Arguments are:
        command : str
            Specifies which metric to get. (Optional) Default is "nil" Available parameters are:
                "nil" - all information printed
                "averageVolume" - stock average volume
                "currency" - stock currency
                "dividendYield" - stock dividend yield
                "forwardEps" - stock forward EPS
                "forwardPE" - stock forward P/E Ratio
                "longBusinessSummary" - stock business summary
                "longName" - stock name
                "marketCap" - stock market capitalization
                "pegRatio" - stock PEG Ratio
                "previousClose" - stock previous closing price
                "priceToBook" - stock price to book ratio
                "quoteType" - type of asset
        print : bool
            Specifies whether to print data using pprint. Default is False (Optional)
        Returns: dict or int or float or str
            Returns various values depending on command
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
        Gets stock max period technical data depending on interval of each candlestick. Default is 1D candles.
        Arguments are:
            candle_interval : int
                Specifies interval of each candlestick. Default is 1 (Optional)
            print : bool
                Specifies whether to print data using pprint. Default is False (Optional)
        Returns: pandas DataFrame
            Returns pandas DataFrame of stock data. Open, High, Low, Close, Volume, Dividends, Stock Splits.
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
        Gets stock max period close price data depending on interval of each candlestick. Default is 1D candles.
        Arguments are:
            candle_interval : int
                Specifies interval of each candlestick. Default is 1 (Optional)
            print : bool
                Specifies whether to print data using pprint. Default is False (Optional)
        Returns: pandas Series
            Returns pandas Series of stock data.
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
        Gets stock max period open price data depending on interval of each candlestick. Default is 1D candles.
        Arguments are:
            candle_interval : int
                Specifies interval of each candlestick. Default is 1 (Optional)
            print : bool
                Specifies whether to print data using pprint. Default is False (Optional)
        Returns: pandas Series
            Returns pandas Series of stock data.
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
        Gets stock previous candlestick's close price data depending on interval of each candlestick. Default is 1D candles.
        Arguments are:
            candle_interval : int
                Specifies interval of each candlestick. Default is 1 (Optional)
            print : bool
                Specifies whether to print data using pprint. Default is False (Optional)
        Returns: float
            Returns price of previous candlestick's close price.
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
