from Fin_Data import Fin_Data
from Fin_Extract import Fin_Extract

class FData(Fin_Data, Fin_Extract):
    '''
    The FData class merges Financial Data methods with extraction methods. Inherits Fin_Data and Fin_Extract.
    Attributes are:
        ticker : str
            Specifies which ticker to extract data from. (Required)
        PATH : str
            Specifies where the Chromium WebDriver is located. (Required)
        ignore_errors : "bool"
            Option whether to ignore errors for selenium WebDriver. True = ignore errors. Default is True (Optional)
    '''

    def __init__(self, ticker, PATH = 'C:\Program Files (x86)\chromedriver.exe', ignore_errors=True):
        Fin_Data.__init__(self, ticker, PATH = 'C:\Program Files (x86)\chromedriver.exe')
        Fin_Extract.__init__(self,ticker)
    