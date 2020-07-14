from ..models import db
from sqlalchemy import func


class Origin(db.Model):
    __tablename__ = 'origins'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True),
                          server_default=func.now(), nullable=False)
    updatedAt = db.Column(db.DateTime(timezone=True),
                          server_default=func.now(), onupdate=func.now(),
                          nullable=False)

    roasts = db.relationship('Roast', back_populates='origin')

    def to_dict(self):
        return {"id": self.id, "name": self.name}
