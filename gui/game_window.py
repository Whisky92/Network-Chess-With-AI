import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton

class GameWindow(QDialog):
    def __init__(self, player_1_name, player_2_name):

        super(GameWindow, self).__init__()
        loadUi("resource_ui_files/game.ui", self)