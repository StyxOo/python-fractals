import json
import os

fractals = []


def load_fractals():
    with open(fractal_json_path()) as fractal_file:
        global fractals
        fractals = json.load(fractal_file)


def save_fractal(info):
    fractals.append(info)
    with open(fractal_json_path(), 'w') as fractal_file:
        json.dump(fractals, fractal_file)


def delete_fractal(name):
    for fractal in fractals:
        if fractal['name'] == name:
            fractals.remove(fractal)


def fractal_json_path():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fractals.json')


def fractal_img_path(name):
    file = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), './images/{0}.png'.format(name))

load_fractals()