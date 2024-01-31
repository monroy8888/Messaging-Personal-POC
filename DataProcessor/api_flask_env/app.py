from apiflask import APIFlask
from flask_cors import CORS
from flask_migrate import Migrate

from app.config.db import db
from app.config import config
from app.routes.app_routes import bp

config_name = 'development'
app = APIFlask(__name__)
CORS(app)
app.config.from_object(config.configuration[config_name])
app.register_blueprint(bp)
migrate = Migrate(app, db)

db.init_app(app)
