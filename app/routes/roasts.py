from flask import Blueprint, request
from ..models import db
from ..models.roasts import Roast
from ..models.users import User
from ..auth import require_auth

bp = Blueprint('roasts', __name__, url_prefix='/api/roasts')


@bp.route('/user/<id>')
@require_auth
def getRoasts(id):
    roasts = Roast.query.filter(Roast.userId == id).all()
    roasts_list = get_list(roasts)
    return {"roasts_list": roasts_list}

@bp.route('/<username>/<roastName>')
@require_auth
def get_roast(username, roastName):
    user = User.query.filter(User.username == username).first()
    roast = Roast.query.filter(Roast.userId == user.id).filter(Roast.name == roastName).first()
    roast_obj = roast.to_dict()
    roast_obj["timestamps"] = get_list(roast.timestamps)
    roast_obj["milestones"] = get_list(roast.milestones)
    roast_obj["notes"] = get_list(roast.notes)
    roast_obj["user"] = user.to_dict()
    return roast_obj


@bp.route('<id>', methods=['POST'])
@require_auth
def post_roast(id):
    data = request.json
    print(data)
    roast = Roast(userId=id, name=data["name"], description=data["description"])
    db.session.add(roast)
    db.session.commit()
    return roast.to_dict()


@bp.route('<id>', methods=['PUT'])
@require_auth
def update_roast(id):
    data = request.json
    roast = Roast.query.filter(Roast.id == id).first()
    values = ["supplier", "bean", "load", "ambientTemp",
              "originId", "firstCrack", "secondCrack", "totalTime"]

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


def get_list(query_nodes):
    dict_list = []
    for query in query_nodes:
        dict_list.append(query.to_dict())
    return dict_list
