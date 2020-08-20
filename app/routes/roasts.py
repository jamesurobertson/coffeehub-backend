from flask import Blueprint, request
from ..models import db
from ..models.roasts import Roast
from ..models.users import User
from ..models.cups import Cup
from ..auth import require_auth
from ..utils import get_list

bp = Blueprint('roasts', __name__, url_prefix='/api/roasts')


@bp.route('')
@require_auth
def get_roasts(user):
    print(f'user: {user}')
    roasts = Roast.query.filter(Roast.userId == user.id).all()
    roasts_list = get_list(roasts)
    return {"roasts_list": roasts_list}


@bp.route('/initial')
@require_auth
def get6(user):
    print(f'user: {user}')
    roasts = Roast.query.filter(Roast.userId == user.id).limit(6)
    roasts_list = get_list(roasts)
    return {"roasts_list": roasts_list}


@bp.route('/<username>/<roastName>')
@require_auth
def get_roast(username, roastName, user):
    user = User.query.filter(User.username == username).first()
    roast = Roast.query.filter(Roast.userId == user.id).filter(Roast.name == roastName).first()
    roast_obj = roast.to_dict()
    roast_obj["timestamps"] = get_list(roast.timestamps)
    roast_obj["milestones"] = get_list(roast.milestones)
    roast_obj["notes"] = get_list(roast.notes)
    roast_obj["user"] = user.to_dict()
    return roast_obj


@bp.route('', methods=['POST', 'DELETE'])
@require_auth
def post_roast(user):
    data = request.json
    print(data)
    if request.method == 'POST':
        roast = Roast(userId=user.id, name=data["name"],
                      description=data["description"])
        db.session.add(roast)
    else:
        roast = Roast.query.filter(Roast.id == data["roastId"]).first()
        if roast.userId != user.id:
            return "Can not delete roasts that you did not create", 404

        nodes = roast.notes + roast.milestones + roast.timestamps + roast.cups + roast.comments
        for node in nodes:
            db.session.delete(node)

        db.session.delete(roast)

    db.session.commit()
    return roast.to_dict()


@bp.route('<id>', methods=['PUT'])
@require_auth
def update_roast(id, user):
    data = request.json
    roast = Roast.query.filter(Roast.id == id).first()

    if "supplier" in data:
        roast.supplier = data["supplier"]
    if "bean" in data:
        roast.bean = data["bean"]
    if "load" in data:
        roast.load = data["load"]
    if "ambientTemp" in data:
        roast.ambientTemp = data["ambientTemp"]
    if "originId" in data:
        roast.originId = data["originId"]
    if "firstCrack" in data:
        roast.firstCrack = data["firstCrack"]
    if "secondCrack" in data:
        roast.secondCrack = data["secondCrack"]
    if "totalTime" in data:
        roast.totalTime = data["totalTime"]

    db.session.commit()
    return roast.to_dict()


@bp.route('/cup/<id>', methods=["POST", "DELETE"])
@require_auth
def cup(id, user):
    if request.method == 'POST':
        cup = Cup(userId=user.id, roastId=id)
        db.session.add(cup)
    else:
        cup = Cup.query.filter(Cup.userId == user.id).filter(Cup.roastId == id).first()
        db.session.delete(cup)

    db.session.commit()
    return cup.to_dict()


@bp.route('/validate/<roast_name>')
@require_auth
def validate_roast_name(user, roast_name):
    print(roast_name)
    roast = Roast.query.filter(Roast.userId == user.id).filter(Roast.name == roast_name).first()
    print(roast)

    if roast:
        return 'false'
    else:
        return 'true'
