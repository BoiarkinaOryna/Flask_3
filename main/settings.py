import flask_sqlalchemy, flask_migrate, flask, os, flask_login

main = flask.Flask(
    import_name = "main",
    static_url_path = "/main/",
    template_folder = "templates",
    instance_path = os.path.abspath(__file__ + "/../instance")
)

main.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

DATABASE = flask_sqlalchemy.SQLAlchemy(
    app = main
)

migrate = flask_migrate.Migrate(app = main, db = DATABASE)