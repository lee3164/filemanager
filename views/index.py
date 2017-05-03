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
    md5 = get_post_param('md5', '', str)
    assert_param_is_none(dirname, dirparent, mode, comment)
    data = file_biz.add_file(dirname, dirparent, mode, comment, 'r', file_link, md5)
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


@handle_error_if_exist
@require_login
def move():
    fid = get_post_param('file_id', 0, int)
    did = get_post_param('dir_id', 0, int)
    assert fid != 0, 'file_id is required'
    assert did != 0, 'did is required'
    file_biz.move_file(fid, did)
    return make_json_success_response({})


@handle_error_if_exist
@require_login
def copy():
    fid = get_post_param('file_id', 0, int)
    did = get_post_param('dir_id', 0, int)
    assert fid != 0, 'file_id is required'
    assert did != 0, 'did is required'
    data = file_biz.copy_file(fid, did)
    return make_json_success_response(data)


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
    fid = get_post_param('fid', 0, int)
    assert fid, 'fid is null'
    flink = file_biz.get_file_link(fid)
    response = send_from_directory('/home/lxy/Files', flink, as_attachment=True)
    response.headers['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8080'
    response.headers['Access-Control-Allow-Credentials'] = "true"
    return response


@handle_error_if_exist
@require_login
def check_file_md5():
    md5 = get_post_param('md5', '', str)
    assert md5, 'md5 is null'
    data = file_biz.get_file_md5(md5)
    return make_json_success_response(data)


@handle_error_if_exist
@require_login
def remove():
    fid = get_post_param('fid', 0, int)
    assert fid, 'fid is null'
    file_biz.delete_file(fid)
    return make_json_success_response({})