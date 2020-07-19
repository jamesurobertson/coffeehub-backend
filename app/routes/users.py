from flask import Blueprint, request
from ..models import db
from ..models.follows import Follow
from ..models.cups import Cup
from ..models.users import User
from ..auth import require_auth
from ..utils import get_list
from ..utils import merge

bp = Blueprint('users', __name__, url_prefix='/api/users')


@bp.route('/<id>/feed')
@require_auth
def getRoasts(id):
    user = User.query.filter(User.id == id).first()
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
            roast_origin = cup.roast.origin.to_dict()
            roast_likes = len(cup.roast.cups)
            roast_dict["user"] = cup.roast.user.to_dict()
            roast_dict["origin"] = roast_origin
            roast_dict["numLikes"] = roast_likes

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
            f_user_followed_users.append(followed_user_dict)
        user_obj['followed_users'] = f_user_followed_users
        feed.append(user_obj)


    return {'feed': feed}


# {'id': 2, 'userId': 1, 'userFollowedId': 3}
