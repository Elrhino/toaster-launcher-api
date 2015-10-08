import json

from models.user import User


def get_response():
    users = [
        User(email="just@doit.com", name="Shia Laboeuf"),
        User(email="ebony@ivory.com", name="Terry Crews"),
        User(email="dude@lebowski.com", name="The Dude")
    ]

    return deserialize_array(users)


def deserialize_array(array):
    response = ""
    for val in array:
        response += json.dumps(val.__dict__, sort_keys=True) + ","

    return response[:-1]
