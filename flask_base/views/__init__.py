
def init_app(app):
    from . import routes
    app.register_bluprint(routes)
    return app