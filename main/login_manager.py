import flask_login
from .settings import main
from registration.models import Users

main.secret_key = "067bbv48jbvd3sill911vbhtfj449hv3mwr6h9"
# print("secret_key =", shop.secret_key)    

login = flask_login.LoginManager(main)
login.init_app(main)

@login.user_loader
def load(id):
    return Users.query.get(id)