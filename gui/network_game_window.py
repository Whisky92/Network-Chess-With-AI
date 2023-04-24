from model.piece_type import PieceType
from PyQt5 import QtCore
from gui.message_box import MessageBox
from time import sleep
from gui.game_window import GameWindow
from network.my_string import MyString
from _thread import start_new_thread
from model.game import Game


class NetworkGameWindow(GameWindow):
    """
    A class to represent an online game in the gui
    """

    socketSignal = QtCore.pyqtSignal(object)

    def __init__(self, widget, player_1_name, player_2_name, owned_player_name, time, yet_to_decide, server_network):
        GameWindow.__init__(self, widget, player_1_name, player_2_name, time, yet_to_decide)

        self.owned_player_name = owned_player_name
        self.server_network = server_network

        self.player_1_name = player_1_name
        self.player_2_name = player_2_name

        self.current_received_steps = []
        self.pawn_type = []

        self.socketSignal.connect(self.handle_server_responses_of_message_boxes)

        start_new_thread(self.check_board_of_other_player, ())

    def handle_server_responses_of_message_boxes(self, message):
        """
        Does the appropriate action in case a message box must be shown

        :param message: the message indicating the message box to be shown
        """
        enemy = self.player1Name.text() if self.owned_player_name == self.player2Name.text() \
            else self.player2Name.text()

        if message[0] == "make_enemy_surrender":
            box = MessageBox.surrender_message_box(self, enemy)

            self.manage_box(box, enemy)

        elif message[0] == "draw_request":
            box = MessageBox.draw_request_message_box(self, enemy)

            self.manage_box(box, enemy)

        elif message[0] == "check":
            MessageBox.check_message_box(self)

        elif message[0] == "end_of_game":
            MessageBox.end_game_message_box(self, message[1], False).exec_()

        elif message[0] == "checkmate":
            winner = self.player2Name.text() if self.game.get_current_player() == self.game.get_white_player() \
                else self.player1Name.text()

            self.server_network.send_object([self.owned_player_name, "checkmate"])
            box = MessageBox.checkmate_message_box(self, winner, False)
            self.return_to_main_menu(box)

        elif message[0] == "stalemate":

            self.server_network.send_object([self.owned_player_name, "stalemate"])
            box = MessageBox.stalemate_message_box(self, False)
            self.return_to_main_menu(box)

    def return_to_main_menu(self, box):
        """
        Handles actions in case the "Return to main menu" button was pressed

        :param box: the message box to be shown
        """

        box.btn1.clicked.disconnect()
        box.btn2.clicked.disconnect()

        def on_btn1_click():
            """
            The actions in case btn1 is clicked
            """

            self.server_network.client.close()
            MessageBox.return_to_main_menu(self.widget, box)

        box.btn2.clicked.connect(on_btn1_click)

        box.exec_()

    def set_click_listeners_of_p1(self):
        """
        Sets the click listeners of action buttons of player 1
        """

        self.makePlayer2Surrender.clicked.connect(self.on_make_enemy_surrender)
        self.player1DrawRequest.clicked.connect(self.on_draw_request)
        self.player1Surrender.clicked.connect(self.on_surrender)
        self.player1StepInfo.clicked.connect(self.on_step_info)

    def set_click_listeners_of_p2(self):
        """
        Sets the click listeners of action buttons of player 2
        """

        self.makePlayer1Surrender.clicked.connect(self.on_make_enemy_surrender)
        self.player2DrawRequest.clicked.connect(self.on_draw_request)
        self.player2Surrender.clicked.connect(self.on_surrender)
        self.player2StepInfo.clicked.connect(self.on_step_info)

    def check_board_of_other_player(self):
        """
        Continuously communicates with the server to get information
        about the enemy player's board state and message boxes
        """
        while True:

            sleep(1)
            received_steps = self.server_network.send_board(MyString("get_steps"))

            if len(received_steps) != 0 and received_steps[1] != self.owned_player_name and \
                    received_steps != self.current_received_steps:

                self.make_other_player_pieces_move(received_steps)

            self.timers[self.game.get_current_player()].start_timer()
            message = self.server_network.send_object(MyString(self.owned_player_name))

            if len(message) != 0:
                self.socketSignal.emit(message)
                if message[0] in ["checkmate", "stalemate"]:
                    return

    def make_other_player_pieces_move(self, received_steps):
        """
        Moves the pieces of the other player in case if it is possible

        :param received_steps: the answer from the server
        """

        self.current_received_steps = received_steps
        start_cell = self.game.get_board_table()[received_steps[0][0]][received_steps[0][1]]

        if start_cell in self.king_start_cells:
            target_cell = self.game.get_board_table()[received_steps[0][2]][received_steps[0][3]]

            self.set_castling_properties(start_cell, target_cell)

        self.make_move(received_steps[0][0], received_steps[0][1], received_steps[0][2], received_steps[0][3])

        if len(received_steps[2]) != 0:
            self.promote_other_player_pieces(received_steps)

    def promote_other_player_pieces(self, received_steps):
        """
        Promotes the other player's pawns in case if it is possible

        :param received_steps:
        """

        self.game.get_board_table()[received_steps[0][2]][received_steps[0][3]].get_piece() \
            .set_piece_type(received_steps[2][0])
        self.promote_in_gui(received_steps[2][0],
                            self.game.get_board_table()[received_steps[0][2]][received_steps[0][3]],
                            self.board.itemAtPosition(received_steps[0][2], received_steps[0][3]).widget())

    def promote_in_gui(self, p_type, cell, gui_cell):
        """
        Does the pawn promotion in gui

        :param p_type: the type to promote the pawn to
        :param cell: the cell of the piece
        :param gui_cell: the cell in gui
        """
        if p_type == PieceType.QUEEN:
            MessageBox.promote_to_queen(cell, gui_cell)

        elif p_type == PieceType.ROOK:
            MessageBox.promote_to_rook(cell, gui_cell)

        elif p_type == PieceType.BISHOP:
            MessageBox.promote_to_bishop(cell, gui_cell)

        else:
            MessageBox.promote_to_knight(cell, gui_cell)

    @QtCore.pyqtSlot()
    def make_step(self):
        """
        Moves the selected piece to the desired cell, if it is possible
        """

        current_player_name = self.player1Name.text() if self.game.get_current_player() == self.game.get_white_player() \
            else self.player2Name.text()

        if current_player_name == self.owned_player_name:
            GameWindow.make_step(self)

            if self.step_was_made:
                self.step_was_made = False
                self.server_network.send_object([self.current_step_cells, self.owned_player_name, self.pawn_type])
                self.pawn_type = []

    def check_game_ending_conditions(self):
        """
        Checks whether the game reached a state in which a game finishes, like stalemate and checkmate
        """

        if self.game.is_stalemate():
            self.server_network.send_object([self.owned_player_name, "stalemate"])

        if self.game.is_king_targeted(self.game.get_current_player()):
            for i in self.colored_cells:
                i.setStyleSheet(i.styleSheet().replace("background-color: #3F704D", ""))
            self.colored_cells = []

            if len(self.game.steps_if_king_is_targeted()) == 0:
                winner = self.player2Name.text() if self.game.get_current_player() == self.game.get_white_player() \
                    else self.player1Name.text()
                self.server_network.send_object([self.owned_player_name, "checkmate"])
                return

            self.server_network.send_object([self.owned_player_name, "check"])

    def promote_pawn(self, target_cell, target):
        """
        Promotes the pawn if possible

        :param target_cell: the target cell
        :param target: the target cell in gui
        """
        GameWindow.promote_pawn(self, target_cell, target)
        self.pawn_type.append(target_cell.get_piece().get_piece_type())

    @QtCore.pyqtSlot()
    def on_draw_request(self):
        """
        Handles actions in case the draw request button was pressed
        """

        target = self.sender()

        if (target == self.player1DrawRequest and self.owned_player_name == self.player_1_name) or \
                (target == self.player2DrawRequest and self.owned_player_name == self.player_2_name):

            self.server_network.send_object([self.owned_player_name, "draw_request"])

    @QtCore.pyqtSlot()
    def on_make_enemy_surrender(self):
        """
        Handles actions in case the "make enemy surrender" button was pressed
        """

        target = self.sender()

        if (target == self.makePlayer2Surrender and self.owned_player_name == self.player_1_name) or \
                (target == self.makePlayer1Surrender and self.owned_player_name == self.player_2_name):

            self.server_network.send_object([self.owned_player_name, "make_enemy_surrender"])

    @QtCore.pyqtSlot()
    def on_step_info(self):
        """
        Handles actions in case the step info button was pressed
        """

        target = self.sender()

        if (target == self.player1StepInfo and self.owned_player_name == self.player_1_name) or \
                (target == self.player2StepInfo and self.owned_player_name == self.player_2_name):

            MessageBox.step_recognition_box(self.game)

    @QtCore.pyqtSlot()
    def on_surrender(self):
        """
        Handles actions in case the surrender button was pressed
        """

        target = self.sender()

        if (target == self.player1Surrender and self.owned_player_name == self.player_1_name) or \
                (target == self.player2Surrender and self.owned_player_name == self.player_2_name):

            enemy = self.player1Name.text() if self.owned_player_name == self.player2Name.text() \
                else self.player2Name.text()

            box = MessageBox.surrender_message_box(self, enemy)

            self.manage_box(box, enemy)

    def manage_box(self, box, enemy):
        """
        Handles actions in case of surrender

        :param box: the message box to be shown
        :param enemy: the enemy player
        """
        box.btn1.clicked.disconnect()

        if box.questionLabel.toPlainText() == ("Do " + enemy + " agree with a draw?"):
            enemy = "Draw"

        def surrender_with_button():
            """
            Sends data to the server about the surrender to notify the other player
            """

            box.close()

            start_new_thread(self.server_network.send_object, ([self.owned_player_name, "end_of_game", enemy],))
            MessageBox.end_game_message_box(self, enemy, False).exec_()

        box.btn1.clicked.connect(surrender_with_button)

        box.exec_()




