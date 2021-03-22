"""Models for bekah mccurry website."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Project(db.Model):
    """A project"""

    __tablename__ = 'projects'

    # user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # fname = db.Column(db.String)
    # lname = db.Column(db.String)
    # user_email = db.Column(db.String, unique=True)
    # zip_code = db.Column(db.Integer)
    # password = db.Column(db.String)

    # profile = db.relationship('Profile')

    # def __repr__(self):
    #     return f'<User user_id={self.user_id} email={self.user_email}>'


def connect_to_db(flask_app, db_uri='postgresql:///projects', echo=True): #///projects'... check this out
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)