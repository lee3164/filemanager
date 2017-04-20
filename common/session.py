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
        self._session.commit()
        if exc_type is not None:
            self._session.rollback()
        self._session.close()

    def __getattr__(self, item):
        return getattr(self._session, item)
