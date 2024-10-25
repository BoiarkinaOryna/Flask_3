import flask
import flask_mail
from main.mail_config import mail

def render_home():
    email_sended = False
    print("flask.request.cookies =", flask.request.cookies.get('review_sended'))
    if flask.request.cookies.get('review_sended') == "true":
        if flask.request.method == "POST":
            # print("flask.request =", flask.request)
            try:
                msg = flask_mail.Message(
                    subject = f'This is a review from {flask.request.form["username"]}',
                    recipients=['boyarkina.ar@gmail.com'],
                    body = flask.request.form["message"]
                )
                mail.send(msg)
                email_sended = True
                print("home views")
            except:
                print("home views error")
        print("email_sended =", email_sended)
    return flask.render_template("home.html", email_status = email_sended)