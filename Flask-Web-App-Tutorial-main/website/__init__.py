from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note, Drone, Drone_Log
    
    with app.app_context():
        db.create_all()
        drone1 = Drone(name="Drone 1", status="Available")
        drone2 = Drone(name="Drone 2", status="Available")
        drone3 = Drone(name="Drone 3", status="Available")
        drone4 = Drone(name="Drone 4", status="Available")
        db.session.add(drone1)
        db.session.add(drone2)
        db.session.add(drone3)
        db.session.add(drone4)
        db.session.commit()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
