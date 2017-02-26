from views.index import index, add_file_info, rename

urlpatterns = [
    ('/', index, {'methods': ['GET']}),
    ('/add', add_file_info, {'methods': ['GET']}),
    ('/rename', rename, {'methods': ['GET']})
]