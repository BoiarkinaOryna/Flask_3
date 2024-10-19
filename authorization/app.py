import flask

authorization = flask.Blueprint(
    name = "authorization",
    import_name = "authorization",
    static_url_path = "/authorization/",
    template_folder = "templates",
    static_folder = "static"
)