from flask import Flask, request, render_template, send_from_directory
from main_bp.main_view import main_blueprint
from loader_bp.loader_view import loader_blueprint

from functions import load_json


UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

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
