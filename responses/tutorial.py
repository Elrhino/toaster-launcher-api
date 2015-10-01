import json
from models.user import User


def get_response():
    user = User(email="just@doit.com", name="Shia Laboeuf")
    return json.dumps(user.__dict__, sort_keys=True)
