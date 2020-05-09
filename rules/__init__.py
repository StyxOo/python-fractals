import os
import json

settings = []

json_path = os.path.join(os.path.dirname(__file__), './fractals.json')
with open(json_path) as json_file:
    settings = json.load(json_file)