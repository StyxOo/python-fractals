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
        main_layout = QHBoxLayout(self)
        draw_layout = QVBoxLayout(self)
        self.settings_layout = Settings(self)
        self.settings_layout.setFixedWidth(350)
        main_layout.addLayout(draw_layout)
        main_layout.addWidget(self.settings_layout)

        # Flesh out draw section
        draw_text = QTextEdit('Draw')
        draw_layout.addWidget(draw_text)

        # Set main layout
        self.setLayout(main_layout)

        # Load fractal if applicable
        if info is not None:
            self.load_fractal(info)

    def load_fractal(self, info):
        self.settings_layout.load_fractal(info)


class Settings(QWidget):
    def __init__(self, parent=None):
        super(Settings, self).__init__(parent)

        main_layout = QVBoxLayout(self)
        parameters_group = QGroupBox("Parameters", self)
        parameters_layout = QVBoxLayout(parameters_group)
        parameters_group.setLayout(parameters_layout)
        save_group = QGroupBox("Save", self)
        save_group.setFixedHeight(100)
        save_layout = QHBoxLayout(save_group)
        save_group.setLayout(save_layout)
        main_layout.addWidget(parameters_group)
        main_layout.addWidget(save_group)

        # Create parameters
        # Info
        label_text = "Information:\n" \
                     "Characters A-T draw a line. U-Z are placeholders for fractal development.\n" \
                     "+ and - are right and left turns.\n" \
                     "[ saves the current position. ] restores it. " \
                     "Make sure You save a position before trying to load one.\n" \
                     "These characters can be used in the axiom as well as the rules."
        info_label = QLabel(label_text)
        info_label.setWordWrap(True)
        parameters_layout.addWidget(info_label)

        # Axiom
        self.axiom = Axiom(parameters_group)
        parameters_layout.addWidget(self.axiom)

        # Angle
        self.angle = Angle(parameters_group)
        parameters_layout.addWidget(self.angle)

        # Rules
        self.rules = Rules(parameters_group)
        parameters_layout.addWidget(self.rules)

        # Iterations
        self.iterations = Interations(parameters_group)
        parameters_layout.addWidget(self.iterations)

        # Save
        self.save = Save(save_group)
        self.save.save_signal.connect(self.save_fractal)
        save_layout.addWidget(self.save)

        # Set main layout
        self.setLayout(main_layout)

    def read_info(self):
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
        return info

    @Slot()
    def save_fractal(self):
        info = self.read_info()
        fractal.save_fractal(info)

    def load_fractal(self, info):
        self.save.input.setText(info['name'])
        self.axiom.input.setText(info['axiom'])
        for key in info['rules'].keys():
            self.rules.add_rule(key, info['rules'][key])
        self.angle.set_value(info['angle'])
        self.iterations.slider.setValue(int(info['n']))


class Parameters(QGroupBox):
    def __init__(self, parent=None):
        super(Parameters, self).__init__(parent)
        self.setTitle("Parameters")
        self.layout = QVBoxLayout()
        self.init_ui()
        self.setLayout(self.layout)

    def init_ui(self):
        pass


class Axiom(QGroupBox):
    def __init__(self, parent=None):
        super(Axiom, self).__init__(parent)
        self.setTitle("Axiom")
        self.setFixedHeight(75)
        layout = QVBoxLayout()
        self.input = QLineEdit()
        rx = QRegExp("[A-Z]+")
        validator = QRegExpValidator(rx, self)
        self.input.setValidator(validator)
        layout.addWidget(self.input)
        self.setToolTip("The Axiom is the start point for Your fractal.")
        self.setLayout(layout)


class Angle(QGroupBox):
    def __init__(self, parent=None):
        super(Angle, self).__init__(parent)
        self.setTitle("Angle")
        self.setFixedHeight(75)
        layout = QHBoxLayout()
        self.supress_cb = False
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickInterval(45)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setMinimum(0)
        self.slider.setMaximum(180)
        self.slider.valueChanged.connect(self.on_angle_slider_value_changed)
        layout.addWidget(self.slider)
        self.input = QLineEdit()
        validator = QIntValidator(0, 180, self)
        self.input.setValidator(validator)
        self.input.textEdited.connect(self.on_angle_input_value_changed)
        self.input.setFixedWidth(25)
        self.input.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.input)
        self.setToolTip("Angle of rotation when fractal contains ( or )")
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


class Rules(QGroupBox):
    rules = []

    def __init__(self, parent=None):
        super(Rules, self).__init__(parent)
        self.setTitle("Rules")
        self.layout = QVBoxLayout()
        add_button = QPushButton(text='Add Rule')
        add_button.setToolTip("Add new rule")
        add_button.clicked.connect(self.add_rule)
        self.layout.addWidget(add_button)
        self.setToolTip("Rules describe how a fractal develops in each iteration")
        self.setLayout(self.layout)

    def add_rule(self, from_value=None, to_value=None):
        rule = Rule()
        if from_value is not None and to_value is not None:
            rule.from_input.setText(from_value)
            rule.to_input.setText(to_value)
        self.layout.insertWidget(len(self.rules), rule)
        rule.remove_signal.connect(self.remove_rule)
        rule.index = len(self.rules)
        self.rules.append(rule)

    @Slot(int)
    def remove_rule(self, index):
        r = self.layout.takeAt(index)
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
        self.from_input.setFixedWidth(20)
        self.from_input.setAlignment(Qt.AlignCenter)
        self.from_input.setToolTip("Character in fractal to exchange")
        from_rx = QRegExp("[A-Z]")
        from_validator = QRegExpValidator(from_rx, self)
        self.from_input.setValidator(from_validator)
        arrow = QLabel('->')
        self.to_input = QLineEdit()
        self.to_input.setToolTip("Characters which should be placed instead")
        to_rx = QRegExp("[A-Z]+")
        to_validator = QRegExpValidator(to_rx, self)
        self.to_input.setValidator(to_validator)
        remove_button = QPushButton('rm')
        remove_button.setToolTip("Remove this rule")
        remove_button.clicked.connect(self.remove)
        layout.addWidget(self.from_input)
        layout.addWidget(arrow)
        layout.addWidget(self.to_input)
        layout.addWidget(remove_button)
        self.setLayout(layout)

    def remove(self):
        self.remove_signal.emit(self.index)


class Interations(QGroupBox):
    def __init__(self, parent=None):
        super(Interations, self).__init__(parent)
        self.setTitle("Iterations")
        self.setToolTip("Number of iterations for fractal")
        self.setFixedHeight(75)
        layout = QVBoxLayout()
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(10)
        self.slider.setTickInterval(1)
        self.slider.setTickPosition(QSlider.TicksBelow)
        layout.addWidget(self.slider)
        self.setLayout(layout)


class Save(QWidget):
    save_signal = Signal()

    def __init__(self, parent=None):
        super(Save, self).__init__(parent)
        # self.setTitle("Save")
        layout = QHBoxLayout()
        self.input = QLineEdit()
        self.input.setToolTip("Name under which fractal should be saved")
        rx = QRegExp("([A-Z]|[0-9])+")
        validator = QRegExpValidator(rx, self)
        self.input.setValidator(validator)
        button = QPushButton('Save')
        button.setToolTip("Save")
        button.clicked.connect(self.save)
        layout.addWidget(self.input)
        layout.addWidget(button)
        self.setLayout(layout)

    def save(self):
        self.save_signal.emit()