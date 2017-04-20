from modules.file import File
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
