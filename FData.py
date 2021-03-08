from Fin_Data import Fin_Data
from Fin_Extract import Fin_Extract

class FData(Fin_Data, Fin_Extract):
    '''
    The FData class merges Financial Data methods with extraction methods. Inherits Fin_Data and Fin_Extract.
    Attributes are:
        ticker : str
            Specifies which ticker to extract data from. (Required)
    '''

    def __init__(self, ticker):
        Fin_Extract.__init__(self,ticker)
    