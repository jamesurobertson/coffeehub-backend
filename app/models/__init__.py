from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from . import (comments, cups, follows, milestones, origins, roasts, timestamps, notes, users)
