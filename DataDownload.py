from Stock_Data import Stock_Data
import pandas as pd
from datetime import datetime
import pprint

# Imports selenium errors and exceptions.
from selenium.common.exceptions import *

# Start time of code
start_time = datetime.now()

# Split list into multiple lists
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


# List of S&P500 Companies
components = r'C:\Users\Dennis Loo.000\Desktop\Value_Investing_Screener\Ticker_List\S&P500 Components.csv'

error_list = []

with open(components, 'r') as sp500:

    # Read CSV
    df = pd.read_csv(sp500)
    df = df.set_index('Ticker')

    # chunks of 10 lists
    components_list = df.index.tolist()
    components_chunks = list(chunks(components_list, 49))
    components_len = len(components_chunks) # Len = 51
    # Now at components_chunks[2], SCHW

    # If stock does not exist, add into error_list
    for ticker in components_chunks[0]:
        stock = Stock_Data(ticker)
        try:
            download_bool = stock.download()
            if download_bool == False:
                error_list.append(ticker)
        # Error handling
        except ValueError or KeyError:
            error_list.append(ticker)

#### DEBUG #####
# stock = Stock_Data('AAPL')
# print(stock.income_statement())

time_taken = datetime.now() - start_time
print(f'Error List = {error_list}')
print(f'---Time taken = {time_taken}---')