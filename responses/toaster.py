import json
from models.toaster import Toaster


def get_response():
    toaster = Toaster(name='The Brave Little Toaster')

    return json.dumps(toaster.__dict__, sort_keys=True)
