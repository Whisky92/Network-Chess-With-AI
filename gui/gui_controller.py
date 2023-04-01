import sys
from PyQt5.uic import loadUi
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton
from game_window import GameWindow
from online_play_controller import MultiPlayerMenu


class MainWindow(QDialog):
    def __init__(self):

        super(MainWindow, self).__init__()
        loadUi("resource_ui_files/main_menu.ui", self)

        self.local_pvp_button = self.findChild(QPushButton, "localPlayerVsPlayerButton")
        self.online_pvp_button = self.findChild(QPushButton, "onlinePlayerVsPlayerButton")

        self.local_pvp_button.clicked.connect(self.play_local_pvp)
        self.local_pvp_button.resizeEvent = self.resizeText

        self.online_pvp_button.clicked.connect(self.play_online_pvp)

    def play_local_pvp(self):
        """
        The actions to be done in case the local pvp button was pressed
        """

        screen = PlayerOneNameChoose()
        widget.addWidget(screen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def play_online_pvp(self):
        """
        The actions to be done in case the online pvp button was pressed
        """

        screen = MultiPlayerMenu(widget)
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

        self.local_pvp_button.setFont(f)
        self.matchHistoryButton.setFont(f)
        self.playerVsAiButton.setFont(f)
        self.onlinePlayerVsPlayerButton.setFont(f)


class PlayerOneNameChoose(QDialog):
    def __init__(self):

        super(PlayerOneNameChoose, self).__init__()
        loadUi("resource_ui_files/player1_name_choose.ui", self)

        self.backButton.clicked.connect(self.back_to_previous_page)
        self.submitButton.clicked.connect(self.submit)
        self.submitButton.resizeEvent = self.resizeText

    def back_to_previous_page(self):
        """
        The actions to be done in case the back button was pressed
        """

        current = widget.currentWidget()
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.removeWidget(current)

    def submit(self):
        """
        The actions to be done in case the submit button was pressed
        """

        text = self.nameField.text()

        if text != "":

            screen = PlayerTwoNameChoose(text)
            widget.addWidget(screen)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            self.nameField.setText("")

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


class PlayerTwoNameChoose(QDialog):

    def __init__(self, player_1_name):

        super(PlayerTwoNameChoose, self).__init__()
        loadUi("resource_ui_files/player2_name_choose.ui", self)

        self.backButton.clicked.connect(self.back_to_previous_page)
        self.submitButton.clicked.connect(lambda: self.submit(player_1_name))
        self.submitButton.resizeEvent = self.resizeText

    def back_to_previous_page(self):
        """
        The actions to be done in case the back button was pressed
        """

        current = widget.currentWidget()
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.removeWidget(current)

    def submit(self, player_1_name):
        """
        The actions to be done in case submit button was pressed
        """

        text = self.nameField.text()

        if text != "" and player_1_name != text:

            screen = GameWindow(widget, player_1_name, text, True)
            widget.addWidget(screen)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            self.nameField.setText("")

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


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
main_window = MainWindow()

widget.addWidget(main_window)
widget.show()

try:
    sys.exit(app.exec_())
except Exception:
    print("Exiting")
