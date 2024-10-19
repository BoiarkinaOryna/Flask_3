import flask, flask_login
from registration.models import Users

def render_authorization():
    if flask.request.method == 'POST':
        for user in Users.query.filter_by(name = flask.request.form["name"]):
            print(
                " user =", Users.query.filter_by(name = flask.request.form["name"]), "\n",
                "username from form =", flask.request.form["name"], "\n",
                "user.name =", user.name, "\n",
                )
            if user.password == flask.request.form['password']:
                flask_login.login_user(user = user)
                print("login complete")
                return flask.redirect("/")

    return flask.render_template("authorization.html")