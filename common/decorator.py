import functools
from common.error import error_transform
from common.util import make_json_response


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