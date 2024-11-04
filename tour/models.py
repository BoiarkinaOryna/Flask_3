from main.settings import DATABASE

class Product(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    title = DATABASE.Column(DATABASE.Text(50), primary_key = False)
    country = DATABASE.Column(DATABASE.Text(30), primary_key = False)
    price = DATABASE.Column(DATABASE.Float, primary_key = False)
    date = DATABASE.Column(DATABASE.Text, primary_key = False)
    description = DATABASE.Column(DATABASE.Text, primary_key = False)
    image = DATABASE.Column(DATABASE.Text, primary_key = False)
    full_description = DATABASE.Column(DATABASE.Text, primary_key = False)

    def __repr__(self):
        return f'Назва tour - {self.title}'