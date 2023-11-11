import json


def load_data(filename="temp.json"):
    # load the saved data in directory

    data = json.load(open(filename))
    return data
