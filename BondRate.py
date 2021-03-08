from bs4 import BeautifulSoup as bs
import requests

class BondRate:
    def __init__(self):
        pass

    def bondrate(self):
        # URL to get bond Rate
        URL = "https://www.marketwatch.com/investing/bond/tmubmusd10y?countrycode=bx"

        # GET Request
        html_content = requests.get(URL).text

        # PARSE HTML
        soup = bs(html_content, "lxml")

        # Get bond rate
        rate = soup.find("h3", attrs={'class' : 'intraday__price sup--right'}).get_text().replace("%" , "").strip()

        return float(rate)


