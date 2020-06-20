"""
This is the dashboard window for the ui.
It displays available fractals, allows for adding new ones, as well as editing and removing existing fractals.
"""

import fractal

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *


class Dashboard(QWidget):
    load_signal = Signal(dict)

    def __init__(self, parent=None):
        super(Dashboard, self).__init__(parent)

        layout = QVBoxLayout()

        info_widgets = []
        for info in fractal.fractals:
            fractal_info = FractalInfo(info)
            fractal_info.load_signal.connect(self.load_fractal)
            info_widgets.append(fractal_info)
        info_widget = InfosContainer(info_widgets)

        scroll_area = QScrollArea()
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(False)
        scroll_area.setWidget(info_widget)

        layout.addWidget(scroll_area)

        self.setLayout(layout)

    @Slot(dict)
    def load_fractal(self, info):
        self.load_signal.emit(info)


class InfosContainer(QWidget):
    def __init__(self, infos, parent=None):
        super(InfosContainer, self).__init__(parent)
        layout = QGridLayout()
        infos_per_row = 5
        for i in range(len(infos)):
            column = i % infos_per_row
            row = int(i/infos_per_row)
            layout.addWidget(infos[i], row, column)
        self.setLayout(layout)


class FractalInfo(QFrame):
    load_signal = Signal(dict)

    def __init__(self, info, parent=None):
        super(FractalInfo, self).__init__(parent)
        self.setFrameShape(QFrame.Box)
        self.info = info
        layout = QVBoxLayout()
        header_layout = QHBoxLayout()
        self.label = QLabel(info['name'])
        self.button = QPushButton()
        header_layout.addWidget(self.label)
        header_layout.addWidget(self.button)
        layout.addLayout(header_layout)
        dash = QFrame()
        dash.setFrameShape(QFrame.HLine)
        layout.addWidget(dash)
        layout.addWidget(QPushButton("Image here"))
        self.setLayout(layout)

    def mousePressEvent(self, event:QMouseEvent):
        self.load_self()

    def load_self(self):
        print("Load {0}".format(self.info['name']))
        self.load_signal.emit(self.info)

