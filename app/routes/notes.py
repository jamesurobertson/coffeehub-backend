from flask import Blueprint, request
from ..models import db
from ..models.notes import Note
from ..auth import require_auth

bp = Blueprint('notes', __name__, url_prefix='/api/notes')


@bp.route('/<id>', methods=["POST"])
@require_auth
def post_note(id, user):
    data = request.json
    print(data)
    if "timestamp" in data:
        note = Note(roastId=id, note=data["note"], timestamp=data["timestamp"])
    else:
        note = Note(roastId=id, note=data["note"])
    db.session.add(note)
    db.session.commit()
    return note.to_dict()
