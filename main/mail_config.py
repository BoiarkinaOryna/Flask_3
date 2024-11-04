from .settings import main
from flask_mail import Mail

main.config['MAIL_SERVER'] = 'smtp.gmail.com'
main.config['MAIL_PORT'] = 587
main.config['MAIL_USE_TLS'] = True
main.config['MAIL_USE_SSL'] = False
main.config['MAIL_USERNAME'] = "daria.filinskaya2009@gmail.com"
main.config['MAIL_PASSWORD'] = 'chsx mbei giam ofkt'
main.config['MAIL_DEFAULT_SENDER'] = "daria.filinskaya2009@gmail.com"

mail = Mail(app = main)