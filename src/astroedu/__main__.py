import subprocess
from importlib_resources import files, is_resource
from importlib.util import find_spec
from configparser import ConfigParser
import fire

from astroedu.__build__ import get_astroedu_path
from astroedu.__build__ import build_path_config

commands = ['build', 'interactive', 'magfield', 'get_sun']
astroedu_path = get_astroedu_path()
config_file_name = '/config.ini'
config_file_path = astroedu_path + config_file_name

def main():
    ''' Entry point for package
    '''
    fire.Fire(startup)

def load_astroedu_config():
    ''' Loads the config.ini file

    Returns:
        The config dictionary

    Example:
        >>> astroedu_config = load_astroedu_config()
    '''
    if not is_resource('astroedu', 'config.ini'):
        raise FileExistsError('No config.ini file found. Did you forget to run: \n astroedu build')
    config = ConfigParser()
    config.read(config_file_path)
    return config['astroedu-config']

def _load_interactive(*args):
    ''' Loads an interactive notebook
        Called from startup() only
    '''
    interactive_name = args[1]
    if not is_resource('astroedu.interactives', interactive_name+'.ipynb'):
        raise FileExistsError(f'No interactive named {interactive_name} found.')
    with files('astroedu').joinpath('interactives', interactive_name+'.ipynb') as p:
        call = ['jupyter', 'lab']
        call_args = list(args[2:]) if len(args) > 2 else []
        run_interactive = call + [str(p)] + call_args
        print(f'Loading interactive {interactive_name}!')
        subprocess.run(run_interactive)

def _planetmagfield_quick(*args):
    ''' Utility function to make wuick plots using planetMagFields
    See https://zenodo.org/record/5140421#.YSdp7t_TUuU
    '''
    levels=20
    cmap='RdBu_r'
    proj = 'Mollweide'
    r = 1

    import numpy as np
    
    if len(args) > 4:
        raise ValueError("Too many arguments, exiting ...\n")
    elif len(args) == 4:
        planet = str(args[1]).lower()
        r      = np.float32(args[2])
        proj   = str(args[3])
    elif len(args) == 3:
        planet = str(args[1]).lower()
        try:
            r      = np.float32(args[2])
        except:
            proj   = str(args[2])
    elif len(args) == 2:
        if args[2] == '--help':
            print('planetMagFields\nSubmodule by Ankit Barik - 10.5281/zenodo.5140421\nUsage see - github.com/AnkitBarik/planetMagFields')
        else:
            print("Radius not specified, using surface\n")
            planet = str(args[1]).lower()
    else:
        print("Planet or radius not specified, plotting for Earth's surface\n")
        planet="earth"
        r=1.

    import matplotlib.pyplot as plt
    # from astroedu.planetmagfields.libbfield import getBr, plotAllFields, plotMagField

    if planet == 'all':
        from astroedu.planetmagfields.libbfield import plotAllFields

        with files('astroedu.planetmagfields').joinpath('data/') as p:
            plotAllFields(datDir=p,r=r,levels=levels,cmap=cmap,proj=proj)
            plt.tight_layout()
            plt.subplots_adjust(top=0.895,
                                bottom=0.035,
                                left=0.023,
                                right=0.976,
                                hspace=0.38,
                                wspace=0.109)
    else:
        from astroedu.planetmagfields.libbfield import plotMagField

        with files('astroedu.planetmagfields').joinpath('data/') as p:
            # plotMagField(planet=planet,r=r,datDir=p,levels=levels,cmap=cmap,proj=proj)
            plotMagField(name=planet,r=r,levels=levels,cmap=cmap,proj=proj)
            plt.tight_layout()

    plt.show()

def _get_sun_shortcut(*args):
    ''' Shortcut function to call get_sun
        with any args passed to the Fire CLI
    '''
    from astroedu.functions import get_sun

    if len(args) == 1:
        return get_sun()
    else:
        return get_sun(args[1:])

def startup(*args):
    ''' Startup function called by Fire cli function main()

    Based on arguments passed to astroedu call
    - builds config.ini file
    - launches interactive notebook

    Args:
        args[0] -- string, name of astroedu command to call

    Example:
        Loads the wiens_law interactive and launches jupyterlab
        >>> astroedu interactive wiens_law
        Arguments passed after the interactive name go to jupyter
        >>> astroedu interactive wiens_law --port 9999

        To build the config.ini file
        >>> astroedu build
    '''
    if not args:
        raise ValueError('No arguments passed to astroedu call.')
    command = args[0].lower()
    if command not in commands:
        raise ValueError('Command not recognised.')
    elif command == 'build': 
        build_path_config()
    elif command == 'get_sun':
        _get_sun_shortcut(*args)
    elif len(args) == 1: # build and get_sun don't need extras
        raise ValueError(f'No arguments passed to {command}')
    elif command == 'interactive':
        _load_interactive(*args)
    elif command == 'magfield':
        _planetmagfield_quick(*args)

if __name__ == '__main__':
    fire.Fire(startup)