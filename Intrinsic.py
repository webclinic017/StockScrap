from DBExtract import DBExtract
from Download import Downloader
import pandas as pd
import numpy as np
import statistics as stat

ticker = "AAPL"
DB_PATH = r'C:\Users\Dennis Loo.000\Desktop\FinData'

d = Downloader()
d.download(type_="string", DB_PATH = DB_PATH, buffer=1, ticker = ticker)

# Extract FCF from database

e = DBExtract(DB_PATH)
inc_df = e.json_extract("data", ticker=ticker, FILE_NAME="CashFlow_Financing")
free_cashflow = e.select_item(inc_df, "Free Cash Flow").tolist()

# Find average growth rate for the past x number of years.
prc_list = []
for i in range(0,len(free_cashflow)-1):
    # Find differencem, then prc change
    diff = free_cashflow[i+1] - free_cashflow[i]
    prc_change = round(diff/free_cashflow[i],2)
    prc_list.append(prc_change)

# Growth rate assuming past 5 years FCF growth.
avg_cf = stat.mean(prc_list)

# Get 5 years expected FCF
estimation_years = 5
recent_fcf = free_cashflow[-1]
for i in range(0, estimation_years):
    recent_fcf = recent_fcf * (1+avg_cf)
    print(recent_fcf)

# Get PEG, growth rate
peg = e.json_extract("view", ticker=ticker, FILE_NAME="Profile_Valuations")
print(peg)


