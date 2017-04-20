class FileManagerErrorCode(object):
    ERROR_CODE_OK = 0

    ERROR_CODE_PARAM_ERROR = 4000
    ERROR_CODE_FILE_EXISTED = 4001
    ERROR_CODE_USER_NOT_EXIST = 4002
    ERROR_CODE_PASSWORD_ERROR = 4003
    ERROR_CODE_FILE_NOT_EXIST = 4004
    ERROR_CODE_REQUIRE_LOGIN = 4005

    ERROR_CODE_RPERMISSION_DENYED = 4100
    ERROR_CODE_WPERMISSION_DENYED = 4101
    ERROR_CODE_XPERMISSION_DENYED = 4102
    ERROR_CODE_NO_PERMISSION = 4103

    ERROR_CODE_INTERNAL_SERVER_ERROR = 5000

    _err_maps = {
        ERROR_CODE_OK: 'ok',

        ERROR_CODE_PARAM_ERROR: 'param error',
        ERROR_CODE_FILE_EXISTED: 'file existed',
        ERROR_CODE_USER_NOT_EXIST: 'user not exist',
        ERROR_CODE_PASSWORD_ERROR: 'password error',
        ERROR_CODE_FILE_NOT_EXIST: 'file not exist',
        ERROR_CODE_REQUIRE_LOGIN: 'require login',

        ERROR_CODE_RPERMISSION_DENYED: 'no read permission',
        ERROR_CODE_WPERMISSION_DENYED: 'no write permission',
        ERROR_CODE_XPERMISSION_DENYED: 'no execute permission',
        ERROR_CODE_NO_PERMISSION: 'no permission',

        ERROR_CODE_INTERNAL_SERVER_ERROR: 'internal server error'
    }

    @classmethod
    def get_err_msg(cls, code):
        return cls._err_maps[code]


class FileManagerException(Exception):
    def __init__(self, code, msg=None):
        self.code = code
        self.msg = msg or FileManagerErrorCode.get_err_msg(code)

    @property
    def error(self):
        ret = {
            'code': self.code,
            'message': self.msg,
        }
        return ret


def error_transform(err):
    if isinstance(err, FileManagerException):
        return err
    elif isinstance(err, AssertionError):
        return FileManagerException(FileManagerErrorCode.ERROR_CODE_PARAM_ERROR, err.message)
    else:
        return FileManagerException(FileManagerErrorCode.ERROR_CODE_INTERNAL_SERVER_ERROR)


def assert_no_error(code, msg=None):
    if code != FileManagerErrorCode.ERROR_CODE_OK:
        raise FileManagerException(code)
