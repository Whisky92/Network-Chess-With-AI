import socket

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
from gui.message_box import MessageBox
import threading


class MultiPlayerMenu(QDialog):
    """
    A class to represent the multiplayer menu of the gui
    """
    def __init__(self, widget):

        super(MultiPlayerMenu, self).__init__()
        loadUi("resource_ui_files/multiplayer_menu.ui", self)

        self.host_btn = self.findChild(QPushButton, "hostButton")
        self.host_btn.clicked.connect(lambda: change_ui(PlayerOneNameChoose(widget), widget))
        self.host_btn.resizeEvent = self.resizeText

        self.join_btn = self.findChild(QPushButton, "joinByIpButton")
        self.join_btn.clicked.connect(lambda: change_ui(IpChooseMenu(widget), widget))

        self.backButton.clicked.connect(lambda: on_back_btn_pressed(widget))

    def resizeText(self, event: QEvent):
        """
        Determines text resizing in case the window size changes

        :param event: the event that occurs
        """

        resize(self, [self.backButton, self.host_btn, self.join_btn])


class PlayerOneNameChoose(QDialog):
    """
    A class to represent a menu where host can start a server
    """
    def __init__(self, widget):

        super(PlayerOneNameChoose, self).__init__()
        loadUi("resource_ui_files/host_game.ui", self)

        self.backButton.clicked.connect(lambda: on_back_btn_pressed(widget))
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
            int(time) > 0 and ip != "" and \
                (re.search("((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}", ip)
                 or ip == "localhost"):

            correct = True
            try:
                conn = socket.gethostbyaddr(ip)
            except:
                MessageBox.connection_error_message_box()
                correct = False

            if correct:
                server_network = Network(ip)
                start_new_thread(server.start_server, (ip,))

                loop = QEventLoop()
                QTimer.singleShot(1500, loop.quit)
                loop.exec_()

                server_network.connect()

                names = server_network.send_object(MyString(text))

                change_ui(ReadyMenu(server_network, widget, names, time), widget)

    def resizeText(self, event: QEvent):
        """
        Determines text resizing in case the window size changes

        :param event: the event that occurs
        """

        resize(self, [self.backButton, self.submitButton, self.ipField, self.time, self.nameField])


class IpChooseMenu(QDialog):
    """
    A class to represent a menu where client can join a server
    """

    def __init__(self, widget):

        super(IpChooseMenu, self).__init__()
        loadUi("resource_ui_files/join_ip.ui", self)

        self.submitButton.clicked.connect(lambda: self.connect(widget))
        self.submitButton.resizeEvent = self.resizeText
        self.backButton.clicked.connect(lambda: on_back_btn_pressed(widget))

    def connect(self, widget):
        """
        The actions to be done in case the submit button was pressed
        """

        ip = self.ipField.text()
        name = self.nameField.text()

        if ip != "" and \
                (re.search("((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}", ip) or ip == "localhost"):

            client_network = Network(ip)

            if client_network.connect():

                loop = QEventLoop()
                QTimer.singleShot(1500, loop.quit)
                loop.exec_()

                names = client_network.send_object(MyString(name))

                if name != "" and names[0] != name:

                    change_ui(ReadyMenu(client_network, widget, names), widget)

                    self.nameField.setText("")
                    self.ipField.setText("")

            else:
                MessageBox.connection_error_message_box()

    def resizeText(self, event: QEvent):
        """
        Determines text resizing in case the window size changes

        :param event: the event that occurs
        """

        resize(self, [self.backButton, self.submitButton, self.ipField, self.nameField])


class ReadyMenu(QDialog):
    """
    A class to represent the game lobby
    """

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

        self.backButton.clicked.connect(lambda: on_back_btn_pressed(widget))

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
        """
        Starts the game for the second player (on main thread)

        :param value: the parameter is just there to make it possible to invoke on main thread
        """
        change_ui(NetworkGameWindow(self.widget, self.rolls[0], self.rolls[1],
                                    self.owned_checkbox.text(), self.time, False, self.server_network), self.widget)

    def start_game(self, current_player):
        """
        Starts the game in case the current player is the host

        :param current_player: the current player
        """
        if current_player == "p1" and self.p1_checkbox.isChecked() and self.p2_checkbox.isChecked():

            self.server_network.send_object(MyString("ready"))
            self.stop = True
            change_ui(NetworkGameWindow(self.widget, self.rolls[0], self.rolls[1],
                                   self.owned_checkbox.text(), self.time, False, self.server_network), self.widget)

    def wait_for_other_player(self, owned_checkbox, not_owned_checkbox):
        """
        Starts a while cycle to wait for another player to connect the lobby

        :param owned_checkbox: the checkbox owned by the current player
        :param not_owned_checkbox: the checkbox not owned by the current player

        :return: signal when game can start
        """
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
        """
        Continuously checks the state of checkboxes and returns when game starts

        :param owned_checkbox: the checkbox owned by the current player
        :param not_owned_checkbox: the checkbox not owned by the current player

        :return: signal when gama can start
        """

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





