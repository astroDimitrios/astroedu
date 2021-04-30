from configparser import ConfigParser
from os import path
import subprocess

def load_astroedu_path():
    from site import getusersitepackages
    return getusersitepackages() + '/astroedu/'

def load_astroedu_config():
    if not path.exists(config_file_name):
        raise FileExistsError('No config.ini file found. Did you forget to run: \n astroedu build')
    config = ConfigParser()
    config.read(config_file_name)
    return config['astroedu-config']

commands = ['interactive']
astroedu_path = load_astroedu_path()
config_file_name = 'config.ini'
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
        interactive_path = astroedu_path+'interactives/'+interactive_name+'.ipynb'
        interactive_path = './interactives/'+interactive_name+'.ipynb'
        if not path.exists(interactive_path):
            raise FileExistsError(f'No interactive named {interactive_name}.')
        call = ['jupyter', 'lab']
        call_args = list(args[2:]) if len(args) > 2 else []
        run_interactive = call + [interactive_path] + call_args
        print(f'Loading interactive {interactive_name}!')
        subprocess.run(run_interactive)

# if __name__ == '__main__':
#     startup('interactive', 'wiens_law', '--port', '9999')