from random import randint

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import math


class Painter:
    def __init__(self, canvas, x1, y1, x2, y2, random_color, mark_first, mark_nodes):
        self.canvas = canvas
        self.ahead = ((x2 - x1) / 10, (y2 - y1) / 10)
        self.position = (x1, y1)
        self.positions = []

        self.random_color = random_color
        self.mark_first = mark_first
        self.mark_nodes = mark_nodes

    def forward(self):
        painter = QPainter(self.canvas)
        painter.setPen(Qt.black)

        if self.random_color:
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            painter.setPen(QColor(r, g, b))

        if self.mark_first:
            painter.setPen(Qt.red)
            self.mark_first = False

        new_pos = (self.position[0] + self.ahead[0], self.position[1] + self.ahead[1])
        painter.drawLine(self.position[0], self.position[1], new_pos[0], new_pos[1])
        self.position = new_pos

        if self.mark_nodes:
            pen = painter.pen()
            pen.setWidth(3)
            painter.setPen(pen)
            # painter.drawPoint(self.position[0], self.position[1])
            painter.drawLine(self.position[0], self.position[1], self.position[0], self.position[1])

        painter.end()

    def save_position(self):
        pos = {"position": self.position, "forward": self.ahead}
        self.positions.append(pos)

    def load_position(self):
        pos = self.positions.pop()
        self.position = pos['position']
        self.ahead = pos['forward']

    def rotate(self, angle):
        angle = math.radians(angle)
        x = math.cos(angle) * self.ahead[0] - math.sin(angle) * self.ahead[1]
        y = math.sin(angle) * self.ahead[0] + math.cos(angle) * self.ahead[1]
        self.ahead = (x, y)
