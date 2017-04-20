# coding=utf-8
from flask import session, request

from dal import user_dal, file_dal
from common.error import FileManagerErrorCode as ErrorCode, \
    FileManagerException, assert_no_error
from operator import itemgetter


def add_file(file_name, parent_name, mode, comment, file_type, file_link=''):
    user = request.user or None
    uid = user.id
    gid = user.group[0].id  # TODO: 支持多组
    params = {
        'fname': file_name,
        'fparent': parent_name,
        'ftype': file_type,
        'fmode': mode,
        'fcomment': comment,
        'flink': file_link,
        'uid': uid,
        'gid': gid
    }
    return file_dal.create_file(**params)


def rename(fid, new_name):
    return file_dal.rename(fid, new_name)


def get_files_by_dir(dirname):
    user = request.user or None
    code, dir_obj = file_dal.get_file_by_name(dirname)
    assert_no_error(code)
    r, _, x = _view_mode(user, dir_obj)
    if not x:
        raise FileManagerException(ErrorCode.ERROR_CODE_XPERMISSION_DENYED)
    if not r:
        raise FileManagerException(ErrorCode.ERROR_CODE_RPERMISSION_DENYED)

    data = file_dal.get_files_by_dir(dirname, user.id)
    sorted(data, key=lambda obj: (obj['file_type'], obj['file_name']))
    return data


def get_file_link(fid):
    return file_dal.get_file_link(fid)


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
