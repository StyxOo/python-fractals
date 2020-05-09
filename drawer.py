import turtle


def draw_fractal(fractal, settings, distance):
    t = turtle.Turtle()  # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(9)

    for c in fractal:
        if c in settings['variables']:
            t.forward(distance)
        elif c == '+':
            t.right(settings['angle'])
        elif c == '-':
            t.left(settings['angle'])
        else:
            print("Unknown character '{}' in fractal".format(c))
    wn.exitonclick()
