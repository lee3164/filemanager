
class Config(object):
    DEBUG = True
    PROGECT_PATH = '/home/lxy/Workbench/git/filemanager/'
    DATABASE_PATH = PROGECT_PATH
    DATABASE_NAME = 'db.sqlite'

class TestConfig(Config):
    DATABASE_PATH = Config.PROGECT_PATH + 'test/'
    DATABASE_NAME = 'test.db'
    SECRET_KEY = '1234567890'

def load_config():
    return TestConfig()