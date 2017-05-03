from modules.file import File, FileMD5
from common.error import FileManagerErrorCode as ErrorCode
from common.session import make_session
import datetime


def get_file_by_id(fid):
    return File.query.filter(File.id == fid).first()


def get_file_by_name(fname):
    ret = None
    if fname != '/':
        idx = fname.rindex('/')
        fname = fname[idx + 1:]

    f = File.query.filter(File.fname == fname).first()
    if f == None:
        ret = ErrorCode.ERROR_CODE_FILE_NOT_EXIST, None
    else:
        ret = ErrorCode.ERROR_CODE_OK, f
    return ret


def get_files_by_dir(dirname, uid):
    arr = []
    files = File.query.filter(File.fparent == dirname).filter(File.uid == uid).all()
    for f in files:
        arr.append(f.to_json())
    return arr


def rename(fid, new_name):
    file = File.query.filter(File.id == fid).first()
    file.fname = new_name
    file.fmtime = datetime.datetime.now()
    with make_session() as session:
        session.add(file)


def get_file_link(fid):
    file = File.query.filter(File.id == fid).first()
    if file is None:
        raise
    return file.flink


def move_file(fid, new_parent):
    file = get_file_by_id(fid)
    file.fparent = new_parent
    with make_session() as session:
        session.add(file)


def copy_file(fid, parent):
    file = get_file_by_id(fid)
    params = {
        'fname': file.fname,
        'fparent': parent,
        'ftype': file.ftype,
        'fmode': file.fmode,
        'fcomment': file.fcomment,
        'flink': file.flink,
        'uid': file.uid,
        'gid': file.gid
    }
    return create_file(**params)


def create_file(**params):
    model = File()
    fname = model.fname = params.pop('fname')
    fparent = model.fparent = params.pop('fparent')
    model.ftype = params.pop('ftype')
    model.fmode = params.pop('fmode')
    model.fcomment = params.pop('fcomment')
    model.flink = params.pop('flink')
    model.uid = params.pop('uid')
    model.gid = params.pop('gid')
    with make_session() as session:
        session.add(model)

    obj = File.query.filter(File.fname == fname).filter(File.fparent == fparent).first()
    return obj.to_json()


def get_file_md5(md5):
    item = FileMD5.query.filter(FileMD5.md5 == md5).first()
    if not item:
        return {
            'file_link': ''
        }
    else:
        return {
            'file_link': item.fname
        }


def insert_file_md5(fname, md5):
    item = FileMD5()
    item.fname = fname
    item.md5 = md5
    with make_session() as session:
        session.add(item)


def _delete_dir(fid, session):
    item = session.query(File).filter(File.id == fid).first()
    dir_path = item.fparent + item.fname
    children = session.query(File).filter(File.fparent == dir_path).all()
    for child in children:
        if child.ftype == 'r':
            session.delete(child)
        else:
            _delete_dir(child.fid, session)
    session.delete(item)


def delete_dir_file(fid):
    with make_session() as session:
        _delete_dir(fid, session)


def delete_regular_file(fid):
    with make_session() as session:
        item = session.query(File).filter(File.id == fid).first()
        session.delete(item)
