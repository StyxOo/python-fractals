"""
This window holds the edit section.
Here it is possible to change the properties of the fractal, as well as drawing it to the screen.
"""

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import fractal


class Edit(QWidget):

    def __init__(self, info=None, parent=None):
        super(Edit, self).__init__(parent)

        # Create two main sections of edit window
        main_layout = QHBoxLayout()
        draw_layout = QVBoxLayout()
        settings_layout = QVBoxLayout()
        main_layout.addLayout(draw_layout)
        main_layout.addLayout(settings_layout)

        # Flesh out draw section
        draw_text = QTextEdit('Draw')
        draw_layout.addWidget(draw_text)

        # Flesh out settings section
        parameters_layout = QVBoxLayout()
        save_layout = QHBoxLayout()
        settings_layout.addLayout(parameters_layout)
        settings_layout.addLayout(save_layout)

        # Create parameters
        # Axiom
        self.axiom = Axiom()
        parameters_layout.addWidget(self.axiom)

        # Angle
        self.angle = Angle()
        parameters_layout.addWidget(self.angle)

        # Rules
        self.rules = Rules()
        parameters_layout.addWidget(self.rules)

        # Iterations
        self.iterations = Interations()
        parameters_layout.addWidget(self.iterations)

        # Save
        self.save = Save()
        self.save.save_signal.connect(self.save_fractal)
        save_layout.addWidget(self.save)

        # Set main layout
        self.setLayout(main_layout)

        # Load fractal if applicable
        if info is not None:
            self.load_fractal(info)

    @Slot()
    def save_fractal(self):
        info = {}
        info['name'] = self.save.input.text()
        info['axiom'] = self.axiom.input.text()
        info['rules'] = {}
        for rule in self.rules.rules:
            key = rule.from_input.text()
            value = rule.to_input.text()
            info['rules'][key] = value
        info['angle'] = self.angle.input.text()
        info['n'] = str(self.iterations.slider.value())
        fractal.save_fractal(info)

    def load_fractal(self, info):
        self.save.input.setText(info['name'])
        self.axiom.input.setText(info['axiom'])
        for key in info['rules'].keys():
            self.rules.add_rule(key, info['rules'][key])
        self.angle.set_value(info['angle'])
        self.iterations.slider.setValue(int(info['n']))


class Axiom(QWidget):
    def __init__(self, parent=None):
        super(Axiom, self).__init__(parent)
        layout = QVBoxLayout()
        self.label = QLabel('Axiom:')
        self.input = QLineEdit()
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        self.setLayout(layout)


class Angle(QWidget):
    def __init__(self, parent=None):
        super(Angle, self).__init__(parent)
        layout = QVBoxLayout()
        label = QLabel('Angle:')
        layout.addWidget(label)
        value_layout = QHBoxLayout()
        layout.addLayout(value_layout)
        self.supress_cb = False
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(180)
        self.slider.valueChanged.connect(self.on_angle_slider_value_changed)
        value_layout.addWidget(self.slider)
        self.input = QLineEdit()
        self.input.textChanged.connect(self.on_angle_input_value_changed)
        value_layout.addWidget(self.input)
        self.setLayout(layout)

    def on_angle_slider_value_changed(self):
        if not self.supress_cb:
            try:
                self.input.setText(str(self.slider.value()))
            except:
                pass
        else:
            self.supress_cb = False

    def on_angle_input_value_changed(self):
        try:
            self.supress_cb = True
            self.slider.setValue(int(self.input.toPlainText()))
        except:
            pass

    def set_value(self, value):
        self.input.setText(str(value))
        self.slider.setValue(int(value))


class Rules(QWidget):
    rules = []

    def __init__(self, parent=None):
        super(Rules, self).__init__(parent)
        self.layout = QVBoxLayout()
        label = QLabel('Rules:')
        self.layout.addWidget(label)
        add_button = QPushButton(text='Add Rule')
        add_button.clicked.connect(self.add_rule)
        self.layout.addWidget(add_button)
        self.setLayout(self.layout)

    def add_rule(self, from_value=None, to_value=None):
        rule = Rule()
        if from_value is not None and to_value is not None:
            rule.from_input.setText(from_value)
            rule.to_input.setText(to_value)
        self.layout.insertWidget(len(self.rules) + 1, rule)
        rule.remove_signal.connect(self.remove_rule)
        rule.index = len(self.rules)
        self.rules.append(rule)

    @Slot(int)
    def remove_rule(self, index):
        r = self.layout.takeAt(index + 1)
        self.rules.pop(index)
        r.widget().deleteLater()
        self.update_rule_indices()

    def update_rule_indices(self):
        for i in range(len(self.rules)):
            self.rules[i].index = i


class Rule(QWidget):
    remove_signal = Signal(int)
    index = None

    def __init__(self, parent=None):
        super(Rule, self).__init__(parent)
        layout = QHBoxLayout()
        self.from_input = QLineEdit()
        arrow = QLabel('->')
        self.to_input = QLineEdit()
        remove_button = QPushButton('rm')
        remove_button.clicked.connect(self.remove)
        layout.addWidget(self.from_input)
        layout.addWidget(arrow)
        layout.addWidget(self.to_input)
        layout.addWidget(remove_button)
        self.setLayout(layout)

    def remove(self):
        self.remove_signal.emit(self.index)


class Interations(QWidget):
    def __init__(self, parent=None):
        super(Interations, self).__init__(parent)
        layout = QVBoxLayout()
        label = QLabel('Iterations:')
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(10)
        layout.addWidget(label)
        layout.addWidget(self.slider)
        self.setLayout(layout)


class Save(QWidget):
    save_signal = Signal()

    def __init__(self, parent=None):
        super(Save, self).__init__(parent)
        layout = QHBoxLayout()
        self.input = QLineEdit()
        button = QPushButton('Save')
        button.clicked.connect(self.save)
        layout.addWidget(self.input)
        layout.addWidget(button)
        self.setLayout(layout)

    def save(self):
        self.save_signal.emit()