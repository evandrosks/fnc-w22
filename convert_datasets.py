import numpy as np
import pandas as pd


def get_data(path: str, name: str):
    '''Grabs stance and body csv files from original dataset and joins them
       to one dataframe.
    
    Args:
        path (str): parent folder of files
        name (str): type of csv to grab ('train' or 'test')
    
    Returns:
        pandas.core.frame.DataFrame of joined bodies and stances
    '''
    stances = pd.read_csv(f'{path}/{name}_stances.csv')
    bodies = pd.read_csv(f'{path}/{name}_bodies.csv')
    
    data = stances.join(bodies.set_index('Body ID'), on='Body ID')
    
    return data    