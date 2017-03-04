from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Session = scoped_session(sessionmaker())
Base = declarative_base()
Base.query = Session.query_property()

def _create_engine(db_path, db_name):
    path = 'sqlite:///%s%s' % (db_path, db_name)
    engine = create_engine(path)
    return engine


def config_db(app):
    config = app.config
    engine = _create_engine(config.get('DATABASE_PATH'), config.get('DATABASE_NAME'))
    Session.configure(bind=engine)
    from modules.file import File
    Base.metadata.create_all(engine)

def config_db(db_path, db_name):
    engine = _create_engine(db_path, db_name)
    Session.configure(bind=engine)
    from modules.file import File
    Base.metadata.create_all(engine)