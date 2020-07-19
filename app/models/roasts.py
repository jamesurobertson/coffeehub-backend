from ..models import db
from sqlalchemy import func


class Roast(db.Model):
    __tablename__ = 'roasts'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1000))
    supplier = db.Column(db.String(100))
    originId = db.Column(db.Integer, db.ForeignKey('origins.id'))
    bean = db.Column(db.String(50))
    ambientTemp = db.Column(db.Float)
    load = db.Column(db.Float)
    yieldNum = db.Column(db.Float)
    firstCrack = db.Column(db.String)
    secondCrack = db.Column(db.String)
    totalTime = db.Column(db.String(10))
    createdAt = db.Column(db.DateTime(timezone=True),
                          server_default=func.now(), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now(),
                          nullable=False)

    origin = db.relationship('Origin', back_populates='roasts')
    user = db.relationship('User', back_populates='roasts')
    milestones = db.relationship('Milestone', back_populates='roast')
    notes = db.relationship('Note', back_populates='roast')
    timestamps = db.relationship('Timestamp', back_populates='roast')
    cups = db.relationship('Cup', back_populates='roast')
    comments = db.relationship('Comment', back_populates='roast')

    def to_dict(self):
        return {"id": self.id, "userId": self.userId,
                "name": self.name, "description": self.description,
                "supplier": self.supplier, "originId": self.originId,
                "bean": self.bean, "ambientTemp": self.ambientTemp,
                "load": self.load, "yieldNum": self.yieldNum,
                "firstCrack": self.firstCrack, "secondCrack": self.secondCrack,
                "totalTime": self.totalTime, "createdAt": self.createdAt}
