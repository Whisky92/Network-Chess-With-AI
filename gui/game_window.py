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
from clickable_label import ClickableLabel


class GameWindow(QDialog):
    def __init__(self, widget, player_1_name, player_2_name, yet_to_decide):

        super(GameWindow, self).__init__()
        loadUi("resource_ui_files/game.ui", self)

        self.widget = widget
        self.game = Game()

        self.boardWidget: QWidget = self.gameBoard
        self.board: QGridLayout = self.gameLayout

        self.__fill_name_labels(player_1_name, player_2_name, yet_to_decide)
        self.fill_board()

        self.colored_cells = []
        self.current_piece = None

        self.player1Name: QLabel
        self.player2Name: QLabel

        self.player_1_current_capture_cell = 0
        self.player_2_current_capture_cell = 0

        self.current_step_cells = []
        self.step_was_made = False

        self.player1Surrender.clicked.connect(lambda: MessageBox.surrender_message_box(self, self.player2Name.text()))
        self.player2Surrender.clicked.connect(lambda: MessageBox.surrender_message_box(self, self.player1Name.text()))

        self.player1DrawRequest.clicked.connect(lambda: MessageBox.draw_request_message_box(self, self.player2Name.text()))
        self.player2DrawRequest.clicked.connect(lambda: MessageBox.draw_request_message_box(self, self.player1Name.text()))

        self.makePlayer1Surrender.clicked.connect(lambda:
                                                  MessageBox.make_enemy_surrender_message_box(self,
                                                                                              self.player2Name.text(),
                                                                                              self.player1Name.text(),
))
        self.makePlayer2Surrender.clicked.connect(lambda:
                                                  MessageBox.make_enemy_surrender_message_box(self,
                                                                                              self.player1Name.text(),
                                                                                              self.player2Name.text()))
        self.player1Name.resizeEvent = self.resizeText

        self.step_progress = 1

    def __fill_name_labels(self, player_1_name, player_2_name, yet_to_decide):
        """
        Fills the name labels with the appropriate player's name

        :param player_1_name: the name of the 1'st player
        :param player_2_name: the name of the 2'nd player
        """

        if (GameWindow.get_first_player(player_1_name, player_2_name) == player_1_name) or (not yet_to_decide):
            self.player1Name.setText(player_1_name)
            self.player2Name.setText(player_2_name)
        else:
            self.player1Name.setText(player_2_name)
            self.player2Name.setText(player_1_name)

    def fill_board(self):
        """
        Fills the game board with piece images
        """

        for i in range(0, 8):
            for j in range(0, 8):

                item = self.board.itemAtPosition(i, j).widget()
                print(type(item))
                cell_type = self.game.get_board_table()[i][j].get_piece().get_piece_type()
                direction = self.game.get_board_table()[i][j].get_piece().get_direction()
                item.clicked.connect(self.make_step)

                pixmap = None

                if cell_type == PieceType.PAWN and direction == 1:
                    pixmap = QPixmap("./resource_images/pieces/w_pawn.png")
                elif cell_type == PieceType.PAWN and direction == -1:
                    pixmap = QPixmap("./resource_images/pieces/b_pawn.png")
                elif cell_type == PieceType.ROOK and direction == 1:
                    pixmap = QPixmap("./resource_images/pieces/w_rook.png")
                elif cell_type == PieceType.ROOK and direction == -1:
                    pixmap = QPixmap("./resource_images/pieces/b_rook.png")
                elif cell_type == PieceType.KNIGHT and direction == 1:
                    pixmap = QPixmap("./resource_images/pieces/w_knight.png")
                elif cell_type == PieceType.KNIGHT and direction == -1:
                    pixmap = QPixmap("./resource_images/pieces/b_knight.png")
                elif cell_type == PieceType.BISHOP and direction == 1:
                    pixmap = QPixmap("./resource_images/pieces/w_bishop.png")
                elif cell_type == PieceType.BISHOP and direction == -1:
                    pixmap = QPixmap("./resource_images/pieces/b_bishop.png")
                elif cell_type == PieceType.KING and direction == 1:
                    pixmap = QPixmap("./resource_images/pieces/w_king.png")
                elif cell_type == PieceType.KING and direction == -1:
                    pixmap = QPixmap("./resource_images/pieces/b_king.png")
                elif cell_type == PieceType.QUEEN and direction == 1:
                    pixmap = QPixmap("./resource_images/pieces/w_queen.png")
                elif cell_type == PieceType.QUEEN and direction == -1:
                    pixmap = QPixmap("./resource_images/pieces/b_queen.png")

                if pixmap is not None:
                    item.setPixmap(pixmap)

    @staticmethod
    def get_first_player(player_1_name, player_2_name):
        """
        Rolls the first player between player1 and player2

        :param player_1_name: the name of the first player
        :param player_2_name: the name of the second player

        :return: the rolled first player between the two
        """
        names = [player_1_name, player_2_name]
        return random.choice(names)

    @QtCore.pyqtSlot()
    def make_step(self):
        """
        Moves the selected piece to the desired cell, if it is possible
        """
        target = self.sender()

        pos = self.board.getItemPosition(self.board.indexOf(target))
        pos_x = pos[0]
        pos_y = pos[1]

        if self.step_progress == 1:
            self.__if_step_progress_is_one(target, pos_x, pos_y)

        else:
            self.__if_step_progress_is_two(target, pos_x, pos_y)

    def __if_step_progress_is_one(self, target, pos_x, pos_y):
        """
        Does the necessary processes if 'self.step_progress' is 1

        :param target: the selected cell
        :param pos_x: the target's x coordinate
        :param pos_y: the target's y coordinate
        """

        if self.__is_correct_position(pos_x, pos_y):

            if self.game.is_king_targeted(self.game.get_current_player()):

                cell = self.game.get_board_table()[pos_x][pos_y]

                cells = self.game.steps_if_king_is_targeted()

                if len(cells) != 0:

                    current_check_counter_start = self.game.contains_start_cell(cells, cell)

                    if current_check_counter_start is None:
                        MessageBox.still_check_message_box()
                        return

                    else:
                        self.__mark_possible_steps(current_check_counter_start[1])

            else:
                self.__mark_possible_steps(self.game.filter_wrong_moves(pos_x, pos_y))
            self.step_progress = 2
            self.current_piece = target

    def __if_step_progress_is_two(self, target, pos_x, pos_y):
        """
        Does the necessary processes if 'self.step_progress' is 2

        :param target: the selected cell
        :param pos_x: the target's x coordinate
        :param pos_y: the target's y coordinate
        """

        if "background-color: #3F704D" in target.styleSheet():
            start_pos = self.board.getItemPosition(self.board.indexOf(self.current_piece))

            start_cell = self.game.get_board_table()[start_pos[0]][start_pos[1]]
            target_cell = self.game.get_board_table()[pos_x][pos_y]

            self.make_move(start_pos[0], start_pos[1], pos_x, pos_y)
            self.current_step_cells = [start_pos[0], start_pos[1], pos_x, pos_y]
            self.step_was_made = True

            if target_cell.get_piece().get_direction() == 1:
                enemy_border = 0
            else:
                enemy_border = 7

            if target_cell.get_piece().get_piece_type() == PieceType.PAWN and \
                    target_cell.get_piece().get_piece_x() == enemy_border:

                self.promote_pawn(target_cell, target)

            self.check_game_ending_conditions()

        self.step_progress = 1

        for i in self.colored_cells:
            i.setStyleSheet(i.styleSheet().replace("background-color: #3F704D", ""))
        self.colored_cells = []

    def promote_pawn(self, target_cell, target):
        MessageBox.promote_message_box(self, target_cell, target)

    def make_move(self, start_x, start_y, target_x, target_y):

        start_cell = self.game.get_board_table()[start_x][start_y]
        target_cell = self.game.get_board_table()[target_x][target_y]

        if start_cell.get_piece().get_en_passant_step() is not None and target_cell == \
                start_cell.get_piece().get_en_passant_step():

            self.__step_in_case_of_en_passant_step(start_cell, target_cell)
        elif target_cell in self.game.get_castling_step():

            self.__step_in_case_of_castling_step(start_cell, target_cell)

        self.__normal_step(start_x, start_y, target_x, target_y)

    def __step_in_case_of_en_passant_step(self, start_cell, target_cell):
        """
        Does the necessary processes if the current step is an en-passant step

        :param start_cell: the cell to move from
        :param target_cell: the cell to move to
        """

        cell_to_capture_from_y = target_cell.get_piece().get_piece_y()
        cell_to_capture_from_x = target_cell.get_piece().get_piece_x() + 1 \
                                 * start_cell.get_piece().get_direction()

        cell_to_capture_from = self.board.itemAtPosition(cell_to_capture_from_x, cell_to_capture_from_y) \
            .widget()

        self.__capture(cell_to_capture_from.pixmap())
        cell_to_capture_from.clear()
        cell_to_capture_from.update()

    def __step_in_case_of_castling_step(self, start_cell, target_cell):
        """
        Does the necessary processes if the current step is a castling step

        :param start_cell: the cell to move from
        :param target_cell: the cell to move to
        """

        index = Game.get_index_of_item(self.game.get_castling_step(), target_cell)

        x = start_cell.get_piece().get_piece_x()

        rook_start_y = self.game.get_castling_rook()[index].get_piece().get_piece_y()
        rook_start_pos = self.board.itemAtPosition(x, rook_start_y).widget()

        rook_target_y = self.game.get_rook_target()[index].get_piece().get_piece_y()
        rook_target_pos = self.board.itemAtPosition(x, rook_target_y).widget()

        rook_target_pos.setPixmap(rook_start_pos.pixmap())
        rook_start_pos.clear()
        rook_start_pos.update()

    def __normal_step(self, start_x, start_y, target_x, target_y):
        """
        Moves the target piece from the 'start_cell' to 'target_cell'

        :param start_cell: the cell to move from
        :param target_cell: the cell to move to
        :param target: the target cell's representation in the GUI
        """

        start_cell = self.game.get_board_table()[start_x][start_y]
        start_c = self.board.itemAtPosition(start_x, start_y).widget()

        target_cell = self.game.get_board_table()[target_x][target_y]
        target_c = self.board.itemAtPosition(target_x, target_y).widget()

        print(start_c, "start_c")
        print(target_c, "target_c")

        start_pixmap = start_c.pixmap()
        target_pixmap = target_c.pixmap()

        if target_pixmap is not None:
            self.__capture(target_pixmap)

        target_c.setPixmap(start_pixmap)
        start_c.clear()
        start_c.update()

        self.game.move_piece(start_cell, target_cell)

    def check_game_ending_conditions(self):
        """
        Checks whether the game reached a state in which a game finishes, like stalemate and checkmate
        """

        if self.game.is_stalemate():
            MessageBox.stalemate_message_box(self)

        if self.game.is_king_targeted(self.game.get_current_player()):
            for i in self.colored_cells:
                i.setStyleSheet(i.styleSheet().replace("background-color: #3F704D", ""))
            self.colored_cells = []

            if len(self.game.steps_if_king_is_targeted()) == 0:
                winner = self.player2Name.text() if self.game.get_current_player() == self.game.get_white_player() \
                    else self.player1Name.text()
                MessageBox.checkmate_message_box(self, winner)
                return

            MessageBox.check_message_box(self)

    def __capture(self, target_pixmap):
        """
        Captures the piece image from the target cell

        :param target_pixmap: the piece image to be captured
        """

        target_board = self.player1CapturedPiecesLayout \
            if self.game.get_current_player() == self.game.get_black_player() else \
            self.player2CapturedPiecesLayout

        if target_board == self.player1CapturedPiecesLayout:
            x_coord = self.player_1_current_capture_cell // 4
            y_coord = self.player_1_current_capture_cell % 4

            self.player_1_current_capture_cell += 1

        else:
            x_coord = self.player_2_current_capture_cell // 4
            y_coord = self.player_2_current_capture_cell % 4

            self.player_2_current_capture_cell += 1

        item = target_board.itemAtPosition(x_coord, y_coord).widget()
        item.setPixmap(target_pixmap)

    def __mark_possible_steps(self, cells):
        """
        Recolors the cells in the list to green

        :param cells: the array of cells to be colored
        """

        for i in cells:
            piece = i.get_piece()
            item = self.board.itemAtPosition(piece.get_piece_x(), piece.get_piece_y()).widget()
            item.setStyleSheet(item.styleSheet() + "background-color: #3F704D")
            self.colored_cells.append(item)

    def __is_correct_position(self, pos_x, pos_y):
        """
        Checks whether the cell of given coordinates is a legal target cell

        :param pos_x: the x coordinate of the target cell
        :param pos_y: the y coordinate of the target cell

        :return: the logical value whether the target cell is a legal target
        """

        owned_pieces = self.game.get_current_player().get_pieces_on_board()

        for i in owned_pieces:
            if pos_x == i.get_piece_x() and pos_y == i.get_piece_y():
                return True
        return False

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

        self.player1Name.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.player2Name.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        self.player1Name.setFont(f)
        self.player2Name.setFont(f)
