from PyQt5.uic import loadUi
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLabel, QSizePolicy
from gui.game_window import GameWindow
from gui.online_play_controller import MultiPlayerMenu
from gui.ai_game_window import AiGameWindow
from gui.statistic_row import StatisticRow
import sys
import sqlite3


class MainWindow(QDialog):
    def __init__(self):

        super(MainWindow, self).__init__()
        loadUi("resource_ui_files/main_menu.ui", self)

        self.local_pvp_button = self.findChild(QPushButton, "localPlayerVsPlayerButton")
        self.local_play_vs_ai_button = self.findChild(QPushButton, "playerVsAiButton")
        self.online_pvp_button = self.findChild(QPushButton, "onlinePlayerVsPlayerButton")
        self.match_history_button = self.findChild(QPushButton, "matchHistoryButton")

        self.local_pvp_button.clicked.connect(self.play_local_pvp)
        self.local_pvp_button.resizeEvent = self.resizeText

        self.local_play_vs_ai_button.clicked.connect(self.play_against_ai)

        self.online_pvp_button.clicked.connect(self.play_online_pvp)

        self.match_history_button.clicked.connect(self.check_statistics)

    def play_local_pvp(self):
        """
        The actions to be done in case the local pvp button was pressed
        """

        screen = PlayerOneNameChoose()
        widget.addWidget(screen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def play_against_ai(self):
        """
        The actions to be done in case the local play vs AI button was pressed
        """

        screen = PlayVsAiNameChoose()
        widget.addWidget(screen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def play_online_pvp(self):
        """
        The actions to be done in case the online pvp button was pressed
        """

        screen = MultiPlayerMenu(widget)
        widget.addWidget(screen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def check_statistics(self):
        """
        The actions to be done in case the match history button was pressed
        """
        screen = Statistics()
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


class Statistics(QDialog):
    def __init__(self):

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

        self.backButton.clicked.connect(self.back_to_previous_page)
        self.backButton.resizeEvent = self.resizeText
    def back_to_previous_page(self):
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


class PlayVsAiNameChoose(QDialog):

    def __init__(self):
        super(PlayVsAiNameChoose, self).__init__()
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

            screen = AiSetTime(text)
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


class AiSetTime(QDialog):
    def __init__(self, p1_name):

        super(AiSetTime, self).__init__()
        loadUi("resource_ui_files/time_set.ui", self)

        self.backButton.clicked.connect(self.back_to_previous_page)
        self.submitButton.clicked.connect(lambda: self.submit(p1_name))
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

        if self.timeInMinutes.text() is not None and self.timeInMinutes.text().isdigit() and \
            int(self.timeInMinutes.text()) > 0:

            time = 120 if int(self.timeInMinutes.text()) > 120 else int(self.timeInMinutes.text())

            screen = AiGameWindow(widget, player_1_name, time, True)
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

        self.backButton.setFont(f)
        self.submitButton.setFont(f)


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

            screen = TimeSet(player_1_name, text)
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

class TimeSet(QDialog):

    def __init__(self, p1_name, p2_name):

        super(TimeSet, self).__init__()
        loadUi("resource_ui_files/time_set.ui", self)

        self.backButton.clicked.connect(self.back_to_previous_page)
        self.submitButton.clicked.connect(lambda: self.submit(p1_name, p2_name))
        self.submitButton.resizeEvent = self.resizeText

    def back_to_previous_page(self):
        """
        The actions to be done in case the back button was pressed
        """

        current = widget.currentWidget()
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.removeWidget(current)

    def submit(self, player_1_name, player_2_name):
        """
        The actions to be done in case submit button was pressed
        """

        if self.timeInMinutes.text() is not None and self.timeInMinutes.text().isdigit() and \
            int(self.timeInMinutes.text()) > 0:

            time = 120 if int(self.timeInMinutes.text()) > 120 else int(self.timeInMinutes.text())

            screen = GameWindow(widget, player_1_name, player_2_name, time, True)
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
