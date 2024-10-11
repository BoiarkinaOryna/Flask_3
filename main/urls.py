from .settings import main
import home
import flask

home.home.add_url_rule(
    rule = '/',
    view_func = home.render_home
)
main.register_blueprint(blueprint = home.home)