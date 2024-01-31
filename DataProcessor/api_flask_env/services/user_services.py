import os

from app.repositories.user_repositories import UserRepository
from app.models.app_models import Registro

from werkzeug.utils import secure_filename


class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    def get_user_service(self, user_id: int):
        data_user = self.user_repo.get_user(user_id)
        return data_user

    def post_register_service(self, form_data: dict, data_filename: str):
        name = form_data['nombre']
        description = form_data['descripcion']
        resume = form_data['resumen']
        urls = form_data['urls']

        new_register = Registro(nombre=name,
                                descripcion=description,
                                resumen=resume,
                                files=data_filename,
                                urls=urls)

        self.user_repo.post_register_repo(new_register)

    @staticmethod
    def save_file(files):
        path = os.path.join(os.path.dirname(__file__), 'uploads')
        data_filename = secure_filename(files.filename)
        files.save(os.path.join(path, data_filename))
        return data_filename
