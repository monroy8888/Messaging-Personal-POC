from apiflask import APIBlueprint

bp = APIBlueprint('users', __name__, url_prefix="/users")

from app.controllers.user_controller import UserView
