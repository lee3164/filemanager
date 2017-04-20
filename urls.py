from views.index import index, get_dir_files, add_dir, add_file, download_file
from views.user import login, add_user

urlpatterns = [
    ('/disk/home/', index, {'methods': ['GET']}),
    ('/disk/api/get_files_by_dir/', get_dir_files, {'methods': ['GET']}),
    ('/disk/api/dir/create/', add_dir, {'methods': ['POST']}),
    ('/disk/api/file/create/', add_file, {'methods': ['POST']}),
    ('/disk/api/file/download/', download_file, {'methods': ['GET']}),
    ('/disk/api/login/', login, {'methods': ['POST']}),
    ('/register/', add_user, {'methods': ['POST']})
]
