import painter
from tkinter import *


root = Tk()

# Create a canvas for turtle to draw on
canvas = Canvas(root, width=300, height=300)
canvas.grid(row=0, column=0, columnspan=2)


def on_draw():
    fractal = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+[[AAAAAAAAAAAAAAAA+[[AAAAAAAA+[[AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA[-AAAAAAAAAAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA+[[AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA[-AAAAAAAAAAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAAAAAAAAAA[-AAAAAAAAAAAAAAAAAAAAAAAA+[[AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA[-AAAAAAAAAAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAAAAAA+[[AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA[-AAAAAAAAAAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAAAAAAAAAA+[[AAAAAAAA+[[AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA[-AAAAAAAAAAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA+[[AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA[-AAAAAAAAAAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAAAAAAAAAA[-AAAAAAAAAAAAAAAAAAAAAAAA+[[AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA[-AAAAAAAAAAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAAAAAA+[[AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA[-AAAAAAAAAAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA[-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+[[AAAAAAAA+[[AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA[-AAAAAAAAAAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA+[[AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA[-AAAAAAAAAAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAAAAAAAAAA[-AAAAAAAAAAAAAAAAAAAAAAAA+[[AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA[-AAAAAAAAAAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAAAAAA+[[AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA[-AAAAAAAAAAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAAAAAAAAAAAAAA+[[AAAAAAAA+[[AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA[-AAAAAAAAAAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA+[[AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA[-AAAAAAAAAAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAAAAAAAAAA[-AAAAAAAAAAAAAAAAAAAAAAAA+[[AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA[-AAAAAAAAAAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAAAAAA+[[AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAAAAAA[-AAAAAAAAAAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AAAA+[[AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]-AAAA[-AAAAAA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X]+AA+[[A+[[X]-X]-A[-AX]+X]-A+[[X]-X]-A[-AX]+X]-AA[-AAA+[[X]-X]-A[-AX]+X]+A+[[X]-X]-A[-AX]+X"
    painter.draw_fractal(fractal, 25, 1)


def on_speed_change(value):
    value = float(value)
    value += 1
    if value > 10:
        value = 0
    painter.change_speed(value)


# Create a label to display fractal
fractal_label = Label(root, text="Fractal will display here")
fractal_label.grid(row=1, column=0, columnspan=2, sticky=W)

# Create a slider for drawing speed
draw_speed = Scale(root, length=200, from_=0, to=10, orient=HORIZONTAL, command=on_speed_change)
draw_speed.grid(row=2, column=0)

# Create a button to draw fractal
draw_button = Button(root, text="Draw", command=on_draw)
draw_button.grid(row=2, column=1)


if __name__ == '__main__':
    painter.setup_turtle(canvas)
    root.mainloop()
