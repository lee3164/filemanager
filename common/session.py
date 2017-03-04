from modules import Session

def make_session():
    return SessionHelper()

class SessionHelper():
    def __init__(self):
        pass

    def __enter__(self):
        self._session = Session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print exc_type
        print exc_val
        print exc_tb
        self._session.close()

    def __getattr__(self, item):
        return getattr(self._session, item)


