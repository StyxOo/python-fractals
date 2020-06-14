"""
This creates the main application to be used. It requests windows as required for content.
"""

from PySide2.QtWidgets import *

import sys
import fractal

from ui_windows.dashboard import Dashboard
from ui_windows.edit import Edit


class MyApplication(QMainWindow):
    def __init__(self, parent=None):
        super(MyApplication, self).__init__(parent)

        self.show_dashboard()

        content_menu = self.menuBar().addMenu("Tools")
        content_menu.addAction('show Dashboard', self.show_dashboard)
        content_menu.addAction('show Edit', self.show_edit)

    def show_dashboard(self):
        dashboard = Dashboard()
        self.setCentralWidget(dashboard)
        dashboard.show()
        self.setWindowTitle('Dashboard')

    def show_edit(self):
        edit = Edit(info=fractal.fractals[0])
        self.setCentralWidget(edit)
        edit.show()
        self.setWindowTitle('Edit')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    instance = MyApplication()
    instance.show()
    sys.exit(app.exec_())