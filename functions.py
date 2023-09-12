import json
from config import POST_PATH


def load_json():
    with open(POST_PATH, 'r', encoding='UTF-8') as fp:
        return json.load(fp)


def dump_json(json_data):
    with open(POST_PATH, 'w', encoding='UTF-8') as fp:
        return json.dump(json_data, fp, ensure_ascii=False, indent=4)
