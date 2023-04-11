from my_message_box import MyDualMessageBox, MySingleMessageBox, MyQuadrupleMessageBox
from model.piece_type import PieceType
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
import pickle
from _thread import *

from network.my_string import MyString


class MessageBox:

    @staticmethod
    def stalemate_message_box(game):
        """
        The message box to be shown in case of stalemate

        :param game: the object to represent the current game
        """

        msgbox = MyDualMessageBox("The result of the game is stalemate",
                                  b1_text="Start a new game",
                                  b2_text="Return to main menu")
        msgbox.questionLabel.setAlignment(QtCore.Qt.AlignCenter)

        msgbox.btn1.clicked.connect(lambda: MessageBox.__start_new_game(game, msgbox))
        msgbox.btn2.clicked.connect(lambda: MessageBox.__return_to_main_menu(game.widget, msgbox))

        msgbox.exec_()

    @staticmethod
    def checkmate_message_box(game, game_result):
        """
        The message box to be shown in case of checkmate

        :param game: the object to represent the current game
        :param game_result: the result of current game
        """

        game_result = game_result + "'s victory"

        msgbox = MyDualMessageBox("CheckMate!\nThe result of the game is: " + game_result,
                                  b1_text="Start a new game",
                                  b2_text="Return to main menu")
        msgbox.questionLabel.setAlignment(QtCore.Qt.AlignCenter)

        msgbox.btn1.clicked.connect(lambda: MessageBox.__start_new_game(game, msgbox))
        msgbox.btn2.clicked.connect(lambda: MessageBox.__return_to_main_menu(game.widget, msgbox))

        return msgbox

    @staticmethod
    def end_game_message_box(game, game_result):
        """
        The message box to be shown in case the game finishes by a button being pressed

        :param game: the object to represent the current game
        :param game_result: the result of current game
        """

        if game_result != "Draw":
            game_result = game_result + "'s victory"

        msgbox = MyDualMessageBox("The result of the game is: " + game_result,
                                  b1_text="Start a new game",
                                  b2_text="Return to main menu")
        msgbox.questionLabel.setAlignment(QtCore.Qt.AlignCenter)

        msgbox.btn1.clicked.connect(lambda: MessageBox.__start_new_game(game, msgbox))
        msgbox.btn2.clicked.connect(lambda: MessageBox.__return_to_main_menu(game.widget, msgbox))

        msgbox.exec_()

    @staticmethod
    def make_enemy_surrender_message_box(game, player_name, enemy_player_name):
        """
        The message box to be shown in case someone asks the other player if he/she would like to surrender

        :param game: the object to represent the current game
        :param player_name: the name of the initiating person
        :param enemy_player_name: the name of the opponent
        """

        msgbox = MyDualMessageBox("Do " + enemy_player_name + " want to surrender?")
        msgbox.questionLabel.setAlignment(QtCore.Qt.AlignCenter)

        def on_btn1_click():
            """
            The actions in case btn1 is clicked
            """

            msgbox.close()
            MessageBox.end_game_message_box(game, player_name)

        msgbox.btn1.clicked.connect(on_btn1_click)

        msgbox.exec_()

    @staticmethod
    def draw_request_message_box(game, enemy_player_name):
        """
        The message box to be shown in case someone asks the other player for a draw

        :param game: the object to represent the current game
        :param enemy_player_name: the name of the opponent
        """

        msgbox = MyDualMessageBox("Do " + enemy_player_name + " agree with a draw?")
        msgbox.questionLabel.setAlignment(QtCore.Qt.AlignCenter)

        def on_btn1_click():
            """
            The actions in case btn1 is clicked
            """

            msgbox.close()
            MessageBox.end_game_message_box(game, "Draw")

        msgbox.btn1.clicked.connect(on_btn1_click)

        msgbox.exec_()

    @staticmethod
    def surrender_message_box(game, enemy_player_name):
        """
        The message box to be shown in case someone would like to surrender

        :param game: the object to represent the current game
        :param enemy_player_name: the name of the opponent
        """

        msgbox = MyDualMessageBox("Do you really want to surrender?")
        msgbox.questionLabel.setAlignment(QtCore.Qt.AlignCenter)

        def on_btn1_click():
            """
            The actions in case btn1 is clicked
            """

            msgbox.close()
            MessageBox.end_game_message_box(game, enemy_player_name)

        msgbox.btn1.clicked.connect(on_btn1_click)

        msgbox.exec_()

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
    def promote_message_box(game, cell, gui_cell):
        """
        The message box to be shown in case a pawn must be promoted

        :param game: the object to represent the current game
        :param cell: the cell of the pawn
        :param gui_cell: the cell's representation in GUI
        """

        msgbox = MyQuadrupleMessageBox("Choose the type of piece you would like to promote the pawn to")
        msgbox.questionLabel.setAlignment(QtCore.Qt.AlignCenter)

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
        current.__init__(widget, name1, name2)
        widget.addWidget(current)
        widget.setCurrentIndex(widget.currentIndex() + 1)



    @staticmethod
    def __return_to_main_menu(widget, msgbox):
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

        if cell.get_piece().get_direction() == 1:
            pixmap = QPixmap("./resource_images/pieces/w_queen.png")
        else:
            pixmap = QPixmap("./resource_images/pieces/b_queen.png")
        gui_cell.setPixmap(pixmap)

    @staticmethod
    def promote_to_rook(cell, gui_cell):

        if cell.get_piece().get_direction() == 1:
            pixmap = QPixmap("./resource_images/pieces/w_rook.png")
        else:
            pixmap = QPixmap("./resource_images/pieces/b_rook.png")
        gui_cell.setPixmap(pixmap)

    @staticmethod
    def promote_to_bishop(cell, gui_cell):

        if cell.get_piece().get_direction() == 1:
            pixmap = QPixmap("./resource_images/pieces/w_bishop.png")
        else:
            pixmap = QPixmap("./resource_images/pieces/b_bishop.png")
        gui_cell.setPixmap(pixmap)

    @staticmethod
    def promote_to_knight(cell, gui_cell):

        if cell.get_piece().get_direction() == 1:
            pixmap = QPixmap("./resource_images/pieces/w_knight.png")
        else:
            pixmap = QPixmap("./resource_images/pieces/b_knight.png")
        gui_cell.setPixmap(pixmap)
