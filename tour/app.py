import flask
tour = flask.Blueprint(
    name = "tour",
    import_name = "tour",
    static_url_path = "/tour/",
    template_folder = "templates",
    static_folder = "static"
)