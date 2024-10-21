from main.settings import DATABASE
from flask_login import UserMixin

class Users(DATABASE.Model, UserMixin):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True, nullable = False)
    name = DATABASE.Column(DATABASE.String(50))
    password = DATABASE.Column(DATABASE.String(100))

    def __repr__(self):
        return f"Name - {self.name}"