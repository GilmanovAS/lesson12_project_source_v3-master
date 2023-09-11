import json

POST_PATH = "posts.json"
def load_json():
    with open(POST_PATH, 'r', encoding='UTF-8') as fp:
        return json.load(fp)
