from ..models import db
from sqlalchemy import func


class Timestamp(db.Model):
    __tablename__ = 'timestamps'

    id = db.Column(db.Integer, primary_key=True)
    roastId = db.Column(db.Integer, db.ForeignKey("roasts.id"), nullable=False)
    roastTemp = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True),
                           server_default=func.now(), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True),
                           server_default=func.now(), onupdate=func.now(),
                           nullable=False)

    roast = db.relationship('Roast', back_populates='timestamps')

    def to_dict(self):
        return {"id": self.id, "roastId": self.roastId, "timestamp": self.timestamp}
