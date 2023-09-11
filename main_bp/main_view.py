from flask import render_template, Blueprint, request

from functions import load_json

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    search_str = request.values.get('s')
    posts = [x for x in load_json() if search_str.lower() in x['content'].lower()]
    return render_template('post_list.html', search_str=search_str, posts=posts)
