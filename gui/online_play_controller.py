from PyQt5.uic import loadUi
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets
from PyQt5.QtCore import QEvent, QEventLoop, QTimer, pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QCheckBox
import network.server as server
from network.network import Network
from _thread import *
import re
import socket
from time import sleep
from network.network_messages import NetworkMessages
from network.my_string import MyString

server_network = Network("localhost")


class MultiPlayerMenu(QDialog):
    def __init__(self, widget):

        super(MultiPlayerMenu, self).__init__()
        loadUi("resource_ui_files/multiplayer_menu.ui", self)

        self.host_btn = self.findChild(QPushButton, "hostButton")
        self.host_btn.clicked.connect(lambda: self.host_game(widget))
        self.host_btn.resizeEvent = self.resizeText

        self.join_btn = self.findChild(QPushButton, "joinByIpButton")
        self.join_btn.clicked.connect(lambda: self.join_game(widget))

        self.backButton.clicked.connect(lambda: self.back_to_previous_page(widget))

    def host_game(self, widget):

        screen = PlayerOneNameChoose(widget)
        widget.addWidget(screen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def join_game(self, widget):

        screen = IpChooseMenu(widget)
        widget.addWidget(screen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

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
        self.backButton.setFont(f)

    def back_to_previous_page(self, widget):
        """
        The actions to be done in case the back button was pressed
        """

        current = widget.currentWidget()
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.removeWidget(current)


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

            server_network.connect()
            names = server_network.send_object(MyString(text))
            print(names)
            screen = ReadyMenu(widget, names)
            print("hello")
            widget.addWidget(screen)
            print("megyen")
            widget.setCurrentIndex(widget.currentIndex() + 1)

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


class IpChooseMenu(QDialog):

    def __init__(self, widget):

        super(IpChooseMenu, self).__init__()
        loadUi("resource_ui_files/join_ip.ui", self)

        self.submitButton.clicked.connect(lambda: self.connect(widget))
        self.backButton.clicked.connect(lambda: self.back_to_previous_page(widget))

    def connect(self, widget):
        """
        The actions to be done in case the submit button was pressed
        """

        ip = self.ipField.text()
        name = self.nameField.text()

        if ip != "" and \
                (re.search("((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}", ip) or ip == "localhost"):
            print("true")

            client_network = Network(ip)
            client_network.connect()

            loop = QEventLoop()
            QTimer.singleShot(1500, loop.quit)
            loop.exec_()

            names = client_network.send_object(MyString(name))

            print(names)
            if name != "" and names[0] != name:
                print("megyenősös megyen")
                screen = ReadyMenu(widget, names)
                widget.addWidget(screen)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                self.nameField.setText("")
                self.ipField.setText("")

    def back_to_previous_page(self, widget):
        """
        The actions to be done in case the back button was pressed
        """

        current = widget.currentWidget()
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.removeWidget(current)


class ReadyMenu(QDialog):
    def __init__(self, widget, players):

        super(ReadyMenu, self).__init__()
        loadUi("resource_ui_files/ready_menu.ui", self)
        self.p1_checkbox = self.findChild(QCheckBox, "player1_cb")
        self.p1_checkbox.setText(players[0])

        self.p2_checkbox: QCheckBox = self.findChild(QCheckBox, "player2_cb")

        self.p1_checkbox.clicked.connect(self.on_click)

        if players[1] != "":
            self.p2_checkbox.setText(players[1])
        else:
            print("megyenget")
            start_new_thread(self.wait_for_other_player, ())

    def wait_for_other_player(self):
        while True:
            try:
                sleep(1)
                print("amegyen")
                arr = server_network.send_object(MyString("wait"))
                print(arr)
                if arr[1] != "":
                    print("letsgooo")
                    self.p2_checkbox.setText(arr[1])
                    self.p2_checkbox.update()
                    break

            except:
                break

    @pyqtSlot()
    def on_click(self):

        self.p1_checkbox.setChecked(False)

    def p2_join(self, p2_name):
        self.p2_checkbox.setText(p2_name)

