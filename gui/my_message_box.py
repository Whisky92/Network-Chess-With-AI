from PyQt5 import QtWidgets, uic, QtCore, QtGui
import sys
from PyQt5.QtWidgets import QTextEdit, QFrame
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt


def set_message_box_properties(msgbox, title):
    """
    Sets the properties of message boxes
    """

    msgbox.setWindowFlag(Qt.FramelessWindowHint)
    msgbox.setWindowModality(Qt.ApplicationModal)

    msgbox.questionLabel: QTextEdit

    msgbox.questionLabel.setAlignment(Qt.AlignCenter)
    msgbox.questionLabel.setText(title)
    msgbox.questionLabel.setFrameStyle(QFrame.NoFrame)
    msgbox.questionLabel.viewport().setAutoFillBackground(False)
    msgbox.questionLabel.setText(title)
    msgbox.questionLabel.setReadOnly(True)

    p = msgbox.questionLabel.palette()
    p.setColor(QPalette.Base, QColor(0, 0, 0, 0))
    msgbox.questionLabel.setPalette(p)

    radius = 20
    path = QtGui.QPainterPath()

    path.addRoundedRect(QtCore.QRectF(msgbox.rect()), radius, radius)
    mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
    msgbox.setMask(mask)


class MyStepRecognitionMessageBox(QtWidgets.QDialog):
    """
    A class to represent a message box that is shown in case
    step recognition was pressed
    """

    def __init__(self):

        QtWidgets.QDialog.__init__(self)
        uic.loadUi("resource_ui_files/step_show_box.ui", self)


class MyDualMessageBox(QtWidgets.QDialog):
    """
    A class to represent a message box with two buttons
    """

    def __init__(self, title, b1_text="Yes", b2_text="No"):

        QtWidgets.QDialog.__init__(self)
        uic.loadUi("resource_ui_files/message_box.ui", self)

        set_message_box_properties(self, title)

        self.btn1.setText(b1_text)
        self.btn2.setText(b2_text)

        self.btn2.clicked.connect(self.close)


class MySingleMessageBox(QtWidgets.QDialog):
    """
    A class to represent a message box with one button
    """
    def __init__(self, title):

        QtWidgets.QDialog.__init__(self)
        uic.loadUi("resource_ui_files/single_message_box.ui", self)

        set_message_box_properties(self, title)

        self.btn.setText("OK")

        self.btn.clicked.connect(self.close)


class MyQuadrupleMessageBox(QtWidgets.QDialog):
    """
    A class to represent a message box with four buttons
    """

    def __init__(self, title):

        QtWidgets.QDialog.__init__(self)
        uic.loadUi("resource_ui_files/quadruple_message_box.ui", self)

        set_message_box_properties(self, title)
