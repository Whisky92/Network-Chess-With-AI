from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore, QtGui
from PyQt5.uic import loadUi
import enum
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer, QEvent
from PyQt5.QtGui import QColorConstants
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QMainWindow, QPushButton, QSpinBox, QTextEdit, QVBoxLayout, QWidget
from gui.message_box import MessageBox


class MyTimer(QDialog):

    def __init__(self, turn_length_in_minutes):
        QDialog.__init__(self)
        loadUi("resource_ui_files/timer.ui", self)

        self.panel: QLabel

        self.panel.setFont(QFont("Times New Roman", 40))

        self.panel.setAlignment(Qt.AlignHCenter)
        self.panel.setAlignment(Qt.AlignVCenter)

        self.length = turn_length_in_minutes

        self._status = self.TimerStatus.init
        self._left_seconds = turn_length_in_minutes * 60

        self.timer = QTimer()
        self.timer.timeout.connect(self.countdown_and_show)
        self.show_time()

    def get_remaining_time(self):
        return self._left_seconds

    def countdown_and_show(self):
        if self._left_seconds > 0:
            self._left_seconds -= 1
            self.show_time()
        else:
            self.timer.stop()
            self.show_time()

    def start_timer(self):
        if self._left_seconds > 0:
            self._left_seconds -= 1
            self._status = self.TimerStatus.counting
            self.show_time()
            self.timer.start(1000)

    def stop_timer(self):
        self.timer.stop()
        self._status = self.TimerStatus.paused

    def show_time(self):
        minutes = self._left_seconds // 60
        seconds = self._left_seconds - (minutes * 60)

        default_size = 9

        self.panel.setText("{:02}:{:02}".format(int(minutes), int(seconds)))
        self.panel.setAlignment(Qt.AlignHCenter)
        self.panel.setAlignment(Qt.AlignVCenter)

    class TimerStatus(enum.Enum):
        init, counting, paused = 1, 2, 3




