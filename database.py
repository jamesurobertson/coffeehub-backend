from app.models.comments import Comment
from app.models.cups import Cup
from app.models.follows import Follow
from app.models.milestones import Milestone
from app.models.origins import Origin
from app.models.roasts import Roast
from app.models.timestamps import Timestamp
from app.models.users import User

from app import app, db
from faker import Faker
from random import *
from dotenv import load_dotenv
load_dotenv()


fake = Faker()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.

defaultPic = 'https://randomuser.me/api/portraits/'

with app.app_context():
    db.drop_all()
    db.create_all()

    origins = ['Columbia', 'Brazil', 'Peru', 'El Salvador', 'Costa Rica', 'Guatemala', 'Burundi', 'Ethiopia', 'Rwanda', 'Congo', 'Sumatra', 'Flores', 'Java', 'Sulawesi', 'Timor', 'Papa New Guinea', 'Yemen']
    origins.sort()

    origins_list = []
    for origin in origins:
        origins_list.append(Origin(name=origin))


    for origin in origins_list:
        db.session.add(origin)

    db.session.commit()
