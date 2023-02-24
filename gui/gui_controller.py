import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton
from game_window import GameWindow


class MainWindow(QDialog):
    def __init__(self):

        super(MainWindow, self).__init__()
        loadUi("resource_ui_files/main_menu.ui", self)

        self.local_pvp_button = self.findChild(QPushButton, "localPlayerVsPlayerButton")
        self.local_pvp_button.clicked.connect(self.play_local_pvp)

    def play_local_pvp(self):

        screen = PlayerOneNameChoose()
        widget.addWidget(screen)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class PlayerOneNameChoose(QDialog):
    def __init__(self):

        super(PlayerOneNameChoose, self).__init__()
        loadUi("resource_ui_files/player1_name_choose.ui", self)

        self.backButton.clicked.connect(self.back_to_previous_page)
        self.submitButton.clicked.connect(self.submit)

    def back_to_previous_page(self):

        current = widget.currentWidget()
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.removeWidget(current)

    def submit(self):

        text = self.nameField.text()
        if text != "":
            screen = PlayerTwoNameChoose(text)
            widget.addWidget(screen)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            self.nameField.setText("")



class PlayerTwoNameChoose(QDialog):
    def __init__(self, player_1_name):

        super(PlayerTwoNameChoose, self).__init__()
        loadUi("resource_ui_files/player2_name_choose.ui", self)

        self.backButton.clicked.connect(self.back_to_previous_page)
        self.submitButton.clicked.connect(lambda: self.submit(player_1_name))

    def back_to_previous_page(self):

        current = widget.currentWidget()
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.removeWidget(current)

    def submit(self, player_1_name):

        text = self.nameField.text()
        if text != "":
            screen = GameWindow(player_1_name, text)
            widget.addWidget(screen)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            self.nameField.setText("")


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
main_window = MainWindow()

widget.addWidget(main_window)
widget.show()

try:
    sys.exit(app.exec_())
except Exception:
    print("Exiting")
