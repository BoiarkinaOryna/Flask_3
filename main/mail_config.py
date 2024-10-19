from .settings import main
from flask_mail import Mail

main.config['MAIL_SERVER'] = 'smtp.gmail.com'
main.config['MAIL_PORT'] = 587
main.config['MAIL_USE_TLS'] = True
main.config['MAIL_USE_SSL'] = False
main.config['MAIL_USERNAME'] = 'frank01zeroy@gmail.com'
main.config['MAIL_PASSWORD'] = 'lfww mhod moox mswe'
main.config['MAIL_DEFAULT_SENDER'] = "frank01zeroy@gmail.com"

mail = Mail(app = main)