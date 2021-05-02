import numpy as np

class Constant:
    ''' Class for defining all constants

        For more functionality use astropy's constant instead
        https://docs.astropy.org/en/stable/constants/
        Most of the constants were taken from the page above

    Example:
        >>> c = Constant('c', 299792458, 'm/s', 'Speed of light')
        >>> c
        299792458
    '''

    def __init__(self, symbol, value, unit, name):
        self.symbol = symbol
        self.value = value
        self.unit = unit 
        self.name = name

    def __repr__(self):
        return f'Constant({self.symbol}, {self.value}, {self.unit}, {self.name})'

    def __str__(self):
        return f'Name = {self.name}\nValue = {self.value}\nUnit = {self.unit}'

    def __add__(self, other):
        if isinstance(other, Constant):
            return self.value + other.value
        else:
            return self.value + other

    def __sub__(self, other):
        if isinstance(other, Constant):
            return self.value - other.value
        else:
            return self.value - other

    def __mul__(self, other):
        if isinstance(other, Constant):
            return self.value * other.value
        else:
            return self.value * other

    def __truediv__(self, other):
        if isinstance(other, Constant):
            return self.value / other.value
        else:
            return self.value / other

    def __pow__(self, other):
        if isinstance(other, Constant):
            return self.value ** other.value
        else:
            return self.value ** other

atm = Constant('atm', 101325, 'Pa', 'Standard Atmosphere')

au = Constant('AU', 1.49597871e+11, 'm', 'Astronomical Unit')

b_wien = Constant('b', 2.897771955e-3, 'm K', 'Wiens Displacement constant')

c = Constant('c', 299792458, 'm/s', 'Speed of light')

e = Constant('e', 1.60217663e-19, 'C', 'Electron Charge')

g0 = Constant('g', 9.80665, 'm/s2', 'Standard acceleration of gravity')

G = Constant('G', 6.6743e-11, 'm3 / (kg s2)', 'Gravitational constant')

h = Constant('h', 6.62607015e-34, 'Js', 'Planck constant')

hbar = Constant('hbar', 1.05457182e-34, 'Js', 'Reduced Planck constant')

k_B = Constant('kB', 1.380649e-23, 'J/K', 'Boltzman constant')

L_bol0 = Constant('L_bol0', 3.0128e+28, 'W', 'Luminosity for absolute bolometric magnitude 0')

L_sun = Constant('L_sun', 3.828e+26, 'W', 'Nominal Solar Luminosity')

m_e = Constant('m_e', 9.1093837e-31, 'kg', 'Electron mass')

m_n = Constant('m_n', 1.6749275e-27, 'kg', 'Neutron mass')

m_p = Constant('m_p', 1.67262192e-27, 'kg', 'Proton mass')

M_earth = Constant('M_earth', 5.97216787e+24, 'kg', 'Earth mass')

M_jup = Constant('M_jup', 1.8981246e+27, 'kg', 'Jupiter mass')

M_sun = Constant('M_sun', 1.98840987e+30, 'kg', 'Solar mass')

pc = Constant('pc', 3.08567758e+16, 'm', 'Parsec')

R_earth = Constant('R_earth', 5.97216787e+24, 'm', 'Nominal Earth equatorial radius')

R_jup = Constant('R_jup', 1.8981246e+27, 'm', 'Nominal Jupiter equatorial radius')

R_sun = Constant('R_sun', 1.98840987e+30, 'm', 'Nominal solar radius')

sigma_sb = Constant('sigma_sb', 5.67037442e-08, 'W / (K4 m2)', 'Stefan-Boltzmann constant')

u = Constant('u', 1.66053907e-27, 'kg', 'Atomic mass unit')