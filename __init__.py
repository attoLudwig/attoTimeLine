from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

Timeline = Flask(__name__)
Timeline.config.from_object(Config)

db = SQLAlchemy(Timeline)
migrate = Migrate(Timeline, db)

from Timeline import models
