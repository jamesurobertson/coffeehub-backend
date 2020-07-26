from flask import Blueprint, request
import jwt
from ..config import Configuration
from ..models import db
from ..models.follows import Follow
from ..models.cups import Cup
from ..models.users import User
from ..models.follows import Follow
from ..auth import require_auth
from ..utils import get_list
from ..utils import merge

bp = Blueprint('users', __name__, url_prefix='/api/users')


@bp.route('')
@require_auth
def get_user(user):
    return user.to_dict()

@bp.route('/feed')
@require_auth
def getRoasts(user):
    followed_users = user.follows
    feed = []
    cups = []
    for followed in followed_users:
        f_user = User.query.filter(User.id == followed.userFollowedId).first()
        user_obj = f_user.to_dict()
        f_user_cups = f_user.cups
        f_user_cupped_roasts = []
        for cup in f_user_cups:
            roast_dict = cup.roast.to_dict()
            cup_time = cup.to_dict()["createdAt"]
            roast_origin = cup.roast.origin.to_dict() if cup.roast.origin else []
            roast_likes = len(cup.roast.cups)
            roast_dict["user"] = cup.roast.user.to_dict()
            roast_dict["origin"] = roast_origin
            roast_dict["numLikes"] = roast_likes
            roast_dict["cupTime"] = cup_time

            f_user_cupped_roasts.append(roast_dict)
        user_obj['cupped_roasts'] = f_user_cupped_roasts

        f_user_follows = f_user.follows
        f_user_followed_users = []
        for follow in f_user_follows:
            followed_user = User.query.filter(User.id == follow.userFollowedId).first()
            followed_user_dict = followed_user.to_dict()
            num_roasts = len(followed_user.roasts)
            num_followers = Follow.query.filter(Follow.userFollowedId == followed_user.id).count()
            followed_user_dict["numRoasts"] = num_roasts
            followed_user_dict["numFollowers"] = num_followers
            followed_user_dict["followTime"] = follow.to_dict()["createdAt"]
            f_user_followed_users.append(followed_user_dict)
        user_obj['followed_users'] = f_user_followed_users
        feed.append(user_obj)


    return {'feed': feed}


@bp.route('/<username>')
@require_auth
def getProfiledata(username, user):
    user = User.query.filter(User.username == username).first()
    user_dict = user.to_dict()
    roasts = get_list(user.roasts)
    user_dict["roasts"] = roasts
    followers = Follow.query.filter(Follow.userFollowedId == user.id).all()
    user_dict["following"] = get_list(user.follows)
    user_dict["followers"] = get_list(followers)
    return {"user": user_dict}

@bp.route('/follow/<username>', methods=['POST', 'DELETE'])
@require_auth
def follow(username, user):
    user_followed = User.query.filter(User.username == username).first()
    if request.method == 'POST':
        follow = Follow(userId=user.id, userFollowedId=user_followed.id)
        db.session.add(follow)
    else:
        follow = Follow.query.filter(Follow.userId == user.id).filter(Follow.userFollowedId == user_followed.id).first()
        db.session.delete(follow)

    db.session.commit()
    return follow.to_dict()

@bp.route('/validate/<username>')
@require_auth
def validate(user, username):
    if user.username == username:
        return 'true'

    user = User.query.filter(User.username == username).first()
    if user:
        return 'false'
    else:
        return 'true'


@bp.route('/update', methods=["PUT"])
@require_auth
def update_user(user):
    data = request.json
    if "email" in data and data["email"] != user.email:
        user.email = data["email"]
    if "fullName" in data:
        user.fullName = data["fullName"]
    if "username" in data and data["username"] != user.username:
        user.username = data["username"]
    if "bio" in data:
        user.bio = data["bio"]

    db.session.commit()
    access_token = jwt.encode({'email': user.email}, Configuration.SECRET_KEY)
    return {'token': access_token.decode('UTF-8'), 'user': user.to_dict()}
