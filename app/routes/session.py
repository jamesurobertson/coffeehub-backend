from flask import Blueprint, request
import jwt
from ..models import db
from ..config import Configuration

from ..models.users import User
from ..auth import require_auth

bp = Blueprint('session', __name__, url_prefix='/api/session')

@bp.route('/login', methods=["POST"])
def login():
    data = request.json
    user = User.query.filter(User.email == data['usernameEmail']).first()

    if not user:
        user = User.query.filter(User.username == data['usernameEmail']).first()

        if not user:
            return {"message": "Incorrect username or password."}, 422

    if user.check_password(data["password"]):
        access_token = jwt.encode({'email': user.email}, Configuration.SECRET_KEY)
        return {'token': access_token.decode('UTF-8'), 'user': user.to_dict()}
    else:
        return {"message": "Incorrect username or password."}, 422


@bp.route('/signup', methods=["POST"])
def signup():
    data = request.json
    print(data)
    user = User(email=data["email"], username=data["username"],
                fullName=data["fullName"], password=data["password"])
    db.session.add(user)
    db.session.commit()
    access_token = jwt.encode({'email': user.email}, Configuration.SECRET_KEY)
    return {'token': access_token.decode('UTF-8'), 'user': user.to_dict()}


@bp.route('/validateuser/<username>')
def validate_user(username):
    user = User.query.filter(User.username == username).first()
    if user:
        return 'false'
    else:
        return 'true'


@bp.route('/validateemail/<email>')
def validate_email(email):

    user = User.query.filter(User.email == email).first()
    if user:
        return 'false'
    else:
        return 'true'
