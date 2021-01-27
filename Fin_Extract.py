from Fin_Data import Fin_Data


stock = Fin_Data('MSFT')
stock.income_statement()
stock.driver_end()


# Class Fin_Extract, inheritance from Fin_Data
# class Fin_Extract(Fin_Data):
#     '''
#     # Financial Data Scrapper Made by Gavin Loo 2021.
#     Uses data from MarketWatch.com
#     Uses Fin_Data and Fin_Select Class to extract individual data in str format

#     Args = ticker name, PATH of chromedriver
#     Finish with driver_end() to end drawing data.
#     '''
    
#     # Initializes Fin_Extract class
#     def __init__(self, ticker, PATH = 'C:\Program Files (x86)\chromedriver.exe'):
#         Fin_Data.__init__(self, ticker, PATH = 'C:\Program Files (x86)\chromedriver.exe')
    




