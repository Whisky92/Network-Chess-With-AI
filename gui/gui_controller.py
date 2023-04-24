from PyQt5.uic import loadUi
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLabel, QSizePolicy
from gui.change_ui_and_font import change_ui, resize, on_back_btn_pressed
from gui.game_window import GameWindow
from gui.online_play_controller import MultiPlayerMenu
from gui.ai_game_window import AiGameWindow
from gui.statistic_row import StatisticRow
import sys
import sqlite3


class MainWindow(QDialog):
    """
    A class to represent the main menu of the ui
    """

    def __init__(self):

        super(MainWindow, self).__init__()
        loadUi("resource_ui_files/main_menu.ui", self)

        self.local_pvp_button = self.findChild(QPushButton, "localPlayerVsPlayerButton")
        self.local_play_vs_ai_button = self.findChild(QPushButton, "playerVsAiButton")
        self.online_pvp_button = self.findChild(QPushButton, "onlinePlayerVsPlayerButton")
        self.match_history_button = self.findChild(QPushButton, "matchHistoryButton")

        self.local_pvp_button.clicked.connect(lambda: change_ui(PlayerOneNameChoose(widget), widget))
        self.local_pvp_button.resizeEvent = self.resizeText

        self.local_play_vs_ai_button.clicked.connect(lambda: change_ui(PlayVsAiNameChoose(widget), widget))

        self.online_pvp_button.clicked.connect(lambda: change_ui(MultiPlayerMenu(widget), widget))

        self.match_history_button.clicked.connect(lambda: change_ui(Statistics(widget), widget))

    def resizeText(self, event: QEvent):
        """
        Determines text resizing in case the window size changes

        :param event: the event that occurs
        """

        resize(self, [self.local_pvp_button, self.local_play_vs_ai_button,
                      self.online_pvp_button, self.match_history_button])


class Statistics(QDialog):
    def __init__(self, widget):

        super(Statistics, self).__init__()
        loadUi("resource_ui_files/statistics.ui", self)

        conn = sqlite3.connect('stats.db')
        c = conn.cursor()

        c.execute("""CREATE TABLE if not exists statistics(
            id integer PRIMARY KEY,
            p1 text NOT NULL,
            p2 text NOT NULL,
            game_result text NOT NULL
        ); """)

        c.execute("SELECT * FROM statistics")
        records = c.fetchall()

        for record in records:
            self.statContainer.addWidget(StatisticRow(str(record[1]), str(record[2]), str(record[3])))

        conn.commit()
        conn.close()

        self.backButton.clicked.connect(lambda: on_back_btn_pressed(widget))
        self.backButton.resizeEvent = self.resizeText

        self.installEventFilter(self)

    def resizeText(self, event: QEvent):
        """
        Determines text resizing in case the window size changes

        :param event: the event that occurs
        """

        resize(self, [self.backButton])


class PlayVsAiNameChoose(QDialog):

    def __init__(self, widget):
        super(PlayVsAiNameChoose, self).__init__()
        loadUi("resource_ui_files/player1_name_choose.ui", self)

        self.backButton.clicked.connect(lambda: on_back_btn_pressed(widget))
        self.submitButton.clicked.connect(self.submit)
        self.submitButton.resizeEvent = self.resizeText

    def submit(self):
        """
        The actions to be done in case the submit button was pressed
        """

        text = self.nameField.text()

        if text != "":
            change_ui(AiGameWindow(widget, text, True), widget)
            self.nameField.setText("")

    def resizeText(self, event: QEvent):
        """
        Determines text resizing in case the window size changes

        :param event: the event that occurs
        """

        resize(self, [self.submitButton, self.backButton, self.nameField])


class PlayerOneNameChoose(QDialog):
    def __init__(self, widget):

        super(PlayerOneNameChoose, self).__init__()
        loadUi("resource_ui_files/player1_name_choose.ui", self)

        self.backButton.clicked.connect(lambda: on_back_btn_pressed(widget))
        self.submitButton.clicked.connect(self.submit)
        self.submitButton.resizeEvent = self.resizeText

    def submit(self):
        """
        The actions to be done in case the submit button was pressed
        """

        text = self.nameField.text()

        if text != "":

            change_ui(PlayerTwoNameChoose(text, widget), widget)
            self.nameField.setText("")

    def resizeText(self, event: QEvent):
        """
        Determines text resizing in case the window size changes

        :param event: the event that occurs
        """

        resize(self, [self.submitButton, self.backButton, self.nameField])


class PlayerTwoNameChoose(QDialog):

    def __init__(self, player_1_name, widget):

        super(PlayerTwoNameChoose, self).__init__()
        loadUi("resource_ui_files/player2_name_choose.ui", self)

        self.backButton.clicked.connect(lambda: on_back_btn_pressed(widget))
        self.submitButton.clicked.connect(lambda: self.submit(player_1_name))
        self.submitButton.resizeEvent = self.resizeText

    def submit(self, player_1_name):
        """
        The actions to be done in case submit button was pressed
        """

        text = self.nameField.text()

        if text != "" and player_1_name != text:

            change_ui(TimeSet(player_1_name, text, widget), widget)
            self.nameField.setText("")

    def resizeText(self, event: QEvent):
        """
        Determines text resizing in case the window size changes

        :param event: the event that occurs
        """

        resize(self, [self.submitButton, self.backButton, self.nameField])


class TimeSet(QDialog):

    def __init__(self, p1_name, p2_name, widget):

        super(TimeSet, self).__init__()
        loadUi("resource_ui_files/time_set.ui", self)

        self.backButton.clicked.connect(lambda: on_back_btn_pressed(widget))
        self.submitButton.clicked.connect(lambda: self.submit(p1_name, p2_name))
        self.submitButton.resizeEvent = self.resizeText

    def submit(self, player_1_name, player_2_name):
        """
        The actions to be done in case submit button was pressed
        """

        if self.timeInMinutes.text() is not None and self.timeInMinutes.text().isdigit() and \
            int(self.timeInMinutes.text()) > 0:

            time = 120 if int(self.timeInMinutes.text()) > 120 else int(self.timeInMinutes.text())

            change_ui(GameWindow(widget, player_1_name, player_2_name, time, True), widget)

    def resizeText(self, event: QEvent):
        """
        Determines text resizing in case the window size changes

        :param event: the event that occurs
        """

        resize(self, [self.submitButton, self.backButton, self.timeInMinutes])


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
main_window = MainWindow()

widget.addWidget(main_window)
widget.show()

try:
    sys.exit(app.exec_())
except Exception:
    print("Exiting")
