from PyQt5.uic import loadUi
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from PyQt5.QtCore import QEvent, QEventLoop, QTimer
from PyQt5.QtWidgets import QDialog, QPushButton, QCheckBox
import network.server as server
from network.network import Network
from _thread import *
import re
from time import sleep
from network.my_string import MyString
from gui.network_game_window import NetworkGameWindow
from gui.change_ui_and_font import change_ui, resize, on_back_btn_pressed
import threading


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
        loadUi("resource_ui_files/host_game.ui", self)

        self.backButton.clicked.connect(lambda: self.back_to_previous_page(widget))
        self.submitButton.resizeEvent = self.resizeText
        self.submitButton.clicked.connect(lambda: self.submit(widget))

    def submit(self, widget):
        """
        The actions to be done in case the submit button was pressed
        """

        ip = self.ipField.text()
        text = self.nameField.text()
        time = self.time.text()

        if text != "" and time is not None and time.isdigit() and \
            int(time) > 0:
            server_network = Network(ip)
            start_new_thread(server.start_server, (ip,))

            loop = QEventLoop()
            QTimer.singleShot(1500, loop.quit)
            loop.exec_()

            server_network.connect()

            names = server_network.send_object(MyString(text))
            screen = ReadyMenu(server_network, widget, names, time)

            widget.addWidget(screen)
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

        resize(self, [self.backButton, self.submitButton, self.ipField, self.time, self.nameField])


class IpChooseMenu(QDialog):

    def __init__(self, widget):

        super(IpChooseMenu, self).__init__()
        loadUi("resource_ui_files/join_ip.ui", self)

        self.submitButton.clicked.connect(lambda: self.connect(widget))
        self.submitButton.resizeEvent = self.resizeText
        self.backButton.clicked.connect(lambda: self.back_to_previous_page(widget))

    def connect(self, widget):
        """
        The actions to be done in case the submit button was pressed
        """

        ip = self.ipField.text()
        name = self.nameField.text()

        if ip != "" and \
                (re.search("((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}", ip) or ip == "localhost"):

            client_network = Network(ip)
            client_network.connect()

            loop = QEventLoop()
            QTimer.singleShot(1500, loop.quit)
            loop.exec_()

            names = client_network.send_object(MyString(name))

            if name != "" and names[0] != name:

                screen = ReadyMenu(client_network, widget, names)
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

    def resizeText(self, event: QEvent):
        """
        Determines text resizing in case the window size changes

        :param event: the event that occurs
        """

        resize(self, [self.backButton, self.submitButton, self.ipField, self.nameField])


class ReadyMenu(QDialog):

    rolled_players = []
    socketSignal = QtCore.pyqtSignal(object)

    def __init__(self, server_network, widget, players, time=None):

        super(ReadyMenu, self).__init__()
        loadUi("resource_ui_files/ready_menu.ui", self)

        self.server_network = server_network

        self.p1_checkbox: QCheckBox = self.findChild(QCheckBox, "player1_cb")
        self.p1_checkbox.setText(players[0])

        self.p2_checkbox: QCheckBox = self.findChild(QCheckBox, "player2_cb")

        self.submit_btn = self.findChild(QPushButton, "submitButton")
        self.submit_btn.resizeEvent = self.resizeText

        self.widget = widget
        self.players = players

        self.time: str

        self.socketSignal.connect(self.change_for_second_player)

        self.stop = False

        self.rolls = ["", ""]

        if players[1] != "":
            current_player = "p2"
            self.owned_checkbox = self.p2_checkbox
            not_owned_checkbox = self.p1_checkbox
            not_owned_checkbox.setDisabled(True)
            self.time = int(self.server_network.send_object(MyString("get_time")).get_string())
            self.p2_checkbox.setText(players[1])
            self.submit_btn.clicked.connect(lambda: self.start_game(current_player))
            thread = threading.Thread(target=self.check_ready, args=(self.owned_checkbox, not_owned_checkbox), daemon=True)
            thread.start()

        else:
            current_player = "p1"
            self.owned_checkbox = self.p1_checkbox
            not_owned_checkbox = self.p2_checkbox
            not_owned_checkbox.setDisabled(True)
            self.time = int(time)
            self.server_network.send_object(MyString(time))
            self.submit_btn.clicked.connect(lambda: self.start_game(current_player))

            start_new_thread(self.wait_for_other_player, (self.owned_checkbox, not_owned_checkbox))

    def resizeText(self, event: QEvent):
        """
        Determines text resizing in case the window size changes

        :param event: the event that occurs
        """

        resize(self, [self.backButton, self.submitButton, self.player1_cb, self.player2_cb])

    def change_for_second_player(self, value):
        self.start()

    def start_game(self, current_player):
        if current_player == "p1" and self.p1_checkbox.isChecked() and self.p2_checkbox.isChecked():

            self.server_network.send_object(MyString("ready"))
            self.stop = True
            self.start()

    def start(self):

        screen = NetworkGameWindow(self.widget, self.rolls[0], self.rolls[1],
                                   self.owned_checkbox.text(), self.time, False, self.server_network)
        self.widget.addWidget(screen)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def wait_for_other_player(self, owned_checkbox, not_owned_checkbox):
        while True:
            try:
                sleep(1)
                arr = self.server_network.send_object(MyString("wait"))

                if arr[1] != "":
                    self.p2_checkbox.setText(arr[1])
                    self.p2_checkbox.update()
                    break

            except:
                break
        return self.check_ready(owned_checkbox, not_owned_checkbox)

    def check_ready(self, owned_checkbox, not_owned_checkbox):
        rolls = self.server_network.send_object(MyString("get_rolls"))
        self.rolls[0] = rolls[0]
        self.rolls[1] = rolls[1]
        while True:
            try:
                sleep(0.5)
                if self.stop:
                    break
                state = "checked" if owned_checkbox.isChecked() else "unchecked"
                arr = self.server_network.send_object(MyString(state)).get_string()
                box_checked = True if arr == "checked" else False
                not_owned_checkbox.setChecked(box_checked)
                not_owned_checkbox.update()

                sleep(0.5)
                if owned_checkbox == self.p2_checkbox:
                    arr2 = self.server_network.send_object(MyString("start_game")).get_string()
                    if arr2 == "yes":
                        self.socketSignal.emit("asdd")
                        break
            except:
                break
        return





