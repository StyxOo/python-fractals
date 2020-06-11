"""
This is the dashboard window for the ui.
It displays available fractals, allows for adding new ones, as well as editing and removing existing fractals.
"""

from PySide2.QtWidgets import *


class Dashboard(QWidget):
    def __init__(self, parent=None):
        super(Dashboard, self).__init__(parent)

        layout = QGridLayout()
        layout.addWidget(QPushButton('Tool #1'))
        self.setLayout(layout)
        self.hide()
