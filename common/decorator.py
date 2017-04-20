import functools
from flask import session, request

from common.error import \
    error_transform, \
    FileManagerErrorCode as ErrorCode, \
    FileManagerException

from common.util import make_json_response, get_post_param
from dal import user_dal, file_dal


def handle_error_if_exist(func):
    @functools.wraps(func)
    def _wrapped(*args, **kwargs):
        try:
            ret = func(*args, **kwargs)
        except Exception, err:
            err = error_transform(err)
            return make_json_response(err.error)
        else:
            return ret

    return _wrapped


def require_login(func):
    @functools.wraps(func)
    def _wrapped(*args, **kwargs):
        uid = session.get('uid', None) or 0
        print 'uid:', uid
        if not uid:
            raise FileManagerException(ErrorCode.ERROR_CODE_REQUIRE_LOGIN)
        c, u = user_dal.get_user_by_id(uid)
        if c != ErrorCode.ERROR_CODE_OK:
            raise FileManagerException(c)
        setattr(request, 'user', u)
        return func(*args, **kwargs)

    return _wrapped


def check_permission(func):
    @functools.wraps(func)
    def _wrapped(*args, **kwargs):
        fid = get_post_param('fid', 0, int)
        assert fid, 'require param: fid'
        user = request.user
        file = file_dal.get_file_by_id(fid)
        if file.uid != user.id:
            raise FileManagerException(ErrorCode.ERROR_CODE_NO_PERMISSION)
        return func(*args, **kwargs)
    return _wrapped