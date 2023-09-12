import logging

from flask import Flask, send_from_directory

from config import MAX_CONTENT_LENGTH, LOG_LEVEL, APP_DEBUG
from loader_bp.loader_view import loader_blueprint
from main_bp.main_view import main_blueprint

logging.basicConfig(encoding='UTF-8', level=LOG_LEVEL)
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
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


app.run(debug=APP_DEBUG, host='127.0.0.1', port='5001')
