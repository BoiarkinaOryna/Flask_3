import flask, os, pandas 
from .models import Product
from main.settings import DATABASE

def render_certain_tour(id: int):
        path_xl = os.path.abspath(__file__ + "/../Product2.xlsx")
        read_xl = pandas.read_excel(io = path_xl, header = None, names = ["title", "description", "country", "price", "date", "image", "full_description"])
        print(read_xl)
        for row in read_xl.iterrows():
                row_data = row[1]
                product = Product(
                        title = row_data["title"],
                        description = row_data["description"],
                        country = row_data["country"],
                        price = row_data["price"],
                        date = row_data["date"],
                        image = row_data["image"],
                        full_description = row_data["full_description"]
                )
                DATABASE.session.add(product)
        DATABASE.session.commit()
        return flask.render_template("tour_url.html", tour = Product.query.get(id))
def render_tour():        
        print(Product.query.all())
        return flask.render_template("tour.html", tours = Product.query.all())