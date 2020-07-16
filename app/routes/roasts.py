from flask import Blueprint, request
from ..models import db
from ..models.roasts import Roast

bp = Blueprint('roasts', __name__, url_prefix='/api/roasts')


@bp.route('<id>', methods=['POST'])
def postRoast(id):
    data = request.json
    print(data)
    roast = Roast(userId=id, name=data["name"], description=data["description"])
    db.session.add(roast)
    db.session.commit()
    return roast.to_dict()


@bp.route('<id>', methods=['PUT'])
def updateRoast(id):
    data = request.json
    print(data)
    roast = Roast.query.filter(Roast.id == id).first()
    roast.supplier = data["supplier"]
    roast.bean = data["bean"]
    roast.originId = data["originId"]
    roast.load = data["load"]
    roast.ambientTemp = data["ambientTemp"]
    db.session.commit()
    return roast.to_dict()
