import logging
import os
from pprint import pprint

from flask import Flask, send_from_directory

# from config import MAX_CONTENT_LENGTH, LOG_LEVEL, APP_DEBUG
from loader_bp.loader_view import loader_blueprint
from main_bp.main_view import main_blueprint

app = Flask(__name__)
app.config.from_pyfile('config.py')
logging.basicConfig(encoding='UTF-8', level=app.config.get('LOG_LEVEL'))
logging.info('Registration BP info')
logging.debug('Registration BP debug')
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.errorhandler(413)
def error_413_page(e):
    return "<h1> The file size is large. </h1>", 413


@app.route("/uploads/images/<path:path>")
def static_dir(path):
    return send_from_directory("uploads/images", path)

# pprint(os.environ, indent=4)

app.run(app.config.get('HOST'), app.config.get('PORT'))
