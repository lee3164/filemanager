class FileManagerErrorCode(object):
    ERROR_CODE_OK = 0

    ERROR_CODE_PARAM_ERROR = 4000
    ERROR_CODE_FILE_EXISTED = 4001
    _err_maps = {
        ERROR_CODE_OK: 'OK',
        ERROR_CODE_PARAM_ERROR: 'ERROR_PARAM_ERROR',
        ERROR_CODE_FILE_EXISTED: 'ERROR_FILE_EXISTED'
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