from .settings import main
import home
import tour
import flask

tour.tour.add_url_rule(
     rule = "/tour",
     view_func = tour.render_tour, 
     methods = ["GET", "POST"]
)

tour.tour.add_url_rule(
    rule = "/tour_url/<int:id>",
    view_func = tour.render_certain_tour,
    methods = ["GET", "POST"]
)
main.register_blueprint(blueprint = tour.tour)

home.home.add_url_rule(
    rule = '/',
    view_func = home.render_home
)
main.register_blueprint(blueprint = home.home)
