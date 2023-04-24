from model.piece_type import PieceType
from gui.my_message_box import MyDualMessageBox, MySingleMessageBox, MyQuadrupleMessageBox, MyStepRecognitionMessageBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QSizePolicy, QPushButton
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from step_recognition.step_recognition import StepRecognition
import sqlite3
import webbrowser


class MessageBox:
    """
    A class to represent the message boxes to be shown
    """

    @staticmethod
    def step_recognition_box(game):
        """
        A message box to be shown in case the step recognition button was pressed

        :param game: the current game
        """
        msgbox = MyStepRecognitionMessageBox()

        game_steps = game.get_steps()

        for key, value in StepRecognition.popular_openings.items():
            if value[0] == game_steps:

                btn = QPushButton(key, flat=True)

                btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                btn.setFont(QFont("Times New Roman", 20))

                btn.clicked.connect(lambda: webbrowser.open('https://www.chess.com/openings/' + value[1]))

                msgbox.stepContainer.addWidget(btn)

        msgbox.exec_()

    @staticmethod
    def stalemate_message_box(game, is_offline=True):
        """
        The message box to be shown in case of stalemate

        :param game: the object to represent the current game
        :param is_offline: logical value whether the game is offline or not

        :return: the message box to be shown
        """

        msgbox = MyDualMessageBox("The result of the game is stalemate",
                                  b1_text="Start a new game",
                                  b2_text="Return to main menu")
        msgbox.questionLabel.setAlignment(Qt.AlignCenter)

        MessageBox.insert_to_database(game.player1Name.text(), game.player2Name.text(), "Stalemate")

        msgbox.btn1.clicked.connect(lambda: MessageBox.__start_new_game(game, msgbox))
        msgbox.btn2.clicked.connect(lambda: MessageBox.return_to_main_menu(game.widget, msgbox))

        if not is_offline:
            MessageBox.__set_button_stretch(msgbox)

        return msgbox

    @staticmethod
    def checkmate_message_box(game, game_result, is_offline=True):
        """
        The message box to be shown in case of checkmate

        :param game: the object to represent the current game
        :param game_result: the result of current game
        :param is_offline: logical value whether the game is offline or not

        :return: the message box to be shown
        """

        game_result = game_result + "'s victory"

        msgbox = MyDualMessageBox("CheckMate!\nThe result of the game is: " + game_result,
                                  b1_text="Start a new game",
                                  b2_text="Return to main menu")

        return MessageBox.__set_game_ending_message_box_properties(msgbox, game, is_offline, game_result)

    @staticmethod
    def no_more_time_message_box(game, loser, is_offline=True):
        """
        The message box to be shown in case the game finishes by a button being pressed

        :param game: the object to represent the current game
        :param loser: the player who lost the game
        :param is_offline: logical value whether the game is offline or not

        :return: the message box to be shown
        """
        winner = game.player1Name.text() if loser == game.player2Name.text() else game.player2Name.text()
        game_result = winner + "'s victory"

        msgbox = MyDualMessageBox("Time is up! The result of the game is: " + game_result,
                                  b1_text="Start a new game",
                                  b2_text="Return to main menu")

        return MessageBox.__set_game_ending_message_box_properties(msgbox, game, is_offline, game_result)

    @staticmethod
    def end_game_message_box(game, game_result, is_offline=True):
        """
        The message box to be shown in case the game finishes by a button being pressed

        :param game: the object to represent the current game
        :param game_result: the result of current game
        :param is_offline: logical value whether the game is offline or not

        :return: the message box to be shown
        """

        if game_result != "Draw":
            game_result = game_result + "'s victory"

        msgbox = MyDualMessageBox("The result of the game is: " + game_result,
                                  b1_text="Start a new game",
                                  b2_text="Return to main menu")

        return MessageBox.__set_game_ending_message_box_properties(msgbox, game, is_offline, game_result)

    @staticmethod
    def make_enemy_surrender_message_box(game, player_name, enemy_player_name):
        """
        The message box to be shown in case someone asks the other player if he/she would like to surrender

        :param game: the object to represent the current game
        :param player_name: the name of the initiating person
        :param enemy_player_name: the name of the opponent
        """

        msgbox = MyDualMessageBox("Do " + enemy_player_name + " want to surrender?")
        msgbox.questionLabel.setAlignment(Qt.AlignCenter)

        def on_btn1_click():
            """
            The actions in case btn1 is clicked
            """

            msgbox.close()
            MessageBox.end_game_message_box(game, player_name).exec_()

        msgbox.btn1.clicked.connect(on_btn1_click)

        msgbox.exec_()

    @staticmethod
    def draw_request_message_box(game, enemy_player_name):
        """
        The message box to be shown in case someone asks the other player for a draw

        :param game: the object to represent the current game
        :param enemy_player_name: the name of the opponent

        :return: the message box to be shown
        """

        msgbox = MyDualMessageBox("Do " + enemy_player_name + " agree with a draw?")
        msgbox.questionLabel.setAlignment(Qt.AlignCenter)

        def on_btn1_click():
            """
            The actions in case btn1 is clicked
            """

            msgbox.close()
            MessageBox.end_game_message_box(game, "Draw").exec_()

        msgbox.btn1.clicked.connect(on_btn1_click)

        return msgbox

    @staticmethod
    def surrender_message_box(game, enemy_player_name):
        """
        The message box to be shown in case someone would like to surrender

        :param game: the object to represent the current game
        :param enemy_player_name: the name of the opponent

        :return: the message box to be shown
        """

        msgbox = MyDualMessageBox("Do you really want to surrender?")
        msgbox.questionLabel.setAlignment(Qt.AlignCenter)

        def on_btn1_click():
            """
            The actions in case btn1 is clicked
            """

            msgbox.close()
            MessageBox.end_game_message_box(game, enemy_player_name).exec_()

        msgbox.btn1.clicked.connect(on_btn1_click)

        return msgbox

    @staticmethod
    def still_check_message_box():
        """
        The message box to be shown in case stepping with the selected piece would not free the king from check
        """

        msgbox = MySingleMessageBox("Your king is in check.\nYou can't step with this piece.")

        msgbox.exec_()

    @staticmethod
    def check_message_box(game):
        """
        The message box to be shown in case the current player's king is in check

        :param game: the object to represent the current game
        """

        name = game.player1Name.text() if game.game.get_current_player() == game.game.get_white_player() \
            else game.player2Name.text()

        msgbox = MySingleMessageBox(name + "!\nYour king is in check.")
        msgbox.exec_()

    @staticmethod
    def connection_error_message_box():
        """
        The message box to be shown in case of connection error
        """

        msgbox = MySingleMessageBox("Error occurred during connection")
        msgbox.exec_()

    @staticmethod
    def promote_message_box(game, cell, gui_cell):
        """
        The message box to be shown in case a pawn must be promoted

        :param game: the object to represent the current game
        :param cell: the cell of the pawn
        :param gui_cell: the cell's representation in GUI
        """

        msgbox = MyQuadrupleMessageBox("Choose the type of piece you would like to promote the pawn to")
        msgbox.questionLabel.setAlignment(Qt.AlignCenter)

        def on_btn1_clicked():
            """
            The actions in case btn1 is clicked
            """

            game.game.promote_pawn(cell, PieceType.QUEEN)

            MessageBox.promote_to_queen(cell, gui_cell)

            msgbox.close()

        def on_btn2_clicked():
            """
            The actions in case btn2 is clicked
            """

            game.game.promote_pawn(cell, PieceType.ROOK)

            MessageBox.promote_to_rook(cell, gui_cell)

            msgbox.close()

        def on_btn3_clicked():
            """
            The actions in case btn3 is clicked
            """

            game.game.promote_pawn(cell, PieceType.BISHOP)

            MessageBox.promote_to_bishop(cell, gui_cell)

            msgbox.close()

        def on_btn4_clicked():
            """
            The actions in case btn4 is clicked
            """

            game.game.promote_pawn(cell, PieceType.KNIGHT)

            MessageBox.promote_to_knight(cell, gui_cell)

            msgbox.close()

        msgbox.btn1.clicked.connect(on_btn1_clicked)
        msgbox.btn2.clicked.connect(on_btn2_clicked)
        msgbox.btn3.clicked.connect(on_btn3_clicked)
        msgbox.btn4.clicked.connect(on_btn4_clicked)

        msgbox.exec_()

    @staticmethod
    def __start_new_game(game, msgbox):
        """
        Starts a new game

        :param game: the object to represent the current game
        :param msgbox: the message box to be closed
        """

        msgbox.close()

        current = game
        widget = game.widget
        name1 = game.player1Name.text()
        name2 = game.player2Name.text()

        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.removeWidget(game)
        current.__init__(widget, name1, name2, current.time, True)
        widget.addWidget(current)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    @staticmethod
    def return_to_main_menu(widget, msgbox):
        """
        Starts a new game

        :param widget: the widget containing the representation of the current game
        :param msgbox: the message box to be closed
        """

        msgbox.close()

        for i in range(widget.currentIndex(), 0, -1):

            current = widget.currentWidget()
            widget.setCurrentIndex(widget.currentIndex() - 1)
            widget.removeWidget(current)

    @staticmethod
    def promote_to_queen(cell, gui_cell):
        """
        Promotes the piece of the given cell to a queen

        :param cell: the cell's representation in the model
        :param gui_cell: the cell in the gui
        """

        if cell.get_piece().get_direction() == 1:
            pixmap = QPixmap("./resource_images/pieces/w_queen.png")
        else:
            pixmap = QPixmap("./resource_images/pieces/b_queen.png")
        gui_cell.setPixmap(pixmap)

    @staticmethod
    def promote_to_rook(cell, gui_cell):
        """
        Promotes the piece of the given cell to a rook

        :param cell: the cell's representation in the model
        :param gui_cell: the cell in the gui
        """

        if cell.get_piece().get_direction() == 1:
            pixmap = QPixmap("./resource_images/pieces/w_rook.png")
        else:
            pixmap = QPixmap("./resource_images/pieces/b_rook.png")
        gui_cell.setPixmap(pixmap)

    @staticmethod
    def promote_to_bishop(cell, gui_cell):
        """
        Promotes the piece of the given cell to a bishop

        :param cell: the cell's representation in the model
        :param gui_cell: the cell in the gui
        """

        if cell.get_piece().get_direction() == 1:
            pixmap = QPixmap("./resource_images/pieces/w_bishop.png")
        else:
            pixmap = QPixmap("./resource_images/pieces/b_bishop.png")
        gui_cell.setPixmap(pixmap)

    @staticmethod
    def promote_to_knight(cell, gui_cell):
        """
        Promotes the piece of the given cell to a queen

        :param cell: the cell's representation in the model
        :param gui_cell: the cell in the gui
        """

        if cell.get_piece().get_direction() == 1:
            pixmap = QPixmap("./resource_images/pieces/w_knight.png")
        else:
            pixmap = QPixmap("./resource_images/pieces/b_knight.png")
        gui_cell.setPixmap(pixmap)

    @staticmethod
    def __set_game_ending_message_box_properties(msgbox, game, is_offline, game_result):

        msgbox.questionLabel.setAlignment(Qt.AlignCenter)

        MessageBox.insert_to_database(game.player1Name.text(), game.player2Name.text(), game_result)

        msgbox.btn1.clicked.connect(lambda: MessageBox.__start_new_game(game, msgbox))
        msgbox.btn2.clicked.connect(lambda: MessageBox.return_to_main_menu(game.widget, msgbox))

        if not is_offline:
            MessageBox.__set_button_stretch(msgbox)

        return msgbox

    @staticmethod
    def __set_button_stretch(msgbox):
        """
        Sets the stretch in the given message box in online games
        to hide "Start a new game" option

        :param msgbox:
        :return:
        """

        msgbox.btn1.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        msgbox.btn2.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        msgbox.horizontalLayout.setStretch(0, 0)
        msgbox.horizontalLayout.setStretch(1, 0)
        msgbox.horizontalLayout.setStretch(2, 1)
        msgbox.horizontalLayout.setStretch(3, 2)
        msgbox.horizontalLayout.setStretch(4, 1)

    @staticmethod
    def insert_to_database(p1, p2, result):
        """
        Creates the database (if it does not exist)
        and insert the current result into it

        :param p1: the game's first player
        :param p2: the game's second player
        :param result: the result of the game
        """
        conn = sqlite3.connect('stats.db')
        c = conn.cursor()

        c.execute("""CREATE TABLE if not exists statistics(
            id integer PRIMARY KEY,
            p1 text NOT NULL,
            p2 text NOT NULL,
            game_result text NOT NULL
        ); """)

        insert_command = """INSERT INTO statistics
                          (p1, p2, game_result) 
                          VALUES (?, ?, ?);"""

        c.execute(insert_command, (p1, p2, result))

        conn.commit()
        conn.close()



