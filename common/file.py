from modules.file import File, User, Group
from common.session import make_session
from sqlalchemy import and_
from flask import session

def _check_if_set(pos, mode):
    return False if mode[pos] == '-' else True

def _check_user_is_in_group(user, group):
    ret = False
    for g in user.group:
        if g == group:
            ret = True
            break
    return ret

def _view_mode(user, file):
    r = False
    w = False
    x = False
    if user == file.user:
        mode = file.fmode[:3]
        r = _is_user_have_rmode(mode)
        w = _is_user_have_wmode(mode)
        x = _is_user_have_xmode(mode)
    elif _check_user_is_in_group(user, file.group):
        mode = file.fmode[3:6]
        r = _is_user_have_rmode(mode)
        w = _is_user_have_wmode(mode)
        x = _is_user_have_xmode(mode)
    else:
        mode = file.fmode[6:9]
        r = _is_user_have_rmode(mode)
        w = _is_user_have_wmode(mode)
        x = _is_user_have_xmode(mode)
    return r, w, x


def _is_user_have_rmode(mode):
    return _check_if_set(0, mode)

def _is_user_have_wmode(mode):
    return _check_if_set(1, mode)

def _is_user_have_xmode(mode):
    return _check_if_set(2, mode)

def get_files_by_dir(dirname):
    ret = []
    with make_session() as session:
        files = File.query.filter(File.fparent == dirname).all()
        for f in files:
            ret.append(f.to_json())
    return ret

def get_file_info_by_name(dirname, filename):
    ret = {}
    with make_session() as session:
        file = File.query.filter(and_(File.fparent == dirname,
                                      File.fname == filename)).first()
        if file != None:
            ret = file.to_json()
    return ret
