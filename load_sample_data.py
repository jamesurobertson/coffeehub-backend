from app.models.comments import Comment
from app.models.cups import Cup
from app.models.follows import Follow
from app.models.milestones import Milestone
from app.models.origins import Origin
from app.models.roasts import Roast
from app.models.timestamps import Timestamp
from app.models.notes import Note
from app.models.users import User
import math
from app import app, db
from faker import Faker
from random import randint, choice
from dotenv import load_dotenv
import datetime
load_dotenv()


fake = Faker()
defaultPic = 'https://randomuser.me/api/portraits/'
# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.

with app.app_context():
    db.drop_all()
    db.create_all()

    users = [User(email='jamesurobertson@gmail.com', fullName='James Robertson', username='jamesurobertson',
                  password='password', profileImageUrl='https://slickpics.s3.us-east-2.amazonaws.com/uploads/FriJul242125202020.png', bio='This is my bio. Enjoy my roasts :)')]

    for i in range(1,15):
        name = fake.name()
        username = f"{name.replace(' ', '')}{randint(1,1000)}"
        email = f'{username}@coffeehub.com'
        men_or_women = 'men' if randint(1,2) % 2 == 0 else 'women'
        userPic = f'{defaultPic}{men_or_women}/{i}.jpg'
        user = User(fullName=name, username=username, password='password',
                    email=email, profileImageUrl=userPic, bio=fake.text())
        users.append(user)

    origins = ['Colombia', 'Brazil', 'Peru', 'El Salvador', 'Costa Rica', 'Guatemala', 'Burundi', 'Ethiopia',
               'Rwanda', 'Congo', 'Sumatra', 'Flores', 'Java', 'Sulawesi', 'Timor', 'Papa New Guinea', 'Yemen']

    suppliers = ['Sweet Marias', 'Mill City Roasts', 'Klatch Coffee', 'Bean Green', 'BeanBay', 'Ministry Grounds Coffee', 'Mountaintop Coffee', 'Green Beanery', 'North Country Roasters']

    origins.sort()
    origins_list = []
    for origin in origins:
        origins_list.append(Origin(name=origin))

    roasts = [Roast(userId=1, name='first-roast', description='The first roast on the site!', supplier='Sweet Marias', originId='1',
                  bean='Dipilto Finca La Laguna', ambientTemp=74, load=222, yieldNum=198, firstCrack='8:33', totalTime='10:03')]

    for j in range(1, len(users)):
        numRoasts = randint(3, 10)
        for i in range(1, numRoasts):
            origin_id = randint(1, 17)
            origin = choice(origins)
            name = f'{origins[origin_id -1]}{randint(1,1000)}'
            load = randint(180, 250)
            firstCrackMin = randint(6, 12)
            firstCrackSec = randint(10, 59)
            load1 = load - math.floor(load * .1)
            load2 = load - math.floor(load * .2)
            totalTime = f'{firstCrackMin + randint(1,2)}:{firstCrackSec + randint(1,30) if firstCrackSec < 29 else firstCrackSec}'
            year = randint(2019, 2020)
            date = datetime.datetime(year, randint(7,12) if year == 2019 else randint(1, 7), randint(1,28))

            roast = Roast(userId=j + 1, name=name, description=fake.text(), supplier=choice(suppliers),
                          originId=origin_id, bean=origin, ambientTemp=randint(65, 80), load=load,
                          yieldNum=randint(load2, load1), firstCrack=f'{firstCrackMin}:{firstCrackSec}',
                          totalTime=totalTime, createdAt=date)
            roasts.append(roast)

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

    for i in range(1, len(roasts[1:])):
        parts = roasts[i].totalTime.split(':')
        minutes = parts[0]
        seconds = parts[1]
        total = (int(minutes) * 2) + 1 if int(seconds) > 30 else (int(minutes) * 2)
        roast_start = randint(300, 380)
        roast_mid = math.floor(randint(roast_start * 5, roast_start * 6) / 10)
        roast_bottom = roast_mid - randint(50, 90)
        highest_temp = randint(380, 410)
        increments = [math.floor(roast_bottom + (i *((highest_temp - roast_bottom) / total))) for i in range(3, total)]
        increments = [roast_start, roast_mid, roast_bottom] + increments
        times = [i/2 for i in range(0, total)]
        for j in range(0, total):
            timestamp = Timestamp(roastId= i + 1, roastTemp=increments[j], timestamp=times[j])
            timestamps.append(timestamp)


    milestones = [
        Milestone(roastId=1, roastTemp=380,
                  timestamp=0, heatLevel=0, fanspeed=0),
        Milestone(roastId=1, roastTemp=320,
                  timestamp='', heatLevel=9, fanspeed=1),
        Milestone(roastId=1, roastTemp=340,
                  timestamp='', heatLevel=8, fanspeed=2),
        Milestone(roastId=1, roastTemp=360,
                  timestamp='', heatLevel=7, fanspeed=0),
        Milestone(roastId=1, roastTemp=370,
                  timestamp='', heatLevel=5, fanspeed=3),
        Milestone(roastId=1, roastTemp=380,
                  timestamp='', heatLevel=3, fanspeed=4)
    ]

    for i in range(1, len(roasts)):
        roast = roasts[i]
        temps = [320, 340, 360, 370, 380]
        for j in range(1, len(temps)):
            milestone = Milestone(roastId = i + 1, roastTemp=temps[j], fanspeed=randint(0,4), heatLevel=randint(0,10))
            milestones.append(milestone)




    notes = [
        Note(roastId=1, note='Charge at 380 degrees. Enery and Fan off for 1 minute and then Energy 100% until 320 degrees'),
        Note(roastId=1, note='Drop 1 minute and 30 seconds after First Crack')
    ]

    for i in range(1, len(roasts)):
        roast = roasts[i]
        for j in range(1, 3):
            note = Note(roastId = i, note= fake.text())
            notes.append(note)


    follows = [
        Follow(userId=1, userFollowedId=2),
        Follow(userId=1, userFollowedId=3),
    ]

    for i in range(1, len(users)):
        user = users[i]
        followed_set = set()
        num_follows = randint(5, 10)
        while len(followed_set) < num_follows:
            user_followed = randint(1, len(users))
            if user_followed == i:
                continue
            followed_set.add(user_followed)
        for j in followed_set:
            year = randint(2019, 2020)
            date = datetime.datetime(year, randint(7,12) if year == 2019 else randint(1, 7), randint(1,28))
            follows.append(Follow(userId=i, userFollowedId=j, createdAt=date))


    cups = [
        Cup(userId=2, roastId=1),
        Cup(userId=3, roastId=1)
    ]

    for i in range(1, len(roasts)):
        roast = roasts[i]
        cupped_set = set()
        num_cupped = randint(5, 14)
        while len(cupped_set) < num_cupped:
            user_cupped = randint(1, len(users))
            cupped_set.add(user_cupped)
        for j in cupped_set:
            year = randint(2019, 2020)
            date = datetime.datetime(year, randint(7,12) if year == 2019 else randint(1, 7), randint(1,28))
            cups.append(Cup(userId=j, roastId=i, createdAt=date))

    for user in users:
        db.session.add(user)

    for origin in origins_list:
        db.session.add(origin)

    for roast in roasts:
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
