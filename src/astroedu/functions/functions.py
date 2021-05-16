import numpy as np
from astroedu import constants as const

def wiens_law(a):
    ''' Computes the peak wavelengths if temperatures are passed
        Computes the temperatures if peak wavelengths are passed

    0 must not be passed as an argument since 1/0 will fail

    Args:
        a -- float or 1D np.ndarray, peak wavelength or temperature

    Returns:
        float or 1D np.ndarray, peak wavelength or temperature

    Example:
        To get peak wavelengths pass the temperatures to arg a
        >>> T = np.arange(0.1, 3000, 10) # K
        >>> wiens_law(T)
        To get a temperature pass a wavelength
        >>> l = 500*10**(-9) # m
        >>> wiens_law(l)
    '''
    return const.b_wien/a

def plancks_law(T, l):
    ''' Computes the blackbody curve over wavelength range l for temp T
        using Planck's law

    Args:
        T -- float, temperature of blackbody
        l -- float or 1D np.ndarray, wavelengths

    Returns:
        float or 1D np.ndarray, intensity in units: 10^4 W sr^-1 m^-2 nm^-1

    Example:
        >>> plancks_law(300, 560*10**-9)
    '''
    return 2*const.h*const.c**2/l**5 * 1/(np.exp(const.h*const.c/(l*const.k_B*T))-1)