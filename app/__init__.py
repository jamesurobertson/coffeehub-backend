from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Configuration
from app.models import db

from app.routes import users, explore, aws, roasts, notes, session, timestamps, milestones

app = Flask(__name__)
CORS(app)
app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(roasts.bp)
app.register_blueprint(session.bp)
app.register_blueprint(timestamps.bp)
app.register_blueprint(milestones.bp)
app.register_blueprint(notes.bp)
app.register_blueprint(users.bp)
app.register_blueprint(aws.bp)
app.register_blueprint(explore.bp)
