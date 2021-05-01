import subprocess
from importlib_resources import files, is_resource
from importlib.util import find_spec
from configparser import ConfigParser
import fire

from astroedu.__build__ import get_astroedu_path

def main():
    fire.Fire(startup)

def load_astroedu_config():
    if not is_resource('astroedu', 'config.ini'):
        raise FileExistsError('No config.ini file found. Did you forget to run: \n astroedu build')
    config = ConfigParser()
    config.read(config_file_path)
    return config['astroedu-config']

commands = ['build', 'interactive']
astroedu_path = get_astroedu_path()
config_file_name = '/config.ini'
config_file_path = astroedu_path + config_file_name

def startup(*args):
    if not args:
        raise ValueError('No arguments passed to astroedu call.')
    command = args[0]
    if command not in commands:
        raise ValueError('Command not recognised.')
    elif len(args) == 1:
        raise ValueError(f'No arguments passed to {command}')

    if command == 'build': 
        from astroedu.__build__ import build_path_config
        build_path_config()
    elif command == 'interactive':
        interactive_name = args[1]
        if not is_resource('astroedu.interactives', interactive_name+'.ipynb'):
            raise FileExistsError(f'No interactive named {interactive_name} found.')
        with files('astroedu').joinpath('interactives', interactive_name+'.ipynb') as p:
            call = ['jupyter', 'lab']
            call_args = list(args[2:]) if len(args) > 2 else []
            run_interactive = call + [str(p)] + call_args
            print(f'Loading interactive {interactive_name}!')
            subprocess.run(run_interactive)

if __name__ == '__main__':
    fire.Fire(startup)