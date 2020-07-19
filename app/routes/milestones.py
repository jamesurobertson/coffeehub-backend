from flask import Blueprint, request
from ..models import db
from ..models.milestones import Milestone
from ..auth import require_auth

bp = Blueprint('milestones', __name__, url_prefix='/api/milestones')


@bp.route('/<id>', methods=["POST"])
@require_auth
def post_milestone(id):
    data = request.json
    milestone = Milestone(roastId=id, timestamp=data["timestamp"], fanspeed=data["fanSpeed"], heatLevel=data["heatLevel"])
    db.session.add(milestone)
    db.session.commit()
    return milestone.to_dict()
