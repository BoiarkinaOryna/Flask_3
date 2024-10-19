import flask

home = flask.Blueprint(
    name = "home",
    import_name = "home",
    static_url_path = "/home/",
    template_folder = "templates",
    static_folder = "static"
)