from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Configuration
from app.models import db

from app.routes import roasts

app = Flask(__name__)
CORS(app)
app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(roasts.bp)
