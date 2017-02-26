
class Config(object):
    DEBUG = True
    DATABASE_PATH = '/Users/lxy-mac/Workbench/python/filemanager/'
    DATABASE_NAME = 'db.sqlite'


def load_config():
    return Config()