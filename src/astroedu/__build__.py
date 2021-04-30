from configparser import ConfigParser
from os import path
from site import getusersitepackages

def build_path_config():
    install_path = getusersitepackages() + '/astroedu/'
    documents_path = path.expanduser('~/Documents')

    config = ConfigParser()
    config['astroedu-config'] = {'astroedu_path':install_path, 'docs_path':documents_path}

    f = open('config.ini', 'w')
    config.write(f)
    f.close()