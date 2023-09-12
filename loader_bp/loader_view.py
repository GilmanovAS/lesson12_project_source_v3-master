from flask import Blueprint, render_template, send_from_directory, request

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='loader_templates', url_prefix='/post')


@loader_blueprint.route('/form/')
def post_form():
    return render_template('post_form.html')


@loader_blueprint.route('/uploads/<path:path>')
def uploads_url(path):
    return send_from_directory('uploads', path)


@loader_blueprint.route('/uploaded/', methods=["POST"])
def uploaded_page():
    picture = request.files.get('picture')

    return render_template('post_uploaded.html')
