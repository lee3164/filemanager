from modules.file import User
from common.error import FileManagerErrorCode
from common.session import make_session

def make_user(uname, usex, uemail, upwd, ucomment):
    return User(uname=uname, usex=usex, uemail=uemail,
                upassword=upwd, ucomment=ucomment)


def check_password_by_uname(name, pwd):
    ret = None
    u =  User.query.filter(User.uname == name).first()
    if u == None:
        ret = FileManagerErrorCode.ERROR_CODE_USER_NOT_EXIST, None
    elif u.upassword != pwd:
        ret = FileManagerErrorCode.ERROR_CODE_PASSWORD_ERROR, None
    else:
        ret = FileManagerErrorCode.ERROR_CODE_OK, u
    return ret


def get_user_by_id(uid):
    ret = None
    u = User.query.filter(User.id == uid).first()
    if u == None:
        ret = FileManagerErrorCode.ERROR_CODE_USER_NOT_EXIST, None
    else:
        ret = FileManagerErrorCode.ERROR_CODE_OK, u
    return ret


def add_user(group, uname, usex, uemail, upwd, ucomment='no comment'):
    u = make_user(uname, usex, uemail, upwd, ucomment)
    u.group = [group]
    with make_session() as session:
        session.add(u)
        session.commit()