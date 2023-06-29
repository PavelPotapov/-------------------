from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()


from flask import Flask
from .admin.admin import admin

print("ИНИЦИАЛИЗИРУЕМ БЛОГ")

naming_convention = {
"ix": 'ix_%(column_0_label)s',
"uq": "uq_%(table_name)s_%(column_0_name)s",
"ck": "ck_%(table_name)s_%(column_0_name)s",
"fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
"pk": "pk_%(table_name)s"
}

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'afiqwerfijqe1231vwf'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.register_blueprint(admin, url_prefix='/admin')
    db.init_app(app)
    with app.app_context():
        if db.engine.url.drivername == 'sqlite':
            migrate.init_app(app, db, render_as_batch=True)
        else:
            migrate.init_app(app, db)

    return app

