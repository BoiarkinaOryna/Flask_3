import flask

user = flask.Blueprint(
    name = "user",
    import_name = "user",
    static_url_path = "/user/",
    template_folder = "templates",
    static_folder = "static",
)