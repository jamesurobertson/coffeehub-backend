import os
import boto3
import time
from flask import Blueprint, request
from ..models import db
from ..models.users import User
from ..auth import require_auth

bp = Blueprint("aws", __name__, url_prefix="/api/aws")

UPLOAD_FOLDER = 'uploads'
BUCKET = 'slickpics'


@bp.route('/upload', methods=["POST"])
@require_auth
def upload(user):
    f = request.files['file']
    f.filename = change_name(f.filename)
    f.save(os.path.join(UPLOAD_FOLDER, f.filename))
    upload_file(f"uploads/{f.filename}", BUCKET)
    user.profileImageUrl = f'https://slickpics.s3.us-east-2.amazonaws.com/uploads/{f.filename}'
    db.session.commit()
    return {"img": f'https://slickpics.s3.us-east-2.amazonaws.com/uploads/{f.filename}'}



def upload_file(file_name, bucket):
    """
    Function to upload a file to an S3 bucket
    """
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response


def change_name(file_name):
    return f"{time.ctime().replace(' ', '').replace(':', '')}.png"
