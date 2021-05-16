import unittest
import numpy as np

from astroedu.classes import Body2D
from astroedu.constants import au

class TestLoadData(unittest.TestCase):
    def test_Body2D_tides(self):
        '''
        Test that the data loads as a pandas df
        '''
        earth = Body2D.Earth(0, 0)
        moon = Body2D.Moon(384400000/au, 0)
        forces = earth.tides(moon, step=0.25, scale=5.972*10**24)
        true_forces = [3.31874952061913e-05, np.array([3.43155527e-05, 3.39721024e-05, 3.31738253e-05, 3.24165524e-05,
             3.21141611e-05, 3.24165524e-05, 3.31738253e-05, 3.39721024e-05]), np.array([ 1.12805754e-06,  7.84607232e-07,  0.00000000e+00, -7.70942821e-07,
             -1.07333414e-06, -7.70942821e-07,  0.00000000e+00,  7.84607232e-07]), np.array([ 0.00000000e+00, -4.02857477e-07, -5.49819045e-07, -3.75505178e-07,
             -0.00000000e+00,  3.75505178e-07,  5.49819045e-07,  4.02857477e-07]), np.array([ 0.00000000e+00, -4.02857477e-07, -5.49819045e-07, -3.75505178e-07,
             0.00000000e+00,  3.75505178e-07,  5.49819045e-07,  4.02857477e-07])]
        self.assertEqual(forces, true_forces, 'Forces are not equal')

if __name__ == '__main__':
    unittest.main()