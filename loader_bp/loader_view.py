from flask import Blueprint, render_template, request
from functions import load_json, dump_json
import logging
from config import UPLOAD_FOLDER

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='loader_templates', url_prefix='/post')


@loader_blueprint.route('/form/')
def post_form():
    return render_template('post_form.html')


@loader_blueprint.route('/uploaded/', methods=["POST"])
def uploaded_page():
    try:
        picture = request.files.get('picture')
        content = request.values.get('content')
        json_data: dict
        json_data = load_json()
        json_data.append({
            'pic': f'/{UPLOAD_FOLDER}/{picture.filename}',
            'content': content
        })
        if not picture.filename is None:
            picture.save(f'{UPLOAD_FOLDER}/{picture.filename}')
        if picture.filename.split('.')[-1] not in {'jpg', 'png', 'jpeg'}:
            logging.info('Not jpg or png')
            raise FileNotFoundError
    except FileNotFoundError:
        logging.exception("FileNotFoundError")
        return '<h2> Not jpg or png </h2> <a href="/" >Назад</a>'
    except PermissionError:
        logging.exception("PermissionError")
        return "<h2> File not found 2 </h2> <a href='/' >Назад</a>"
    else:
        dump_json(json_data)
        return render_template('post_uploaded.html', picture=f'/{UPLOAD_FOLDER}/{picture.filename}', content=content)
