from ..models import db
from sqlalchemy import func


class Cup(db.Model):
    __tablename__ = 'cups'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    roastId = db.Column(db.Integer, db.ForeignKey('roasts.id'), nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True),
                          server_default=func.now(), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now(),
                          nullable=False)

    user = db.relationship('User',back_populates='cups')
    roast = db.relationship('Roast', back_populates='cups')

    def to_dict(self):
        return {"id": self.id, "userId": self.userId, "roastId": self.roastId}
