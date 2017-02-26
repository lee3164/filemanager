# -*- coding: utf-8 -*-
from common.util import get_post_param, make_json_success_response, assert_param_is_none
from common.file import add_file, check_file_exist, rename_file
from common.decorator import handle_error_if_exist
from common.error import FileManagerException, FileManagerErrorCode
def index():
    val = get_post_param('aa', '', str)
    data = {
        'aa': val
    }
    return make_json_success_response(data)

# 增
@handle_error_if_exist
def add_file_info():
    filename = get_post_param('filename', '', str)
    fileparent = get_post_param('fileparent', '', str)
    filepath = get_post_param('filepath', '', str)
    filetype = get_post_param('filetype', '', str)
    assert_param_is_none(filename, fileparent, filepath, filetype)
    if check_file_exist(filepath):
        raise FileManagerException(FileManagerErrorCode.ERROR_CODE_FILE_EXISTED)
    add_file(filename, fileparent, filepath, filetype)
    return make_json_success_response({})

# 删



# 改
@handle_error_if_exist
def rename():
    newname = get_post_param('newname', '', str)
    filepath = get_post_param('filepath', '', str)
    assert_param_is_none(newname, filepath)
    rename_file(filepath, newname)
    return make_json_success_response({})



# 查
@handle_error_if_exist
def get_dir_files(dirname):
    pass


def get_file_by_name(filename):
    pass







