from ..models import db
from sqlalchemy import func


class Roast(db.Model):
    __tablename__ = 'roasts'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    originId = db.Column(db.Integer, db.ForeignKey('origins.id'), nullable=False)
    coffeeSupplier = db.Column(db.String(100), nullable=False)
    load = db.Column(db.Integer, nullable=False)
    yieldNum = db.Column(db.Integer, nullable=False)
    firstCrack = db.Column(db.Integer)
    secondCrack = db.Column(db.Integer)
    totalTime = db.Column(db.Integer, nullable=False)
    abientTemp = db.Column(db.Integer, nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True),
                          server_default=func.now(), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now(),
                          nullable=False)

    origin = db.relationship('Origin', back_populates='roasts')
    user = db.relationship('User', back_populates='roasts')
    milestones = db.relationship('Milestone', back_populates='roast')
    timestamps = db.relationship('Timestamp', back_populates='roast')
    cups = db.relationship('Cup', back_populates='roast')
    comments = db.relationship('Comment', back_populates='roast')

    def to_dict(self):
        return {"id": self.id, "userId": self.userId, "originId": self.originId, "coffeeSupplier": self.coffeeSupplier,
                "load": self.load, "yieldNum": self.yieldNum, "firstCrack": self.firstCrack, "secondCrack": self.secondCrack,
                "totalTime": self.totalTime, "ambientTemp": self.ambientTemp }
