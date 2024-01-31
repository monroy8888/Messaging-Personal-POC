from app.controllers.user_controller import UserView, Hello
from app import bp

# User routes:
bp.add_url_rule('/', view_func=Hello.as_view('hello'))
bp.add_url_rule('/<int:user_id>', view_func=UserView.as_view("user-view"))

# Event routes:
# Fess routes:
