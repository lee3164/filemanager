from views.index import index, get_dir_files

urlpatterns = [
    ('/', index, {'methods': ['GET']}),
    ('/get_files_by_dir', get_dir_files, {'methods': ['GET']}),
]