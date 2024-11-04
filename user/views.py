import flask
from registration.models import Users
from flask_login import current_user 

def render_user():
    return flask.render_template("user.html", users = Users.query.all())