# Import BS4 Classes
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


# URL to check for valuations table.
URL = f'https://www.marketwatch.com/investing/stock/AAPL/company-profile?mod=mw_quote_tab'


# GET REQUEST
html_content = requests.get(URL).text

# PARSE
soup = bs(html_content, "lxml")

val_selc = soup.find_all("ul", attrs={'class': 'list list--kv list--col50'})

for item in val_selc:
    item_selc = item.find_all("li")[2]
    val = item_selc.find("span").get_text()

print(val)


    





