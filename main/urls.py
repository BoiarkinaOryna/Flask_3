from .settings import main
import home, registration, authorization, user, tour

home.home.add_url_rule(
    rule = '/',
    view_func = home.render_home,
    methods = ['GET', 'POST']
)
main.register_blueprint(blueprint = home.home)

registration.registration.add_url_rule(
    rule = '/registration',
    view_func = registration.render_registration,
    methods = ['GET', 'POST']
)
main.register_blueprint(blueprint = registration.registration)

authorization.authorization.add_url_rule(
    rule = '/authorization',
    view_func = authorization.render_authorization,
    methods = ['GET', 'POST']
)
main.register_blueprint(blueprint = authorization.authorization)

user.user.add_url_rule(
    rule = "/user",
    view_func = user.render_user,
    methods = ["GET", "POST"]
)
main.register_blueprint(blueprint = user.user)

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