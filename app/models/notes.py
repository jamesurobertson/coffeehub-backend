from ..models import db
from sqlalchemy import func


class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    roastId = db.Column(db.Integer, db.ForeignKey('roasts.id'), nullable=False)
    note = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.String(20))
    createdAt = db.Column(db.DateTime(timezone=True),
                          server_default=func.now(), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now(),
                          nullable=False)

    roast = db.relationship('Roast', back_populates='notes')

    def to_dict(self):
        return {"id": self.id, "roastId": self.roastId,
                "note": self.note, "timestamp": self.timestamp}
