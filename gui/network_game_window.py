import random
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QDialog, QWidget, QGridLayout, QSizePolicy, QLabel
from PyQt5.QtCore import QEvent
import model.tests.test_tables
from model.game import Game
from model.piece_type import PieceType
from PyQt5 import QtCore
from message_box import MessageBox
from time import sleep
from gui.game_window import GameWindow
from network.my_string import MyString
from _thread import start_new_thread
from gui.clickable_label import ClickableLabel


class NetworkGameWindow(GameWindow):

    socketSignal = QtCore.pyqtSignal(object)
    def __init__(self, widget, player_1_name, player_2_name, owned_player_name, yet_to_decide, server_network):
        GameWindow.__init__(self, widget, player_1_name, player_2_name, yet_to_decide)

        self.owned_player_name = owned_player_name
        self.server_network = server_network

        self.socketSignal.connect(self.make_move_for_other_player)
        self.current_received_steps = []

        start_new_thread(self.check_board_of_other_player, ())

    @QtCore.pyqtSlot()
    def make_step(self):
        print("Owned player:", self.owned_player_name)

        current_player_name = self.player1Name.text() if self.game.get_current_player() == self.game.get_white_player() \
            else self.player2Name.text()
        print("Current player:", current_player_name)
        if current_player_name == self.owned_player_name:
            GameWindow.make_step(self)

            if self.step_was_made:
                self.step_was_made = False
                self.server_network.send_object([self.current_step_cells, self.owned_player_name])

            print("valaki mondja már el hogy mi van itt áááááááááááááááááááá")

    def check_board_of_other_player(self):

        while True:
            sleep(1)
            received_steps = self.server_network.send_board(MyString("get_steps"))
            print("beérkezett: ", received_steps)
            print(type(received_steps))

            if len(received_steps) != 0 and received_steps[1] != self.owned_player_name and \
                    received_steps != self.current_received_steps:
                print("helooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
                print("feltétel igaz")
                self.current_received_steps = received_steps
                self.make_move(received_steps[0][0], received_steps[0][1], received_steps[0][2], received_steps[0][3])
            #self.socketSignal.emit(received_steps)

            current_player_name = self.player1Name.text() if self.game.get_current_player() == self.game.get_white_player() \
                else self.player2Name.text()
            print("Current player:", current_player_name)

    def make_move_for_other_player(self, received_steps):
        if len(received_steps) != 0 and received_steps[1] != self.owned_player_name and \
                received_steps != self.current_received_steps:
            print("helooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"
                  "")
            print("feltétel igaz")
            self.current_received_steps = received_steps
            self.make_move(received_steps[0][0], received_steps[0][1], received_steps[0][2], received_steps[0][3])
        return

    def clear_board(self):
        for i in range(0, 8):
            for j in range(0, 8):

                item = self.board.itemAtPosition(i, j).widget()
                item.clear()
                item.update()



