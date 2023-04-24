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
    """
    A class to represent a timer for the match
    """

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
        """
        Decreases the timer value by 1 and shows the current time.
        If the timer value is zero, stops the timer
        """
        if self._left_seconds > 0:
            self._left_seconds -= 1
            self.show_time()
        else:
            self.timer.stop()
            self.show_time()

    def start_timer(self):
        """
        Starts the timer
        """
        if self._left_seconds > 0:

            self._left_seconds -= 1
            self._status = self.TimerStatus.counting
            self.show_time()
            self.timer.start(1000)

    def stop_timer(self):
        """
        Stops the timer
        """
        self.timer.stop()
        self._status = self.TimerStatus.paused

    def show_time(self):
        """
        Shows the time on the timer in mm:ss form
        """
        minutes = self._left_seconds // 60
        seconds = self._left_seconds - (minutes * 60)

        self.panel.setText("{:02}:{:02}".format(int(minutes), int(seconds)))
        self.panel.setAlignment(Qt.AlignCenter)

    class TimerStatus(enum.Enum):
        """
        An enum class to represent the possible timer statuses
        """

        init, counting, paused = 1, 2, 3




