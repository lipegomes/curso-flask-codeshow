from flask import Flask
from delivery.ext import site


# Enter point
def create_app():
    """Factory principal"""
    app = Flask(__name__)
    site.init_app(app)

    return app
