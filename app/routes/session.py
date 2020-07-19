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
    user = User.query.filter(User.email == data['email']).first()
    if not user:
        return {"message": "Email or Password incorrect"}, 422

    if user.check_password(data["password"]):
        access_token = jwt.encode({'email': user.email}, Configuration.SECRET_KEY)
        return {'token': access_token.decode('UTF-8'), 'user': user.to_dict()}
    else:
        return {"message": "Email or Password incorrect"}, 422
