from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from ui_windows.painter import Painter


class Draw(QWidget):
    draw_signal = Signal()

    def __init__(self, parent=None):
        super(Draw, self).__init__(parent)

        main_layout = QVBoxLayout(self)

        self.drawing = Drawing()
        main_layout.addWidget(self.drawing)

        self.fractal_label = Fractal()
        main_layout.addWidget(self.fractal_label)

        self.draw_control = DrawControlls()
        self.draw_control.draw_signal.connect(self.on_draw)
        main_layout.addWidget(self.draw_control)

    def draw_fractal(self, fractal, angle):
        self.fractal_label.set_fractal(fractal)
        self.drawing.draw(fractal, angle)

    @Slot()
    def on_draw(self):
        self.draw_signal.emit()


class Drawing(QGroupBox):
    def __init__(self, parent=None):
        super(Drawing, self).__init__(parent)
        self.setTitle("Drawing")
        self.setFixedSize(683, 550)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.draw_widget = QLabel()
        canvas = QPixmap(515, 515)
        canvas.fill()
        self.draw_widget.setPixmap(canvas)
        layout.addWidget(self.draw_widget)

    def draw(self, fractal, angle):
        self.draw_widget.pixmap().fill()
        painter = Painter(self.draw_widget.pixmap(), 200, 500, 200, 498)
        for c in fractal:
            if c == '+':
                painter.rotate(angle)
            elif c == '-':
                painter.rotate(-angle)
            elif c == '[':
                painter.save_position()
            elif c == ']':
                painter.load_position()
            elif ord(c) in range(ord('A'), ord('T') + 1):
                painter.forward()
        self.update()

    def save_drawing(self, path):
        self.draw_widget.pixmap().save(path)


class Fractal(QGroupBox):
    def __init__(self, parent=None):
        super(Fractal, self).__init__(parent)
        self.setTitle("Fractal")
        self.setFixedHeight(70)

        layout = QVBoxLayout()

        self.label = QLabel("Fractal will show here")
        layout.addWidget(self.label)

        self.setLayout(layout)

    def set_fractal(self, fractal):
        self.label.setText(fractal)


class DrawControlls(QWidget):
    draw_signal = Signal()

    def __init__(self, parent=None):
        super(DrawControlls, self).__init__(parent)
        # self.setTitle("Draw Controls")
        self.setFixedHeight(100)

        layout = QHBoxLayout()
        self.setLayout(layout)

        self.speed = DrawSpeed()
        layout.addWidget(self.speed)

        self.buttons = DrawButtons()
        self.buttons.draw_signal.connect(self.on_draw)
        layout.addWidget(self.buttons)

    @Slot()
    def on_draw(self):
        self.draw_signal.emit()


class DrawSpeed(QGroupBox):
    def __init__(self, parent=None):
        super(DrawSpeed, self).__init__(parent)
        self.setTitle("Speed")

        layout = QHBoxLayout()
        self.setLayout(layout)

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(1)
        self.slider.setMaximum(11)
        self.slider.setTickPosition(QSlider.TicksBelow)
        # self.slider.valueChanged.connect
        layout.addWidget(self.slider)


class DrawButtons(QGroupBox):
    draw_signal = Signal()

    def __init__(self, parent=None):
        super(DrawButtons, self).__init__(parent)
        self.setTitle("Buttons")

        layout = QHBoxLayout()
        self.setLayout(layout)

        self.draw_button = QPushButton("Draw")
        self.draw_button.clicked.connect(self.on_draw)
        layout.addWidget(self.draw_button)

        self.first_draw_button = QPushButton("drw")
        layout.addWidget(self.first_draw_button)

    def on_draw(self):
        self.draw_signal.emit()
