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
    deleted_signal = Signal()

    def __init__(self, parent=None):
        super(Dashboard, self).__init__(parent)

        layout = QVBoxLayout()

        self.info_widgets = []
        for info in fractal.fractals:
            fractal_info = FractalInfo(info)
            fractal_info.load_signal.connect(self.load_fractal)
            fractal_info.remove_signal.connect(self.info_deleted)
            self.info_widgets.append(fractal_info)
        new_fractal = NewFractal()
        new_fractal.new_fractal.connect(self.load_signal)
        self.info_widgets.append(new_fractal)
        self.info_widget = InfosContainer(self.info_widgets, self)

        scroll_area = QScrollArea()
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(False)
        scroll_area.setWidget(self.info_widget)

        layout.addWidget(scroll_area)

        self.setLayout(layout)

    @Slot(dict)
    def load_fractal(self, info):
        self.load_signal.emit(info)

    @Slot()
    def info_deleted(self):
        self.deleted_signal.emit()


class InfosContainer(QWidget):
    def __init__(self, infos, parent=None):
        super(InfosContainer, self).__init__(parent)
        layout = QGridLayout()
        infos_per_row = 4
        for i in range(len(infos)):
            infos[i].setParent(self)
            column = i % infos_per_row
            row = int(i/infos_per_row)
            layout.addWidget(infos[i], row, column)
        self.setLayout(layout)


class FractalInfo(QGroupBox):
    load_signal = Signal(dict)
    remove_signal = Signal()

    def __init__(self, info, parent=None):
        super(FractalInfo, self).__init__(parent)
        # self.setFrameShape(QFrame.Box)
        self.setFixedSize(232, 290)
        self.setTitle(info['name'])
        self.info = info
        layout = QVBoxLayout()
        img_path = fractal.fractal_img_path(info["name"])
        img = QPixmap(img_path)
        self.image = QLabel("Fractal Image")
        self.image.setPixmap(img)
        self.image.setScaledContents(True)
        dash = QFrame()
        dash.setFrameShape(QFrame.HLine)
        layout.addWidget(self.image)
        layout.addWidget(dash)
        self.button = QPushButton("Delete")
        self.button.setFixedHeight(40)
        self.button.clicked.connect(self.delete_self)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def mouseReleaseEvent(self, event):
        mouse_pos = event.pos()
        if self.rect().contains(mouse_pos):
            self.load_self()

    def load_self(self):
        print("Load {0}".format(self.info['name']))
        self.load_signal.emit(self.info)

    def delete_self(self):
        self.delete_dialog = RemoveDialog()
        self.delete_dialog.show()
        self.delete_dialog.accepted.connect(self.confirm_delete)

    def confirm_delete(self):
        fractal.delete_fractal(self.info['name'])
        self.remove_signal.emit()


class NewFractal(QGroupBox):
    new_fractal = Signal(dict)

    def __init__(self, parent=None):
        super(NewFractal, self).__init__(parent)
        self.setFixedSize(232, 290)
        self.setTitle("New Fractal")
        layout = QVBoxLayout()

        image = QPixmap('./assets/baseline_add_black_48dp.png')
        self.image = QLabel()
        self.image.setPixmap(image)
        self.image.setScaledContents(True)
        dash = QFrame()
        dash.setFrameShape(QFrame.HLine)
        layout.addWidget(self.image)
        layout.addWidget(dash)
        self.button = QPushButton("New fractal")
        self.button.clicked.connect(self.create_new)
        self.button.setFixedHeight(40)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def mousePressEvent(self, event: QMouseEvent):
        self.create_new()

    def create_new(self):
        self.new_fractal.emit(None)


class RemoveDialog(QDialog):
    overwrite_signal = Signal()

    def __init__(self, parent=None):
        super(RemoveDialog, self).__init__(parent)
        self.setWindowTitle("Delete")

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel('Are you sure you want to delete the fractal?')
        label.setWordWrap(True)
        layout.addWidget(label)

        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        confirm_button = QPushButton("Delete")
        confirm_button.clicked.connect(self.accept)
        button_layout.addWidget(confirm_button)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(cancel_button)
