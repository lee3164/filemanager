from modules.file import File, User, Group
from common.session import make_session


def get_files_by_dir(dirname):
    ret = []
    with make_session() as session:
        files = File.query.filter(File.fparent == dirname).all()
        for f in files:
            ret.append(f.to_json())
    return ret
