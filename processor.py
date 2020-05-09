settings = {}


def process_fractal(fractal_settings):
    global settings
    settings = fractal_settings
    string = settings['axiom']

    for i in range(settings['n']):
        string = _process_string(string)
    return string


def _process_string(string):
    new_string = ""
    for c in string:
        new_string += _apply_rule(c)
    return new_string


def _apply_rule(c):
    if c in settings['rules']:
        return settings['rules'][c]
    else:
        return c
