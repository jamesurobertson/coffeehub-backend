import os
from flask import Flask, send_from_directory
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Configuration
from app.models import db

from app.routes import (users, explore, aws, roasts,
                        notes, session, timestamps, milestones)


if os.environ.get("FLASK_ENV") == 'production':
    app = Flask(__name__, static_folder='../client/build/static',
                static_url_path='/static')
else:
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


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print(f'caught_path: {path}')
    path_dir = os.path.abspath("./client/build")  # path react build

    if path and (os.path.exists(f'./client/build/static/{path}') or
                 os.path.exists(f'./client/build/{path}')):
        return send_from_directory(os.path.join(path_dir), path)
    else:
        return send_from_directory(os.path.join(path_dir), 'index.html')
