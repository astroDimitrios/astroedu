'''
astroedu.datasets - utilities for loading datasets
'''

from importlib_resources import files, is_resource
import pandas as pd

help_text = '''Pass the name of a dataset to load_data as a string.\n
For instance to load the planets dataset run load_data('planets').\n
The returned value is a Pandas dataframe.\n
To see all available datasets go to https://github.com/astroDimitrios/astroedu/tree/main/src/astroedu/datasets'''

def load_data(data, info=False):
    ''' Loads a dataset as a Pandas dataframe

    Special case data == 'help' the help_text is printed to console
    All datasets visible at:
    https://github.com/astroDimitrios/astroedu/tree/main/src/astroedu/datasets

    Args:
        data -- string, name of the csv file to load (without extension)
        info -- boolean, default False - if True prints a short description
                of the data before loading the dataframe

    Returns:
        A pandas dataframe

    Example:
        >>> planets = load_data('planets')
        >>> load_data('help')
    '''
    if data == 'help':
        print(help_text)
        return
    data_csv = data+'.csv'
    if not is_resource('astroedu.datasets', data_csv):
            raise FileExistsError(f'No data file named {data_csv} found.')
    with files('astroedu.datasets').joinpath(data_csv) as p:
        if info:
            with files('astroedu.datasets').joinpath(data+'.txt') as i:
                InfoHandler = open(str(i), 'r')
                print(InfoHandler.read())
        return pd.read_csv(str(p))