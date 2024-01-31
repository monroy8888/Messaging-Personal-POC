import logging
from sqlalchemy import select

from app.config.db import db
from app.models.app_models import Usuario, Registro


class UserRepository:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def get_user(self, user_id: int):
        data_user = select(Usuario).where(Usuario.id == user_id)
        user = db.session.execute(data_user).scalar()
        if user:
            return user.to_json()
        else:
            self.logger.warning(f"User with ID {user_id} not found.")
            return None

    def post_register_repo(self, register: Registro):
        db.session.add(register)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            self.logger.error(f"Error while committing registration: {e}")
