from PyQt5.uic import loadUi
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets
from PyQt5.QtCore import QEvent, QEventLoop, QTimer
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QCheckBox
import network.server as server
from network.network import Network
from _thread import *
import socket


class MultiPlayerMenu(QDialog):
    def __init__(self, widget):

        super(MultiPlayerMenu, self).__init__()
        loadUi("resource_ui_files/multiplayer_menu.ui", self)

        self.host_btn = self.findChild(QPushButton, "hostButton")
        self.host_btn.clicked.connect(lambda: self.host_game(widget))
        self.host_btn.resizeEvent = self.resizeText

        self.join_btn = self.findChild(QPushButton, "joinByIpButton")

    def host_game(self, widget):

        screen = PlayerOneNameChoose(widget)
        widget.addWidget(screen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def join_game(self):

    def resizeText(self, event: QEvent):
        """
        Determines text resizing in case the window size changes

        :param event: the event that occurs
        """

        default_size = 9

        if self.rect().width() // 40 > default_size:
            f = QFont('', self.rect().width() // 40)
        else:
            f = QFont('', default_size)

        self.host_btn.setFont(f)
        self.join_btn.setFont(f)


class PlayerOneNameChoose(QDialog):
    def __init__(self, widget):

        super(PlayerOneNameChoose, self).__init__()
        loadUi("resource_ui_files/player1_name_choose.ui", self)

        self.backButton.clicked.connect(lambda: self.back_to_previous_page(widget))
        self.submitButton.resizeEvent = self.resizeText
        self.submitButton.clicked.connect(lambda: self.submit(widget))

    def submit(self, widget):
        """
        The actions to be done in case the submit button was pressed
        """

        text = self.nameField.text()

        if text != "":

            start_new_thread(server.start_server, ())

            loop = QEventLoop()
            QTimer.singleShot(1500, loop.quit)
            loop.exec_()

            server_network = Network("localhost")
            print(server_network.connect())

            screen = ReadyMenu(widget, text)
            widget.addWidget(screen)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            self.nameField.setText("")

    def back_to_previous_page(self, widget):
        """
        The actions to be done in case the back button was pressed
        """

        current = widget.currentWidget()
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.removeWidget(current)

    def resizeText(self, event: QEvent):
        """
        Determines text resizing in case the window size changes

        :param event: the event that occurs
        """

        default_size = 9

        if self.rect().width() // 40 > default_size:
            f = QFont('', self.rect().width() // 40)
        else:
            f = QFont('', default_size)

        self.backButton.setFont(f)
        self.submitButton.setFont(f)


class ReadyMenu(QDialog):
    def __init__(self, widget, p1_name):

        super(ReadyMenu, self).__init__()
        loadUi("resource_ui_files/ready_menu.ui", self)

        self.p1_checkbox = self.findChild(QCheckBox, "player1_cb")
        self.p1_checkbox.setText(p1_name)

        self.p2_checkbox = self.findChild(QCheckBox, "player2_cb")

    def p2_join(self, p2_name):
        self.p2_checkbox.setText(p2_name)

