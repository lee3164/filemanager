from modules.file import Group
from common.session import make_session


def _make_group(gname, gcomment):
    return Group(gname=gname, gcomment=gcomment)


def add_group(gname, gcomment):
    g = _make_group(gname, gcomment)
    with make_session() as session:
        session.add(g)
        session.commit()
    return g
