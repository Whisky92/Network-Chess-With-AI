from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui
from PyQt5.QtGui import QFont


class ClickableLabel(QLabel):

    clicked = pyqtSignal()

    def __init__(self, parent=QLabel):
        QLabel.__init__(self, parent=parent)

    def mousePressEvent(self, event):
        """
        A function to perceive when a mouse event happens

        :param event: the event that occured
        """
        self.clicked.emit()
