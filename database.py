from app.models.comments import Comment
from app.models.cups import Cup
from app.models.follows import Follow
from app.models.milestones import Milestone
from app.models.origins import Origin
from app.models.roasts import Roasts
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



    for follow in follows:
        db.session.add(follow)

    db.session.commit()
