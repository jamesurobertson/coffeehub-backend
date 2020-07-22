from flask import Blueprint, request
from ..models import db
from ..models.roasts import Roast
from ..models.users import User
from ..models.timestamps import Timestamp
from ..auth import require_auth

bp = Blueprint('timestamps', __name__, url_prefix='/api/timestamps')


@bp.route('/<id>', methods=["POST"])
@require_auth
def post_timestamps(id):
    data = request.json
    timestamp = Timestamp(
        roastId=id, roastTemp=data["roastTemp"], timestamp=data["timestamp"])
    db.session.add(timestamp)
    db.session.commit()
    return timestamp.to_dict()
