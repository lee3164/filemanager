from flask import session
from dal import user_dal, group_dal


def login_with_name_password(name, pwd):
    code, user = user_dal.check_password_by_uname(name, pwd)
    if user is not None:
        session['uid'] = user.id
    return code


def add_user(dict):
    uname = dict.get('uname', '')
    usex = dict.get('usex', '')
    uemail = dict.get('uemail', '')
    ucomment = dict.get('ucomment', '')
    upwd = dict.get('upwd', '')
    group = group_dal.add_group(uname, uname)
    print locals()
    user_dal.add_user(group, uname, usex, uemail, upwd, ucomment)
