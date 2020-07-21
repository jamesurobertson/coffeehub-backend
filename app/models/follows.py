from ..models import db
from sqlalchemy import func
from ..models.users import User

class Follow(db.Model):
    __tablename__ = 'follows'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    userFollowedId = db.Column(db.Integer, nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True),
                          server_default=func.now(), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now(),
                          nullable=False)

    user = db.relationship('User', back_populates='follows')

    def userFollowed(self):
        return User.query.filter(User.id == self.userFollowedId).first().to_dict()

    def to_dict(self):
        return {"id": self.id, "userId": self.userId, "userFollowed": self.userFollowed(),
                "userFollowedId": self.userFollowedId}
