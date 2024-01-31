from http import HTTPStatus

from apiflask.views import MethodView

from app import bp
from app.schemas.user_schema import Usuario, Eventos, Tarifas, RegistroIn
from app.services.user_services import UserService


# MethodView
class Hello(MethodView):

    def get(self):
        return {'message': 'Hello!'}


class UserView(MethodView):

    def __init__(self):
        self.user_service = UserService()

    def get(self, user_id: int):
        data_user = self.user_service.get_user_service(user_id)
        return {
            "code": HTTPStatus.OK,
            "data": {
                "user_id": data_user
            }
        }


user_service = UserService()


# Decorators
@bp.get('/get_data/<int:user_id>')
def get_data(user_id):
    data_user = user_service.get_user_service(user_id)
    return {
        "code": HTTPStatus.OK,
        "data": {
            "user_id": data_user
        }
    }


@bp.post('/register')
@bp.input(RegistroIn, location='form_and_files')
def post_register(form_and_files):
    try:
        RegistroIn.files_validator(form_and_files['files'])
    except ValueError as e:
        return {
            "code": HTTPStatus.BAD_REQUEST,
            "message": str(e)
        }
    files = form_and_files['files']
    data_filename = user_service.save_file(files)
    user_service.post_register_service(form_and_files, data_filename)

    return {
        "code": HTTPStatus.OK,
        "message": "Cause registered."
    }
