"""
This window holds the edit section.
Here it is possible to change the properties of the fractal, as well as drawing it to the screen.
"""

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import fractal
from fractal import processor


from ui_windows.edit.settings import Settings
from ui_windows.edit.draw import Draw


class Edit(QWidget):
    back_signal = Signal()

    def __init__(self, info=None, parent=None):
        super(Edit, self).__init__(parent)

        # Create two main sections of edit window
        main_layout = QHBoxLayout(self)
        self.draw_layout = Draw(self)
        self.draw_layout.draw_signal.connect(self.draw_fractal)
        self.settings_layout = Settings(self)
        self.settings_layout.setFixedWidth(350)
        self.settings_layout.save_signal.connect(self.save_img)
        self.settings_layout.back_signal.connect(self.back)
        main_layout.addWidget(self.draw_layout)
        main_layout.addWidget(self.settings_layout)

        # Set main layout
        self.setLayout(main_layout)

        # Load fractal if applicable
        if info is not None:
            self.load_fractal(info)
        else:
            self.settings_layout.rules.add_rule()

    def load_fractal(self, info):
        self.settings_layout.load_fractal(info)

    def draw_fractal(self):
        info = self.settings_layout.read_info()
        fractal = processor.process_fractal(info)
        self.draw_layout.draw_fractal(fractal, int(info['angle']))

    def save_img(self, name):
        path = fractal.fractal_img_path(name)
        self.draw_layout.drawing.save_drawing(path)

    @Slot()
    def back(self):
        self.back_signal.emit()