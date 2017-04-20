from common.decorator import handle_error_if_exist
from common.error import FileManagerException, FileManagerErrorCode
from common.util import get_post_param, assert_param_is_none, make_json_success_response
from biz import user_biz

from flask import redirect, request


@handle_error_if_exist
def login():
    print request.form
    uname = get_post_param('user_name', '', str)
    upwd = get_post_param('user_password', '', str)
    print '==>', uname, upwd
    assert_param_is_none(uname, upwd)
    code = user_biz.login_with_name_password(uname, upwd)
    if code != FileManagerErrorCode.ERROR_CODE_OK:
        raise FileManagerException(code)
    return make_json_success_response()


@handle_error_if_exist
def add_user():
    uname = get_post_param('user_name', '', str)
    usex = get_post_param('user_sex', '', str)
    uemail = get_post_param('user_email', '', str)
    upwd = get_post_param('user_password', '', str)
    ucomment = get_post_param('user_comment', '', str)
    print locals()
    assert_param_is_none(uname, usex, uemail, upwd, ucomment)
    data = dict(uname=uname, usex=usex, uemail=uemail,
                upwd=upwd, ucomment=ucomment)
    user_biz.add_user(data)
    return make_json_success_response()
