"""
This window holds the edit section.
Here it is possible to change the properties of the fractal, as well as drawing it to the screen.
"""

from PySide2.QtWidgets import *


class Edit(QWidget):
    def __init__(self, parent=None):
        super(Edit, self).__init__(parent)

        layout = QGridLayout()
        layout.addWidget(QTextEdit('Tool #2'))
        self.setLayout(layout)
        self.hide()