import flask, flask_login
from .models import Users
from main.settings import DATABASE

def render_registration():
    if flask.request.method == 'POST':
        user = Users(
            name = flask.request.form['name'],
            password = flask.request.form['password']
        )
        try:
            DATABASE.session.add(user)
            DATABASE.session.commit()
        except:
            return "Database error"

    return flask.render_template("registration.html")