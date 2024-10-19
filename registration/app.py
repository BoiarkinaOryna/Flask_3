import flask

registration = flask.Blueprint(
    name = "registration",
    import_name = "registration",
    static_url_path = "/registration/",
    template_folder = "templates",
    static_folder = "static"
)