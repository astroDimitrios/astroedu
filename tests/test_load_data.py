import unittest
import pandas as pd

from astroedu.datasets import load_data

class TestLoadData(unittest.TestCase):
    def test_load_data(self):
        '''
        Test that the data loads as a pandas df
        '''
        data = 'planets'
        result = load_data(data)
        self.assertIsInstance(result, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()