import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.engine import reflection

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    db_server = 'database-1.czlutn2hktjl.us-west-2.rds.amazonaws.com'
    db_port = 5432
    db_user = 'postgres'
    db_pw = os.environ['HERBERT_DB_PW']
    db_db = 'TestDB'

    app.config[
        'SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_pw}@{db_server}:{db_port}/{db_db}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}

    db.init_app(app)

    from .views import herb_views
    app.register_blueprint(herb_views.bp)

    from .views import home_views
    app.register_blueprint(home_views.bp)

    from .views import search
    app.register_blueprint(search.bp)

    return app
