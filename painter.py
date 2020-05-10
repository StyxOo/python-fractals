import turtle

positions = []


def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


def draw_fractal(fractal, settings, distance):
    t = turtle.Turtle()  # create the turtle
    wn = turtle.Screen()

    t.up()
    t.back(200)
    t.down()
    t.speed(0)

    for c in fractal:
        if c in 'ABCDE':
            t.forward(distance)
        elif c == '+':
            t.right(settings['angle'])
        elif c == '-':
            t.left(settings['angle'])
        elif c == '[':
            save_position(t)
        elif c == ']':
            jump_to_last_position(t)
        else:
            print("Unknown character '{}' in fractal".format(c))
    wn.exitonclick()


def save_position(t):
    position = {'x': t.xcor(), 'y': t.ycor(), 'heading': t.heading()}
    positions.append(position)


def jump_to_last_position(t):
    position = positions[-1]
    positions.pop()
    t.penup()
    t.setx(position['x'])
    t.sety(position['y'])
    t.setheading(position['heading'])
    t.pendown()
