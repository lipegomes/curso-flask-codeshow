from flask import Flask


# Enter point
def create_app():
    """Factory principal"""
    app = Flask(__name__)
    return app
