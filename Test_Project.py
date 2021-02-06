from Instrinsic import Intrinsic
from Stock_Data import Stock_Data
import pandas as pd
import datetime


#### Database > ABC > TICKER > JSONs
#### Store Data INTO JSON #### 
# ticker = 'MSFT'
# stock = Stock_Data(ticker)

# # Fiscal years prices
# fiscal_year = stock.fiscal_year_prices()

# # Income statement
# inc_df = stock.income_statement()
# eps = stock.select_item(inc_df, 'EPS (Diluted)')
# print(eps)

# # Driver end
# stock.driver_end()

#############################

list_tickers = ['AAPL', 'MSFT', 'GOOG', 'NVDA']
for ticker in list_tickers:
    stock = Stock_Data(ticker)
    # Export data
    stock.export()
