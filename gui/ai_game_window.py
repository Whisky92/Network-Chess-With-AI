import time
from model.colors import Color
from model.piece_type import PieceType
from gui.game_window import GameWindow
from gui.message_box import MessageBox
from ai.ai_logic import AiLogic
from PyQt5 import QtCore


class AiGameWindow(GameWindow):
    """
    A class to represent a game against an AI in the gui
    """

    def __init__(self, widget, player_name, yet_to_decide):
        GameWindow.__init__(self, widget, player_name, "AI", 10, yet_to_decide)

        self.ai_color = Color.WHITE if self.player1Name.text() == "AI" else Color.BLACK
        self.ai_player = self.game.get_white_player() if self.ai_color == Color.WHITE \
            else self.game.get_black_player()

        self.disable_checkboxes()

        AiLogic.set_ai_player(self.ai_color)

        if self.ai_color == Color.WHITE:
            self.move_ai()

    def disable_checkboxes(self):
        """
        Disables the checkboxes, except for the player's surrender
        and step info buttons
        """

        self.makePlayer1Surrender.clicked.disconnect()
        self.makePlayer2Surrender.clicked.disconnect()

        self.player1DrawRequest.clicked.disconnect()
        self.player2DrawRequest.clicked.disconnect()

        if self.ai_color == Color.WHITE:
            self.player1StepInfo.clicked.disconnect()
            self.player1Surrender.clicked.disconnect()
        else:
            self.player2StepInfo.clicked.disconnect()
            self.player2Surrender.clicked.disconnect()

    @QtCore.pyqtSlot()
    def make_step(self):
        """
        Moves the selected piece to the desired cell, if it is possible
        """
        if self.game.get_current_player() != self.ai_player:
            GameWindow.make_step(self)

    def if_step_progress_is_two(self, target, pos_x, pos_y):
        """
        Does the necessary processes if 'self.step_progress' is 2

        :param target: the selected cell
        :param pos_x: the target's x coordinate
        :param pos_y: the target's y coordinate
        """
        correct = GameWindow.if_step_progress_is_two(self, target, pos_x, pos_y)
        if len(correct) != 0:
            self.move_ai()

    def move_ai(self):
        """
        Calculates the AI's best step and moves the appropriate piece
        """

        time.sleep(1)

        ai_step = AiLogic.minimax(self.game.get_board(), 2, self.ai_color, self.game)

        enemy_border = 0 if self.ai_color == Color.WHITE else 7

        start_x = ai_step[1][0]
        start_y = ai_step[1][1]

        target_x = ai_step[2][0]
        target_y = ai_step[2][1]

        start_cell = self.game.get_board_table()[start_x][start_y]

        if start_cell in self.king_start_cells:

            target_cell = self.game.get_board_table()[target_x][target_y]

            self.set_castling_properties(start_cell, target_cell)

        self.make_move(start_x, start_y, target_x, target_y)

        target = self.game.get_board_table()[target_x][target_y]

        if target.get_piece().get_piece_type() == PieceType.PAWN and target_x == enemy_border:
            target.get_piece().set_piece_type(PieceType.QUEEN)
            MessageBox.promote_to_queen(target,
                                        self.board.itemAtPosition(target_x, target_y).widget())

        self.check_game_ending_conditions()



