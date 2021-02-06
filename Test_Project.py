from Instrinsic import Intrinsic
from Stock_Data import Stock_Data
import datetime

#### Get Intrinsic Value ####
ticker = 'TSLA'
stock = Stock_Data(ticker)

# Fiscal years prices
fiscal_year = stock.fiscal_year_prices()

# Income statement
inc_df = stock.income_statement()
eps = stock.select_item(inc_df, 'EPS (Diluted)')
print(eps)

# Driver end
stock.driver_end()





