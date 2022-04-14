import numpy as np
from astroedu import constants as const

def get_today(format='%Y/%m/%d'):
    ''' Gets today's date

    Args:
        format -- str, format str for the .strftime(format) call

    Returns:
        string of the date

    Example:
        >>> get_today()
        '2022/04/14'
        >>> get_today('%Y_%m_%d')
        '2022_04_14'
    '''
    from datetime import datetime
    return datetime.today().strftime(format)

def get_config_path(which_path):
    ''' Gets the path to astroedu install or Documents directory

    Args:
        which_path -- str, 'astroedu' or 'docs'

    Returns:
        str path to the astroedu install or to the Documents directory

    Example:
        >>> get_config_path('docs')
        >>> get_config_path('astroedu')
    '''

    from importlib.util import find_spec

    astroedu_path = find_spec('astroedu').submodule_search_locations[0]

    if which_path == 'astroedu':
        return astroedu_path
    else:
        from configparser import ConfigParser
        config = ConfigParser()
        try:
            config.read(astroedu_path+'/config.ini')
        except FileNotFoundError as err:
            return print('No astroedu config.ini file. Did you forget to run\n>>> astroedu build')
        path = config['astroedu-config']['docs_path']
        return path

def get_sun(*args, **kwargs):
    '''Gets a picture of today's Sun using the SunPy package

    Args:
        date -- str, of format yyyy/mm/dd
        save -- str, 'save'

    Returns:
        opens a plot of the Sun on the requested date
        from the SDO HMI instrument continuum band

        can save the image to the folder Documents/astroedu

    Example:
        From command line
        >>> astroedu get_sun                          # plots today's Sun
        >>> astroedu get_sun 2022/02/02               # plots Sun on diff date than today
        >>> astroedu get_sun save                     # plots then saves image
        In .py or IPython
        >>> from astroedu.functions import get_sun
        >>> get_sun()                                 # plots today's Sun
        >>> get_sun('2022/02/02')                     # plots Sun on diff date than today
        >>> get_sun('2022/02/02', save=True)          # plots then saves image
    '''

    # need SunPy installed
    try:
        import sunpy.map as smap
        from sunpy.net.helioviewer import HelioviewerClient
    except ImportError as err:
        return print("SunPy is not installed.\nhttps://docs.sunpy.org/en/stable/installation.html")

    # SAVE can be set as get_sun(SAVE=True) or via CLI
    SAVE = kwargs.get('save', False)

    # if args passed through Fire CLI as tuple of tuple
    # args are now just inner tuple
    try:
        if isinstance(args[0], tuple):
            args = args[0] 
    except:
        pass

    # today's Sun
    if len(args) == 0:
        date = get_today()
        if SAVE:
            save_date = get_today('%Y_%m_%d')
    elif args[0] == 'save':
        date = get_today()
        save_date = get_today('%Y_%m_%d')
        SAVE = True
    # Sun on different date
    else:
        import datetime
        year, month, day = args[0].split('/')

        try:
            date = datetime.datetime(int(year), int(month), int(day))
        except ValueError as err:
            return print("Date not in the format 'yyyy/mm/dd'")
        
        if (len(args) > 1) or (SAVE == True):
            save_date = '_'.join([year, month, day])
            SAVE = True

    hv = HelioviewerClient()  
    sun = hv.download_jp2(date, observatory="SDO", instrument="HMI", measurement="continuum") 
    hmiC = smap.Map(sun)
    
    import matplotlib.pyplot as plt

    fig = plt.figure(1)
    ax = plt.subplot(111, projection=hmiC)
    cmap = plt.get_cmap('afmhot')
    hmiC.plot(cmap=cmap, annotate=False)
    plt.title(f'SDO HMI Continuum {date}')
    plt.clim(0,300)
    plt.axis('off')
    
    if SAVE:
        save_location = get_config_path('docs')+'/astroedu'

        # check astroedu direc exists in Documents and if not make it
        from pathlib import Path
        Path(save_location).mkdir(exist_ok=True)

        save_name = 'SDO_Sun_'+save_date+'.png'
        print(f'Saving file {save_name} to:\n {save_location}')
        plt.savefig(save_location+'/'+save_name, dpi=300)

    plt.show()

    return


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