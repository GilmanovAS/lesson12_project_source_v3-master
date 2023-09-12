from flask import Flask

from loader_bp.loader_view import loader_blueprint
from main_bp.main_view import main_blueprint

UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.errorhandler(413)
def error_413_page(e):
    return "<h1> The file size is large. </h1>" , 413


# @app.route("/")
# def page_index():
#     pass


# @app.route("/list")
# def page_tag():
#     pass
#
#
# @app.route("/post", methods=["GET", "POST"])
# def page_post_form():
#     pass
#
#
# @app.route("/post", methods=["POST"])
# def page_post_upload():
#     pass
#
#
# @app.route("/uploads/<path:path>")
# def static_dir(path):
#     return send_from_directory("uploads", path)

app.debug = True
app.run()
