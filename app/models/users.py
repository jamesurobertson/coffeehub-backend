from ..models import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import func
from sqlalchemy.orm import validates
from ..utils import get_list


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    fullName = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False, unique=True)
    hashedPassword = db.Column(db.String(128), nullable=False)
    profileImageUrl = db.Column(db.String(255))
    bio = db.Column(db.String(2000))
    createdAt = db.Column(db.DateTime(timezone=True),
                          server_default=func.now(), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now(),
                          nullable=False)

    follows = db.relationship('Follow', back_populates='user')
    comments = db.relationship('Comment', back_populates='user')
    cups = db.relationship('Cup', back_populates='user')
    roasts = db.relationship('Roast', back_populates='user')


    @validates('username', 'email')
    def validate_username(self, key, value):
        if key == 'username':
            if not value:
                raise AssertionError('Must provide a username!')
            if User.query.filter(User.username == value).first():
                raise AssertionError('Username already exists!')
        if key == 'email':
            if not value:
                raise AssertionError('Must provide an email!')
            if User.query.filter(User.email == value).first():
                raise AssertionError('Email already exists!')

        return value

    @property
    def password(self):
        return self.hashedPassword

    @password.setter
    def password(self, password):
        self.hashedPassword = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashedPassword, password)

    def to_dict(self):
        return {"id": self.id, "email": self.email, "fullName": self.fullName, "username": self.username,
                "profileImageUrl": self.profileImageUrl, "following": get_list(self.follows),
                "bio": self.bio, "cups": get_list(self.cups)}
