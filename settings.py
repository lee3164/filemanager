
class Config(object):
    DEBUG = True
    PROGECT_PATH = '/Users/lxy-mac/Workbench/python/filemanager/'
    DATABASE_PATH = PROGECT_PATH
    DATABASE_NAME = 'db.sqlite'

class TestConfig(Config):
    DATABASE_PATH = Config.PROGECT_PATH + 'test/'
    DATABASE_NAME = 'test.db'

def load_config():
    return TestConfig()