# -*- coding: utf-8 -*-
from common.util import get_post_param, make_json_success_response, assert_param_is_none
from common.decorator import handle_error_if_exist, require_login, check_permission
from common.error import FileManagerException, FileManagerErrorCode
from common.file import get_files_by_dir, get_file_info_by_name
from biz import file_biz
from flask import render_template, send_from_directory


def index():
    return render_template('filemanager/index.html')


# 增
@handle_error_if_exist
@require_login
def add_dir():
    dirname = get_post_param('dir_name', '', str)
    dirparent = get_post_param('parent_dir', '', str)
    mode = get_post_param('file_mode', '', str)
    comment = get_post_param('file_comment', '', str)
    assert_param_is_none(dirname, dirparent, mode, comment)
    data = file_biz.add_file(dirname, dirparent, mode, comment, 'd')
    return make_json_success_response(data)


@handle_error_if_exist
@require_login
def add_file():
    dirname = get_post_param('file_name', '', str)
    dirparent = get_post_param('parent_dir', '', str)
    mode = get_post_param('file_mode', '', str)
    comment = get_post_param('file_comment', '', str)
    file_link = get_post_param('real_name', '', str)
    assert_param_is_none(dirname, dirparent, mode, comment)
    data = file_biz.add_file(dirname, dirparent, mode, comment, 'r', file_link)
    return make_json_success_response(data)


# 删



# 改
@handle_error_if_exist
@require_login
@check_permission
def rename():
    fid = get_post_param('fid', -1, int)
    name = get_post_param('new_name', '', str)
    assert fid != -1, 'require param: fid'
    assert name != '', 'require param: new_name'
    file_biz.rename(fid, name)


# 查
@handle_error_if_exist
@require_login
def get_dir_files():
    dirname = get_post_param('dir_name', '', str)
    assert_param_is_none(dirname)
    data = file_biz.get_files_by_dir(dirname)
    return make_json_success_response(data)


@handle_error_if_exist
@require_login
def download_file():
    fid = get_post_param('fid', '', str)
    assert fid, 'fid is null'
    flink = file_biz.get_file_link(fid)
    return send_from_directory('/Users/lxy-mac/Workbench/test/', 'test.py', as_attachment=True)
