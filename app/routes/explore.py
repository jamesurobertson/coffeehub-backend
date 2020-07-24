from flask import Blueprint, request
from sqlalchemy import or_
from ..models import db
from ..models.roasts import Roast
from ..models.users import User
from ..models.origins import Origin
from ..auth import require_auth
from ..utils import get_list

bp = Blueprint('explore', __name__, url_prefix='/api/explore')


@bp.route('/<search_param>')
@require_auth
def get_counts(user, search_param):
    roasts = Roast.query.filter(Roast.name.ilike(f'%{search_param}%')).count()
    users = User.query.filter(or_(User.username.ilike(f'%{search_param}%'), User.fullName.ilike(f'%{search_param}%'))).count()
    origins = Origin.query.filter(Origin.name.ilike(f'%{search_param}%')).all()
    origin_count = 0
    for origin in origins:
        origin_count += len(origin.roasts)

    return {"roasts": roasts, "users": users, "origins": origin_count}

@bp.route('/<search_type>/<search_param>')
@require_auth
def get_all(user, search_type, search_param):
    if search_type == 'roast':
        roasts = Roast.query.filter(Roast.name.ilike(f'%{search_param}%')).all()
        return {"list": get_list(roasts), "type": 'roast'}
    if search_type == 'user':
        users = User.query.filter(or_(User.username.ilike(f'%{search_param}%'), User.fullName.ilike(f'%{search_param}%'))).all()
        # num followers
        # num roasts

        return {"list": get_list(users), "type": 'user'}
    if search_type == 'origin':
        origins = Origin.query.filter(Origin.name.ilike(f'%{search_param}%')).all()
        roasts = []
        for origin in origins:
            roasts += get_list(origin.roasts)
        return {"list": roasts, "type": 'origin'}
