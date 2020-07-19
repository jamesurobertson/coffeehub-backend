from flask import Blueprint, request
from ..models import db
from ..models.notes import Note
from ..auth import require_auth

bp = Blueprint('notes', __name__, url_prefix='/api/notes')


@bp.route('/<id>', methods=["POST"])
@require_auth
def post_note(id):
    data = request.json
    note = Note(roastId=id, timestamp=data["timestamp"], note=data["note"])
    db.session.add(note)
    db.session.commit()
    return note.to_dict()
