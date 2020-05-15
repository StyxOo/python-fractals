import turtle

_t = None
_positions = []


def setup_turtle(canvas):
    global _t
    _t = turtle.RawTurtle(canvas)
    _t.up()
    _t.back(200)
    _t.down()
    _t.speed(0)


def draw_fractal(fractal, angle, distance):
    if _t is None:
        print("Turtle is not set up yet. Run setup_turtle command first!")
        return

    _t.reset()

    for c in fractal:
        if c in 'ABCDE':
            _t.forward(distance)
        elif c == '+':
            _t.right(angle)
        elif c == '-':
            _t.left(angle)
        elif c == '[':
            _save_position(_t)
        elif c == ']':
            _jump_to_last_position(_t)


def _save_position(t):
    position = {'x': t.xcor(), 'y': t.ycor(), 'heading': t.heading()}
    _positions.append(position)


def _jump_to_last_position(t):
    position = _positions[-1]
    _positions.pop()
    t.penup()
    t.setx(position['x'])
    t.sety(position['y'])
    t.setheading(position['heading'])
    t.pendown()
