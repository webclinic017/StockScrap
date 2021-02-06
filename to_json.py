import pandas as pd
from pathlib import Path

class ToJson:
    '''
    Converts pandas DataFrame into JSON file, and stores it somewhere, stores index data as well.
    # Returns None
    '''
    
    def json(self, from_obj=None, export_to=None, filename=None):
        
        # Convert object into json object
        obj = from_obj
        obj.to_json(f'{p}\\{filename}', orient='index')

        return None

    
    
        




    