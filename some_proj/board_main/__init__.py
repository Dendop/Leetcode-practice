from flask import Flask
from board_main import pages


def create_new_app():
    app = Flask(__name__)
    
    app.register_blueprint(pages.bp)
    
    return app
