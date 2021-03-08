from bs4 import BeautifulSoup as bs
import requests

class BondRate:
    '''
    The BondRate class allows you to get US 10 year bond rates (Risk Free Rate)
    Attributes are:
        None
    '''
    def __init__(self):
        pass

    def bondrate(self):
        '''
        Get current US 10 year bond rate.
        Arguments are:
            None
        Returns: float
            Returns float value of US 10 year bond rate.
        '''
        URL = "https://www.marketwatch.com/investing/bond/tmubmusd10y?countrycode=bx"

        # GET Request
        html_content = requests.get(URL).text

        # PARSE HTML
        soup = bs(html_content, "lxml")

        # Get bond rate
        rate = soup.find("h3", attrs={'class' : 'intraday__price sup--right'}).get_text().replace("%" , "").strip()

        return float(rate)


