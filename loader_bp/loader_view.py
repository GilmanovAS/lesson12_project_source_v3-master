from flask import Blueprint, render_template, request

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='loader_templates', url_prefix='/post')

@loader_blueprint.route('/form/')
def post_form():
    return render_template('post_form.html')

