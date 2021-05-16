<center>
    <img width="100%" src="https://raw.githubusercontent.com/astroDimitrios/astroedu/e2d3007b867c3f5ac34d6bf4b2ca2f02aa38d824/assets/logo/astroeduLOGOtag.svg" alt='AP Logo'>
</center>

[![PyPI version](https://badge.fury.io/py/astroedu.svg)](https://badge.fury.io/py/astroedu)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](code_of_conduct.md) 

This package is in alpha.

## Installation

To install **astroedu** run
```
>>> pip install astroedu
```
then run
```
>>> astroedu build
```
which creates the configuration file **config.ini**.

**config.ini** stores the location of your documents folder.
This is where an astroedu folder for interactive activites will me made. (not yet implemented)

## Current Functionality

### Interactives

```
>>> astroedu interactive wiens_law
```

Loads the interactive notebook file exploring Wien's Law. 
Jupyter lab arguments can be passed after the interactive name for instance:

```
>>> astroedu interactive wiens_law --port 9999
```

### Datasets

To use a data set import the utitlity function ```load_data``` from the datasets module:
```
from astroedu.datasets import load_data
```
Then you can load a data set by passing its name as a string to ```load_data```.
```
planets = load_data('planets')
```
The function returns a Pandas dataframe.
If the optional keyword argument ```info``` is ```True``` then a brief explanation of the data is printed before the dataframe is loaded.

### Constants

Astropy like constants for ease of access.
For full functionality use the astropy [constants](https://docs.astropy.org/en/stable/constants/) submodule.

```
>>> from astroedu.constants import c
>>> c
Constant(c, 299792458, m/s, Speed of light)
```
or
```
>>> import astroedu.constants as const
>>> print(const.c)
Name = Speed of light
Value = 299792458
Unit = m/s
```

Constants can perform simple maths with other constants or int/float/np.array.
The returned value is an int/float/np.array not a Constant class instance:
```
>>> from astroedu.constants import c, m_e
>>> c*m_e
2.7309245302881346e-22
```

### Functions

Some basic functions have been implemented:
```
>>> from astroedu.functions import wiens_law
>>> wiens_law(1000)
2.897771955e-06
```

### Classes

Some classes which are hopefully useful!

##### Body2D

The Body2D class is the main body class for planets and other objects.
Usage - ```Body2D(str-name, float-x pos in AU, float-y pos in AU, float-radius in km, float-mass in kg)``` for instance:

```
>>> from astroedu.classes import Body2D
>>> moon = Body2D('Moon', 0, 0, 1737.4, 0.07346*10**24)
>>> print(moon)
Moon at (0.00, 0.00) AU with r = 1.74E+03 km and m = 7.35E+22 kg
```

There are pre-defined class methods for the Earth, Sun, and Moon:

```
>>> from astroedu.classes import Body2D
>>> moon = Body2D.Moon(0, 0)
>>> print(moon)
Moon at (0.00, 0.00) AU with r = 1.74E+03 km and m = 7.35E+22 kg
```

The class has built in methods. For instance to calculate the tides on the Earth due to the Moon:

```
>>> from astroedu.classes import Body2D
>>> earth = Body2D.Earth(0, 0)
>>> moon = Body2D.Moon(384400000/au, 0)
>>> forces = earth.tides(moon, step=0.25, scale=5.972*10**24)
```
Documentation coming soon.
More methods will be added at a later date including calculating gravitational potentials and plotting tides & potentials.