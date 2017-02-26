from modules.file import Files
from modules import Session


def add_file(filename, fileparent, filepath, filetype):
    session = Session()
    try:
        session.add(Files(filename=filename, fileparent=fileparent,
                          filepath=filepath, filetype=filetype))
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def rename_file(filepath, newname):
    file = _get_file(filepath)
    file.filename = newname
    file.filepath = filepath[:filepath.rfind('/') + 1] + newname
    session = Session()
    try:
        session.add(file)
        session.commit()
    except Exception, err:
        print 'err', err
        session.rollback()
        raise
    finally:
        session.close()


def _get_file(filepath):
    file = Files.query.filter(Files.filepath == filepath)
    assert file is not None, 'file is not exist'
    return file

def get_dir_files(dirname):
    files = Files.query.filter(Files.fileparent == dirname)
    ret = []
    if files is not None:
        for file in files:
            ret.append(file.to_json())
    return ret

def check_file_exist(filepath):
    file = Files.query.filter(Files.filepath == filepath)
    if file == None or file == []:
        return False
    return True
