from ..models import db
from sqlalchemy import func


class Milestone(db.Model):
    __tablename__ = 'milestones'

    id = db.Column(db.Integer, primary_key=True)
    roastId = db.Column(db.Integer, db.ForeignKey('roasts.id'), nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)
    fanspeed = db.Column(db.Integer, nullable=False)
    heatLevel = db.Column(db.Integer, nullable=False)
    note = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True),
                          server_default=func.now(), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now(),
                          nullable=False)

    roast = db.relationship('Roast', back_populates='milestones')

    def to_dict(self):
        return {"id": self.id, "roastId": self.roastId, "timestamp": self.timestamp,
                "fanspeed": self.fanspeed, "heatLevel": self.heatLevel, "note": self.note}
