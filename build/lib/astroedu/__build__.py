from configparser import ConfigParser
from os import path
from importlib.util import find_spec

def get_astroedu_path():
    return find_spec('astroedu').submodule_search_locations[0]

def build_path_config():
    astroedu_path = get_astroedu_path()
    documents_path = path.expanduser('~/Documents')

    config = ConfigParser()
    config['astroedu-config'] = {'install_path':astroedu_path, 'docs_path':documents_path}

    f = open(astroedu_path+'/config.ini', 'w')
    config.write(f)
    f.close()