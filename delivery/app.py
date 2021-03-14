from flask import Flask
from delivery.ext import site
from delivery.ext import config
from delivery.ext import toolbar


# Enter point
def create_app():
    """Factory principal"""
    app = Flask(__name__)
    config.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)

    return app
