import pandas as pd
from pathlib import Path

class ToJson:
    '''
    The ToJson class stores pandas DataFrames and Series' into JSON files and stores it in a database.
    Attributes are:
        None
    '''
    
    def json(self, from_obj=None, export_to=None, filename=None, orient='columns'):
        '''
        Stores pandas DataFrame or Series into JSON file and store into database.
        Arguments are:
            from_obj : pandas DataFrame or pandas Series
                Specifies object type to store as JSON. Default is None (Optional)
            export_to : str
                Specifies directory to store JSON file at. Default is None (Optional)
            filename : str
                Specifies file name of JSON file. Default is None (Optional)
            orient : str
                Specifies orient of pandas.to_json function. Default is columns (Optional)
        Returns: None
            Returns None.
        '''
        # Convert object into json object
        obj = from_obj
        obj.to_json(f'{export_to}\\{filename}', orient=orient)

        return None
