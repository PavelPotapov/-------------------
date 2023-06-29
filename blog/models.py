from blog import db
import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    login = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    firstname = db.Column(db.String(255), nullable=False)
    secondname = db.Column(db.String(255), nullable=False)
    date_registration = db.Column(db.Date())
    avatar = db.Column(db.BLOB, nullable=True)  

    def __repr__(self) -> str:
        return 'User id {}, username {}'.format(self.id, self.username)

class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer(), primary_key=True)
    login = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    firstname = db.Column(db.String(255), nullable=False)
    secondname = db.Column(db.String(255), nullable=False)
    date_registration = db.Column(db.Date())
    avatar = db.Column(db.BLOB, nullable=True)  

    def __repr__(self) -> str:
        return 'User id {}, username {}'.format(self.id, self.username)





