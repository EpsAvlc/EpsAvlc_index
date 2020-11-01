import os 
from flask import Flask, url_for, redirect
from flask_bootstrap import Bootstrap

from datetime import timedelta 

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    Bootstrap(app)
    # app.send_file_max_age_default = timedelta(seconds=1)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass

    from . import index
    app.register_blueprint(index.bp)

    from . import fund
    app.register_blueprint(fund.bp)

    @app.route('/')
    def index_page():
        index_url = url_for('index.create')
        return redirect(index_url)


    return app