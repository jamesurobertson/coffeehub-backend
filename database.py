from app.models.comments import Comment
from app.models.cups import Cup
from app.models.follows import Follow
from app.models.milestones import Milestone
from app.models.origins import Origin
from app.models.roasts import Roast
from app.models.timestamps import Timestamp
from app.models.notes import Note
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

with app.app_context():
    db.drop_all()
    db.create_all()

    users = [User(email='jamesurobertson@gmail.com', fullName='James Robertson', username='jamesurobertson',
             password='password', profileImageUrl='https://randomuser.me/api/portraits/', bio='This is my bio. Enjoy my roasts :)'),
             User(email='dan1@gmail.com', fullName='Daniel Robertson', username='DanGR',
             password='password', profileImageUrl='https://randomuser.me/api/portraits/men/2.jpg', bio='This is Dans bio'),
             User(email='vic@gmail.com', fullName='Vic Robertson', username='vic3',
             password='password', profileImageUrl='https://randomuser.me/api/portraits/men/3.jpg', bio='This is Vics bio!!!')]

    origins = ['Colombia', 'Brazil', 'Peru', 'El Salvador', 'Costa Rica', 'Guatemala', 'Burundi', 'Ethiopia',
               'Rwanda', 'Congo', 'Sumatra', 'Flores', 'Java', 'Sulawesi', 'Timor', 'Papa New Guinea', 'Yemen']
    origins.sort()
    origins_list = []
    for origin in origins:
        origins_list.append(Origin(name=origin))

    roast = Roast(userId=1, name='first-roast', description='The firt roast on the site!', supplier='Sweet Marias', originId='1',
                  bean='Dipilto Finca La Laguna', ambientTemp=74, load=222, yieldNum=198, firstCrack='8:33', totalTime='10:03')

    timestamps = [
        Timestamp(roastId=1, roastTemp=380, timestamp=0),
        Timestamp(roastId=1, roastTemp=203, timestamp=.5),
        Timestamp(roastId=1, roastTemp=185, timestamp=1),
        Timestamp(roastId=1, roastTemp=197, timestamp=1.5),
        Timestamp(roastId=1, roastTemp=215, timestamp=2),
        Timestamp(roastId=1, roastTemp=230, timestamp=2.5),
        Timestamp(roastId=1, roastTemp=242, timestamp=3),
        Timestamp(roastId=1, roastTemp=255, timestamp=3.5),
        Timestamp(roastId=1, roastTemp=267, timestamp=4),
        Timestamp(roastId=1, roastTemp=280, timestamp=4.5),
        Timestamp(roastId=1, roastTemp=291, timestamp=5),
        Timestamp(roastId=1, roastTemp=303, timestamp=5.5),
        Timestamp(roastId=1, roastTemp=314, timestamp=6),
        Timestamp(roastId=1, roastTemp=325, timestamp=6.5),
        Timestamp(roastId=1, roastTemp=338, timestamp=7),
        Timestamp(roastId=1, roastTemp=350, timestamp=7.5),
        Timestamp(roastId=1, roastTemp=360, timestamp=8),
        Timestamp(roastId=1, roastTemp=370, timestamp=8.5),
        Timestamp(roastId=1, roastTemp=375, timestamp=9),
        Timestamp(roastId=1, roastTemp=380, timestamp=9.5),
    ]

    milestones = [
        Milestone(roastId=1, roastTemp=380, timestamp=0, heatLevel=0, fanspeed=0),
        Milestone(roastId=1, roastTemp=320, timestamp='', heatLevel=9, fanspeed=1),
        Milestone(roastId=1, roastTemp=340, timestamp='', heatLevel=8, fanspeed=2),
        Milestone(roastId=1, roastTemp=360, timestamp='', heatLevel=7, fanspeed=0),
        Milestone(roastId=1, roastTemp=370, timestamp='', heatLevel=5, fanspeed=3),
        Milestone(roastId=1, roastTemp=380, timestamp='', heatLevel=3, fanspeed=4)
    ]

    notes = [
        Note(roastId=1, note='Drop 1 minute and 30 seconds after First Crack')
    ]

    follows = [
        Follow(userId=1, userFollowedId=2),
        Follow(userId=1, userFollowedId=3),
    ]

    cups = [
        Cup(userId=2, roastId=1),
        Cup(userId=3, roastId=1)
    ]

    for user in users:
        db.session.add(user)

    for origin in origins_list:
        db.session.add(origin)

    db.session.add(roast)

    for timestamp in timestamps:
        db.session.add(timestamp)

    for milestone in milestones:
        db.session.add(milestone)

    for note in notes:
        db.session.add(note)

    for cup in cups:
        db.session.add(cup)

    for follow in follows:
        db.session.add(follow)

    db.session.commit()
