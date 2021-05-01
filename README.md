<center>
    <img width="100%" src="https://raw.githubusercontent.com/astroDimitrios/astroedu/e2d3007b867c3f5ac34d6bf4b2ca2f02aa38d824/assets/logo/astroeduLOGOtag.svg" alt='AP Logo'>
</center>

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](code_of_conduct.md) 

This package is in alpha.

## Installation

**astroedu** requires:

- Numpy
- Matplotlib
- Pandas
- Jupyterlab
- IPywidgets
- Fire
- importlib-resources

```
>>> pip install astroedu
```
(build not implemented yet!)
then run
```
>>> astroedu build
```
which creates the configuration file **config.ini**.

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