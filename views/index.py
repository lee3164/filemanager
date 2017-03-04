# -*- coding: utf-8 -*-
from common.util import get_post_param, make_json_success_response, assert_param_is_none
from common.decorator import handle_error_if_exist
from common.error import FileManagerException, FileManagerErrorCode
from common.file import get_files_by_dir
def index():
    val = get_post_param('aa', '', str)
    data = {
        'aa': val
    }
    return make_json_success_response(data)

# 增


# 删



# 改




# 查
@handle_error_if_exist
def get_dir_files():
    dirname = get_post_param('dir_name', '', str)
    print 'dirname', dirname
    if dirname == '':
        raise FileManagerException(FileManagerErrorCode.ERROR_CODE_PARAM_ERROR)
    data = get_files_by_dir(dirname)
    return make_json_success_response(data)


def get_file_by_name(filename):
    pass







