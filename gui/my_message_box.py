from PyQt5 import QtWidgets, uic, QtCore, QtGui
import sys
from PyQt5.QtWidgets import QTextEdit, QFrame
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt


class MyDualMessageBox(QtWidgets.QDialog):

    def __init__(self, title, b1_text="Yes", b2_text="No"):

        QtWidgets.QDialog.__init__(self)
        uic.loadUi("resource_ui_files/message_box.ui", self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.questionLabel: QTextEdit
        self.questionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.questionLabel.setText(title)

        self.btn1.setText(b1_text)
        self.btn2.setText(b2_text)

        self.questionLabel.setFrameStyle(QFrame.NoFrame)
        self.questionLabel.viewport().setAutoFillBackground(False)
        p = self.questionLabel.palette()
        p.setColor(QPalette.Base, QColor(0, 0, 0, 0))
        self.questionLabel.setPalette(p)

        self.questionLabel.setText(title)

        radius = 20
        path = QtGui.QPainterPath()

        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)

        self.btn2.clicked.connect(self.close)


class MySingleMessageBox(QtWidgets.QDialog):

    def __init__(self, title):

        QtWidgets.QDialog.__init__(self)
        uic.loadUi("resource_ui_files/single_message_box.ui", self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.questionLabel: QTextEdit
        self.questionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.questionLabel.setText(title)

        self.btn.setText("OK")

        self.questionLabel.setFrameStyle(QFrame.NoFrame)
        self.questionLabel.viewport().setAutoFillBackground(False)
        p = self.questionLabel.palette()
        p.setColor(QPalette.Base, QColor(0, 0, 0, 0))
        self.questionLabel.setPalette(p)

        self.questionLabel.setText(title)

        radius = 20
        path = QtGui.QPainterPath()

        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)

        self.btn.clicked.connect(self.close)


class MyQuadrupleMessageBox(QtWidgets.QDialog):

    def __init__(self, title):

        QtWidgets.QDialog.__init__(self)
        uic.loadUi("resource_ui_files/quadruple_message_box.ui", self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.questionLabel: QTextEdit
        self.questionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.questionLabel.setText(title)

        self.questionLabel.setFrameStyle(QFrame.NoFrame)
        self.questionLabel.viewport().setAutoFillBackground(False)
        p = self.questionLabel.palette()
        p.setColor(QPalette.Base, QColor(0, 0, 0, 0))
        self.questionLabel.setPalette(p)

        self.questionLabel.setText(title)

        radius = 20
        path = QtGui.QPainterPath()

        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)
