from flask import  Flask
from flask_cors import CORS

from urls import urlpatterns as patterns
from modules import config_db_with_app
from settings import load_config

def register_urls(app, patterns):
    for pattern in patterns:
        assert len(pattern) > 1
        options = {}
        if (len(pattern) == 3):
            path, view_func, options = pattern
        else:
            path, view_func = pattern
        app.add_url_rule(path, view_func=view_func, **options)

def init_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(load_config())
    print app.config['DATABASE_PATH']
    register_urls(app, patterns)
    config_db_with_app(app)
    return app
