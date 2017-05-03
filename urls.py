from views.index import get_dir_files, add_dir, add_file, download_file, \
    copy, move, check_file_md5, remove
from views.user import login, add_user

urlpatterns = [
    ('/disk/api/dir/get/', get_dir_files, {'methods': ['GET']}),
    ('/disk/api/dir/create/', add_dir, {'methods': ['POST']}),
    ('/disk/api/file/create/', add_file, {'methods': ['POST']}),
    ('/disk/api/file/download/', download_file, {'methods': ['GET']}),
    ('/disk/api/file/copy/', copy, {'methods': ['GET']}),
    ('/disk/api/file/move/', move, {'methods': ['GET']}),
    ('/disk/api/file/remove/', remove, {'methods': ['GET']}),
    ('/disk/api/file/md5/', check_file_md5, {'methods': ['GET']}),
    ('/disk/api/login/', login, {'methods': ['POST']}),
    ('/register/', add_user, {'methods': ['POST']})
]
