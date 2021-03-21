# Import BS4 Classes
from bs4 import BeautifulSoup as bs
import requests

# Import time for sleep functions
import time

# Import datetime for datetime functions and pandas market calendars for stock market holidays
from datetime import datetime, timedelta
import pandas_market_calendars as mcal

# Import pandas and numpy
import pandas as pd
import numpy as np


class Fin_Data:
    '''
    The Fin_Data class allows for scraping of financial data from MarketWatch. It then returns it in a pandas DataFrame or Series format.
    Attributes are:
        ticker : str
            Specifies which ticker to draw financial data from. (Required)
    '''
    
    def __init__(self, ticker):
        self.ticker = ticker

    def __repr__(self):
        return (f'{self.__class__.__name__}('f'{self.ticker!r}')


    def __str__(self):
        return f'Financial Data for {self.ticker}'


    def reorder_df(self, from_df, reverse=False):
        '''
        Reorders pandas DataFrame columns in descending order.
        Arguments are:
            from_df : pandas DataFrame
                Specifies what DataFrame to get list of columns from. (Required)
            reverse : boolean
                Specifies whether to reorder in descending. False = descending. Default is False (Optional)
        Returns: pandas DataFrame
            Returns reordered pandas DataFrame
        '''
        df = from_df.reindex(columns=sorted(from_df.columns, reverse=reverse))
        return df


    def name(self):
        '''
        Get stock's name.
        Arguments are:
            None
        Returns: str
            Returns stock name in string value.
        ''' 

        # URL to check for stock name.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}?mod=mw_quote_tab'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        val = soup.find("h1", attrs={'class': 'company__name'}).get_text()

        return val


    def industry(self):
        '''
        Get stock's industry.
        Arguments are:
            None
        Returns: str
            Returns stock's industry in string value.

        '''

        # URL to check for stock name.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        val_selc = soup.find_all("ul", attrs={'class': 'list list--kv list--col50'})

        for item in val_selc:
            item_selc = item.find_all("li")[0]
            val = item_selc.find("span").get_text()
        
        return val


    def sector(self):
        '''
        Get stock's sector.
        Arguments are:
            None
        Returns: str
            Returns stock's sector in string value.
        '''

        # URL to check for stock name.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        val_selc = soup.find_all("ul", attrs={'class': 'list list--kv list--col50'})

        val =0
        try:
            for item in val_selc:
                item_selc = item.find_all("li")[1]
                val = item_selc.find("span").get_text()
        
        except UnboundLocalError:
            raise ValueError("Unable to get ticker.")
            
        return val


    def exchange(self):
        '''
        Get stock's exchange location.
        Arguments are:
            None
        Returns: str
            Returns stock's exchange location in string value.
        '''

        # URL to check for stock name.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        val_selc = soup.find_all("span", attrs={'class': 'company__market'})[0]
        val = val_selc.get_text()

        # Format Exchange
        val = val.replace(":", "")
        val = val.split(" ")[0]
        
        return val


    def ceo(self):
        '''
        Get stock's CEO name.
        Arguments are:
            None
        Returns: str
            Returns stock's CEO name in string value.
        '''

        # URL to check for stock name.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        group = soup.find_all("div", attrs={'class': 'group right'})[0]
        val = group.div.ul.li.find("a").get_text()

        return val


    def business_model(self):
        '''
        Get stock's business_model overview.
        Arguments are:
            None
        Returns: str
            Returns stock's business_model overview in string value.
        '''
        # URL to check for stock name.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        val = soup.find_all("p", attrs={'class': 'description__text'})[0].get_text()

        return val

    
    def stock_info(self):
        '''
        Get stock's information overview. Includes name, sector, industry, exchange, ceo and business model.
        Arguments are:
            None
        Returns: pandas DataFrame
            Returns stock's main information in pandas DataFrame format.
        '''

        # Name, Sector, Industry, 
        name = self.name()
        sector = self.sector()
        industry = self.industry()
        exchange = self.exchange()
        ceo = self.ceo()
        business_model = self.business_model()

        index = ['Name', 'Sector', 'Industry', 'Exchange', 'CEO', 'Business Model']
        val = [name, sector, industry, exchange, ceo, business_model]

        # Create pandas Series using index list and val list.
        stock_s = pd.Series(val, index, dtype='string', name=f'{self.ticker} Information')

        return stock_s


    def price(self):
        '''
        Get stock's current price.
        Arguments are:
            None
        Returns: float
            Returns stock's price in float value.
        '''
        # URL to check for stock price.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}?mod=mw_quote_tab'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        val = soup.find_all("bg-quote", attrs={'value'})[0].get_text()

        # Remove commas
        val = val.replace(",","")
        # Get Price of Stock in float
        price = float(val)
        
        return price
    

    def check_ticker(self):
        '''
        Uses stock price and sector to check whether the ticker exists in MarketWatch database.
        Arguments are:
            None
        Returns: bool
            Returns True or False depending on whether the stock exists. Returns True for exist.
        '''
    
        exist = True

        while exist == True:
            # try to get price, sector
            try: 
                sec = self.sector()
            except IndexError:
                exist=False
                break
            
            try:
                price = self.price()

            except IndexError:
                exist=False
                break
        
            if sec == 0:
                exist = False
                break

            if float(price) == 0:
                exist = False
                break
                
            break
        
        # Returns True or False depending whether self.ticker exists in database.
        return exist

    
    def valuations(self):
        '''
        Get table of valuation metrics under MarketWatch Profile page.
        Arguments are:
            None
        Returns: pandas Series
            Returns pandas Series of valuation metrics.
        '''

        # URL to check for valuations table.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        table = soup.find_all('table', attrs={'class':'table value-pairs no-heading'})[0]
        table_selc = table.tbody.find_all("tr")

        headers = []
        for tr in table_selc:
            header_selc = tr.find_all("td")[0]
            for val in header_selc:
                headers.append(val)

        values = []
        for tr in table_selc:
            header_selc = tr.find_all("td")[1]
            for val in header_selc:
                values.append(val)

        series = pd.Series(values, index=headers, dtype="string")

        return series


    def efficiency(self):
        '''
        Get table of efficiency metrics under MarketWatch Profile page.
        Arguments are:
            None
        Returns: pandas Series
            Returns pandas Series of efficiency metrics.
        '''

        # URL to check for efficiency table.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        table = soup.find_all('table', attrs={'class':'table value-pairs no-heading'})[1]
        table_selc = table.tbody.find_all("tr")

        headers = []
        for tr in table_selc:
            header_selc = tr.find_all("td")[0]
            for val in header_selc:
                headers.append(val)

        values = []
        for tr in table_selc:
            header_selc = tr.find_all("td")[1]
            for val in header_selc:
                values.append(val)

        series = pd.Series(values, index=headers, dtype="string")

        return series


    def liquidity(self):
        '''
        Get table of liquidity metrics under MarketWatch Profile page.
        Arguments are:
            None
        Returns: pandas Series
            Returns pandas Series of liquidity metrics.
        '''

        # URL to check for liquidity table.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE 
        soup = bs(html_content, "lxml")

        table = soup.find_all('table', attrs={'class':'table value-pairs no-heading'})[2]
        table_selc = table.tbody.find_all("tr")

        headers = []
        for tr in table_selc:
            header_selc = tr.find_all("td")[0]
            for val in header_selc:
                headers.append(val)

        values = []
        for tr in table_selc:
            header_selc = tr.find_all("td")[1]
            for val in header_selc:
                values.append(val)

        series = pd.Series(values, index=headers, dtype="string")

        return series


    def profitability(self):
        '''
        Get table of profitability metrics under MarketWatch Profile page.
        Arguments are:
            None
        Returns: pandas Series
            Returns pandas Series of profitability metrics.
        '''

        # URL to check for profitability table.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        table = soup.find_all('table', attrs={'class':'table value-pairs no-heading'})[3]
        table_selc = table.tbody.find_all("tr")

        headers = []
        for tr in table_selc:
            header_selc = tr.find_all("td")[0]
            for val in header_selc:
                headers.append(val)

        values = []
        for tr in table_selc:
            header_selc = tr.find_all("td")[1]
            for val in header_selc:
                values.append(val)

        series = pd.Series(values, index=headers, dtype="string")

        return series


    def captialization(self):
        '''
        Get table of captialization metrics under MarketWatch Profile page.
        Arguments are:
            None
        Returns: pandas Series
            Returns pandas Series of captialization metrics.
        '''

        # URL to check for profitability table.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        table = soup.find_all('table', attrs={'class':'table value-pairs no-heading'})[4]
        table_selc = table.tbody.find_all("tr")

        headers = []
        for tr in table_selc:
            header_selc = tr.find_all("td")[0]
            for val in header_selc:
                headers.append(val)

        values = []
        for tr in table_selc:
            header_selc = tr.find_all("td")[1]
            for val in header_selc:
                values.append(val)

        series = pd.Series(values, index=headers, dtype="string")

        return series


    def main_page(self):
        '''
        Get table of stock information from MarketWatch landing page.
        Arguments are:
            None
        Returns: pandas Series
            Returns pandas Series of stock information.
        '''

        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        # TABLE
        table = soup.find("div", attrs={'class': 'group group--elements left'})
        table_selc = table.div.ul.find_all("li")

        # HEADERS
        headers = []

        for li in table_selc:
            small = li.find_all("small")
            for header in small:
                header = header.get_text()
                headers.append(header)

        # VALUES
        values = []

        for li in table_selc:
            span = li.find_all("span", attrs={'class': 'primary'})
            for value in span:
                value = value.get_text()
                values.append(value)

        series = pd.Series(values, index=headers, dtype="string")


        # Returns dataframe table
        return series
            
    
    def income_statement(self):
        '''
        Get dataframe of stock income statement
        Arguments are:
            None
        Returns: pandas DataFrame
            Returns pandas DataFrame of stock income statement.
        '''

        # URL Settings and initialise driver as self.driver
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        income_table = soup.find_all("table", attrs={'class': 'table table--overflow align--right'})[0]
        income_headers = income_table.thead.tr.find_all("th")

        headers = []
        for th in income_headers:
            item = th.find_all("div")
            for i in item:
                headers.append(i.contents[0].strip())

        # headers = ['Item', 'Item', '2016', '2017', '2018', '2019', '2020', '5-year trend']

        headers.pop(0)
        headers.pop(-1)
        income_rows = income_table.tbody.find_all("tr")

        index = []

        # items = index
        for tr in income_rows:
            select = tr.find_all("td")[0]
            val = select.find("div").contents[0].strip()
            index.append(val)

            # Get rows
        data_list = [[] for i in range(0,len(headers) -1)] # datalist len = 6
        # rows val
        for tr in income_rows:
            # 1, 2, 3 ,4 ,5 ,6, len(headers) = 6
            # i = 1, 2, 3, 4, 5
            for i in range(1, len(data_list)+1):
                select = tr.find_all("td")[i]
                val = select.find("div").contents[0].get_text()
                data_list[i-1].append(val)

        # Data list add
        data_list.insert(0,index)

        # create dataframe
        df = pd.DataFrame(columns=headers)

        for i in range(0,len(data_list)):
            df[f'{headers[i]}'] = data_list[i]

        # Set item as index
        df = df.set_index(df.columns[0])
            
        # Sort df by year
        df = self.reorder_df(df)

        # Returns dataframe
        return df

    
    def balance_sheet_assets(self):
        '''
        Get dataframe of stock balance sheet assets
        Arguments are:
            None
        Returns: pandas DataFrame
            Returns pandas DataFrame of stock balance sheet assets.
        '''

        # URL Settings and initialise driver as self.driver
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/balance-sheet'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        income_table = soup.find_all("table", attrs={'class': 'table table--overflow align--right'})[0]
        income_headers = income_table.thead.tr.find_all("th")

        headers = []
        for th in income_headers:
            item = th.find_all("div")
            for i in item:
                headers.append(i.contents[0].strip())

        # headers = ['Item', 'Item', '2016', '2017', '2018', '2019', '2020', '5-year trend']

        headers.pop(0)
        headers.pop(-1)
        income_rows = income_table.tbody.find_all("tr")

        index = []

        # items = index
        for tr in income_rows:
            select = tr.find_all("td")[0]
            val = select.find("div").contents[0].strip()
            index.append(val)

            # Get rows
        data_list = [[] for i in range(0,len(headers) -1)] # datalist len = 6
        # rows val
        for tr in income_rows:
            # 1, 2, 3 ,4 ,5 ,6, len(headers) = 6
            # i = 1, 2, 3, 4, 5
            for i in range(1, len(data_list)+1):
                select = tr.find_all("td")[i]
                val = select.find("div").contents[0].get_text()
                data_list[i-1].append(val)

        # Data list add
        data_list.insert(0,index)

        # create dataframe
        df = pd.DataFrame(columns=headers)

        for i in range(0,len(data_list)):
            df[f'{headers[i]}'] = data_list[i]

        # Set item as index
        df = df.set_index(df.columns[0])
            
        # Sort df by year
        df = self.reorder_df(df)

        # Returns dataframe
        return df
        
    
    def balance_sheet_lia(self):
        '''
        Get dataframe of stock balance sheet liabilities
        Arguments are:
            None
        Returns: pandas DataFrame
            Returns pandas DataFrame of stock balance sheet liabilities.
        '''

        # URL Settings and initialise driver as self.driver
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/balance-sheet'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        income_table = soup.find_all("table", attrs={'class': 'table table--overflow align--right'})[1]
        income_headers = income_table.thead.tr.find_all("th")

        headers = []
        for th in income_headers:
            item = th.find_all("div")
            for i in item:
                headers.append(i.contents[0].strip())

        # headers = ['Item', 'Item', '2016', '2017', '2018', '2019', '2020', '5-year trend']

        headers.pop(0)
        headers.pop(-1)
        income_rows = income_table.tbody.find_all("tr")

        index = []

        # items = index
        for tr in income_rows:
            select = tr.find_all("td")[0]
            val = select.find("div").contents[0].strip()
            index.append(val)

            # Get rows
        data_list = [[] for i in range(0,len(headers) -1)] # datalist len = 6
        # rows val
        for tr in income_rows:
            # 1, 2, 3 ,4 ,5 ,6, len(headers) = 6
            # i = 1, 2, 3, 4, 5
            for i in range(1, len(data_list)+1):
                select = tr.find_all("td")[i]
                val = select.find("div").contents[0].get_text()
                data_list[i-1].append(val)

        # Data list add
        data_list.insert(0,index)
        # create dataframe
        df = pd.DataFrame(columns=headers)

        for i in range(0,len(data_list)):
            df[f'{headers[i]}'] = data_list[i]

        # Set item as index
        df = df.set_index(df.columns[0])
            
        # Sort df by year
        df = self.reorder_df(df)

        # Returns dataframe
        return df

    
    def cash_flow_opr(self):
        '''
        Get dataframe of stock cash flow operating activities
        Arguments are:
            None
        Returns: pandas DataFrame
            Returns pandas DataFrame of cash flow operating activities.
        '''

        # URL Settings and initialise driver as self.driver
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/cash-flow'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        income_table = soup.find_all("table", attrs={'class': 'table table--overflow align--right'})[0]
        income_headers = income_table.thead.tr.find_all("th")

        headers = []
        for th in income_headers:
            item = th.find_all("div")
            for i in item:
                headers.append(i.contents[0].strip())

        # headers = ['Item', 'Item', '2016', '2017', '2018', '2019', '2020', '5-year trend']

        headers.pop(0)
        headers.pop(-1)
        income_rows = income_table.tbody.find_all("tr")

        index = []

        # items = index
        for tr in income_rows:
            select = tr.find_all("td")[0]
            val = select.find("div").contents[0].strip()
            index.append(val)

            # Get rows
        data_list = [[] for i in range(0,len(headers) -1)] # datalist len = 6
        # rows val
        for tr in income_rows:
            # 1, 2, 3 ,4 ,5 ,6, len(headers) = 6
            # i = 1, 2, 3, 4, 5
            for i in range(1, len(data_list)+1):
                select = tr.find_all("td")[i]
                val = select.find("div").contents[0].get_text()
                data_list[i-1].append(val)

        
        # Data list add
        data_list.insert(0,index)
        # create dataframe
        df = pd.DataFrame(columns=headers)

        for i in range(0,len(data_list)):
            df[f'{headers[i]}'] = data_list[i]

        # Set item as index
        df = df.set_index(df.columns[0])
            
        # Sort df by year
        df = self.reorder_df(df)

        # Returns dataframe
        return df

    
    def cash_flow_inv(self):
        '''
        Get dataframe of stock cash flow investing activities
        Arguments are:
            None
        Returns: pandas DataFrame
            Returns pandas DataFrame of cash flow investing activities.
        '''

        # URL Settings and initialise driver as self.driver
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/cash-flow'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        income_table = soup.find_all("table", attrs={'class': 'table table--overflow align--right'})[1]
        income_headers = income_table.thead.tr.find_all("th")

        headers = []
        for th in income_headers:
            item = th.find_all("div")
            for i in item:
                headers.append(i.contents[0].strip())

        # headers = ['Item', 'Item', '2016', '2017', '2018', '2019', '2020', '5-year trend']

        headers.pop(0)
        headers.pop(-1)
        income_rows = income_table.tbody.find_all("tr")

        index = []

        # items = index
        for tr in income_rows:
            select = tr.find_all("td")[0]
            val = select.find("div").contents[0].strip()
            index.append(val)

            # Get rows
        data_list = [[] for i in range(0,len(headers) -1)] # datalist len = 6
        # rows val
        for tr in income_rows:
            # 1, 2, 3 ,4 ,5 ,6, len(headers) = 6
            # i = 1, 2, 3, 4, 5
            for i in range(1, len(data_list)+1):
                select = tr.find_all("td")[i]
                val = select.find("div").contents[0].get_text()
                data_list[i-1].append(val)

        # Data list add
        data_list.insert(0,index)
        # create dataframe
        df = pd.DataFrame(columns=headers)

        for i in range(0,len(data_list)):
            df[f'{headers[i]}'] = data_list[i]

        # Set item as index
        df = df.set_index(df.columns[0])
            
        # Sort df by year
        df = self.reorder_df(df)

        # Returns dataframe
        return df

    
    def cash_flow_fin(self):
        '''
        Get dataframe of stock cash flow financing activities
        Arguments are:
            None
        Returns: pandas DataFrame
            Returns pandas DataFrame of cash flow financing activities.
        '''

        # URL Settings and initialise driver as self.driver
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/financials/cash-flow'

        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        income_table = soup.find_all("table", attrs={'class': 'table table--overflow align--right'})[2]
        income_headers = income_table.thead.tr.find_all("th")

        headers = []
        for th in income_headers:
            item = th.find_all("div")
            for i in item:
                headers.append(i.contents[0].strip())

        headers.pop(0)
        headers.pop(-1)
        income_rows = income_table.tbody.find_all("tr")

        index = []

        # items = index
        for tr in income_rows:
            select = tr.find_all("td")[0]
            val = select.find("div").contents[0].strip()
            index.append(val)

            # Get rows
        data_list = [[] for i in range(0,len(headers) -1)] # datalist len = 6
        # rows val
        for tr in income_rows:
            # 1, 2, 3 ,4 ,5 ,6, len(headers) = 6
            # i = 1, 2, 3, 4, 5
            for i in range(1, len(data_list)+1):
                select = tr.find_all("td")[i]
                val = select.find("div").contents[0].get_text()
                data_list[i-1].append(val)

        # Data list add
        data_list.insert(0,index)

        # create dataframe
        df = pd.DataFrame(columns=headers)

        for i in range(0,len(data_list)):
            df[f'{headers[i]}'] = data_list[i]

        # Set item as index
        df = df.set_index(df.columns[0])
            
        # Sort df by year
        df = self.reorder_df(df)

        # Returns dataframe
        return df
    
    
    def balance_sheet(self):
        '''
        Prints full balance sheet for viewing.
        Arguments are:
            None
        Returns: str
            Returns 'Printed balance sheet successfully.'
        '''
        asset = self.balance_sheet_assets()
        time.sleep(3)
        lia = self.balance_sheet_lia()
        print(asset)
        print(lia)
        
        return 'Printed balance sheet successfully.'
    
    
    def cash_flow(self):
        '''
        Prints full cash flow statement for viewing.
        Arguments are:
            None
        Returns: str
            Returns 'Printed cash flow statement successfully.'
        '''
        opr = self.cash_flow_opr()
        time.sleep(2)
        inv = self.cash_flow_inv()
        time.sleep(2)
        fin = self.cash_flow_fin()
        print(opr)
        print(inv)
        print(fin)

        return 'Printed cash flow statement successfully.'


    def years(self):
        '''
        Gets list of years of availble scrapped data from MarketWatch using income statement.
        Arguments are:
            None
        Returns: list
            Returns list of years.
        '''

        # Use income statement DataFrame
        df = self.income_statement()

        # Add years into years list
        years = []
        for cols in df.columns:
            years.append(cols)

        # Sort by years
        years.sort(reverse=False)
        # Return
        return years
    

    def fiscal_month(self):
        '''
        Gets first month of fiscal year of stock.
        Arguments are:
            None
        Returns: int
            Returns first month of fiscal year.
        '''

        # URL to check for valuations table.
        URL = f'https://www.marketwatch.com/investing/stock/{self.ticker}/company-profile?mod=mw_quote_tab'


        # GET REQUEST
        html_content = requests.get(URL).text

        # PARSE
        soup = bs(html_content, "lxml")

        val_selc = soup.find_all("ul", attrs={'class': 'list list--kv list--col50'})

        for item in val_selc:
            item_selc = item.find_all("li")[2]
            val = item_selc.find("span").get_text()

        fiscal_val = val

        # Get month start
        month = int(fiscal_val.split("/")[0])
        
        # Get fiscal year's month start date
        if month != 12:
            month = month + 1
        
        elif month == 12:
            month = 1
        
        return month


    def fiscal_year_dates(self):
        '''
        Gets list of start fiscal year dates
        Arguments are:
            None
        Returns: list
            Returns list of start fiscal year dates.
        '''

        # For each date get price of each stock into a list
        month = self.fiscal_month()
        years = self.years()

        # List to add in fiscal year dates
        fiscal_year_list = []
        for year in years:
            year = int(year)
            day = 1
            date = datetime(year, month, day)

            
            f_date = date.strftime("%Y-%m-%d") # 2020-01-01

            # Get pandas market holidays calendar
            nyse = mcal.get_calendar('NYSE')
            # Get start of year + end of year + 1 
            cal_df = nyse.schedule(start_date=f'{years[0]}-01-01', end_date=f'{int(years[-1]) + 1}-01-01')

            # Get Working Days calendars in list
            cal_list = cal_df.index.tolist()

            # If not in append, else + 1 or + 2
            if date in cal_list:
                fiscal_year_list.append(f_date)
                
                
            else:
                # make a loop, break once date is in cal_list
                for i in range(1,100):
                    date = date + timedelta(days=i)
                    f_date = date.strftime("%Y-%m-%d")

                    if date in cal_list:
                        fiscal_year_list.append(f_date)
                        break
                    
        return fiscal_year_list

if __name__ == "__main__":
    fd = Fin_Data('XPEV')
    df = fd.cash_flow_opr()
    print(df)