from StockDL import StockDL
from datetime import datetime
import pandas as pd

class Downloader:
    '''
    The Downloader class is the stock data downloader component. It allows one to download financial data from MarketWatch or technical data from YahooFinance.
    Attributes are:
        None
    '''
    def __init__(self):
        pass
    

    def download(self,  type_, DB_PATH=None, max=None, ticker=None, list_=None, csv=None, buffer=5, download="ALL", from_=None):
        '''
        Downloads data from MarketWatch and YahooFinance.
        Arguments are:
            type_ : str
                Specifies which tickers to download. (Required) Available parameters are:
                    "string" - downloads single ticker
                    "list" - downloads list of tickers
                    "csv" - downloads list of tickers from csv
            DB_PATH : str
                Directory path to store downloaded files in. Also known as the database path. Default is None (Optional)
            max : int
                Limit number of tickers to download at once. Default is None (Optional)
            ticker : str
                Specifies which ticker to download when using type_ = "string". Default is None (Optional)
            list_ : list
                Specifies list of tickers to download when using type_ = "list". Default is None (Optional)
            csv : str
                Specifies directory of CSV file. Downloads list of tickers to download from csv when using type_ = "csv". Make sure that ticker symbols are available and under a column called "Ticker" Default is None (Optional)
            buffer : int
                Specifies buffer time in seconds in between each download. Default is 5 (Optional)
            download : str
                Specifies what data to download. Default is "ALL" (Optional) Available parameters are:
                "ALL" - download all data available
                "PRICE" - download price data
                "MAIN" - download stock information and key data
                "PROFILE" - download stock profile data
                "INCOME" - download income statement
                "BALANCE" - download balance sheet
                "CASHFLOW" - download cash flow statement
        Returns: list
            Returns list of stock that had errors downloading.
        '''
        # Start time of code
        start_time = datetime.now()

        download_list = []
        error_list = []
        dl = False

        if DB_PATH == None:
            print("Please specify a Database Path for downloads. Use DB_PATH var.")
            exit()

        # IF string
        if type_ == "string":
            stock = StockDL(ticker)
            try:
                dl = stock.stockdl(DB_PATH=DB_PATH, download=download, buffer=buffer)
                if dl == False:
                    error_list.append(ticker)
            # Error handling
            except ValueError or KeyError:
                error_list.append(ticker)
            
            if dl == True:
                download_list.append(ticker)

            if ticker in error_list:
                raise ValueError(f"{ticker} does not exist in the database. Please try another ticker.")

        # IF list
        if type_ == "list":
            components_list = list_
            dl = False

            if from_ != None:
                    index_ticker = components_list.index(from_)
                    components_list = components_list[index_ticker:]
            
            for ticker in components_list:
                stock = StockDL(ticker)
                try:
                    dl = stock.stockdl(DB_PATH=DB_PATH, download=download, buffer=buffer)
                    if dl == False:
                        error_list.append(ticker)
                # Error handling
                except ValueError or KeyError:
                    error_list.append(ticker)

                if dl == True:
                    download_list.append(ticker)

                if ticker in error_list:
                    raise ValueError(f"{ticker} does not exist in the database. Please try another ticker.")

                # index
                idx_element = components_list.index(ticker)
                max_elements = len(components_list)
                prc_complete = round(idx_element/max_elements *100, 2)

                print(f'---Download Progress: {idx_element}/{max_elements}. {prc_complete}%/100%... ')

                print(f'Download List = {download_list}')
                print(f'Error List = {error_list}')

        # IF csv
        if type_ == "csv":
            with open(csv, 'r') as csv_:
                # Read CSV
                df = pd.read_csv(csv_)
                df = df.set_index('Ticker')

                # chunks of 10 lists
                components_list = df.index.tolist()

                if from_ != None:
                    index_ticker = components_list.index(from_)
                    components_list = components_list[index_ticker:]

                # If stock does not exist, add into error_list
                for ticker in components_list:
                    # Starting time
                    start_time_csv = datetime.now()
                    stock = StockDL(ticker)
                    try:
                        dl = stock.stockdl(DB_PATH=DB_PATH, download=download, buffer=buffer)

                        if dl == False:
                            error_list.append(ticker)
                            
                    # Error handling
                    except (ValueError,KeyError):
                        error_list.append(ticker)

                    if dl == True:
                        download_list.append(ticker)

                    if ticker in error_list:
                        raise ValueError(f"{ticker} does not exist in the database. Please try another ticker.")

                    #Time
                    time_taken_csv = datetime.now() - start_time_csv    


                    # Ending time
                    print(f'---Time taken to download {ticker} = {time_taken_csv}')

                    # index
                    idx_element = components_list.index(ticker) +1
                    max_elements = len(components_list)
                    prc_complete = round(idx_element/max_elements *100, 2)

                    print(f'---Download Progress: {idx_element}/{max_elements}. {prc_complete}%/100%... ')

                    print(f'Download List = {download_list}')
                    print(f'Error List = {error_list}')


        time_taken = datetime.now() - start_time
        print(f'---Time taken = {time_taken}---')

        return error_list

if __name__ == "__main__":
    d = Downloader()
    d.download("string", r'C:\Users\Gavin\Desktop\FinData', ticker = "DISSSS", buffer=1)