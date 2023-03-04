import sys
import random
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap, QMouseEvent
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QWidget, QGridLayout, QLabel
from model.game import Game
from model.piece_type import PieceType
from PyQt5.QtWidgets import QSizePolicy
from gui.clickable_label import ClickableLabel
from PyQt5.QtCore import Qt
from PyQt5 import QtCore



class GameWindow(QDialog):
    def __init__(self, player_1_name, player_2_name):

        super(GameWindow, self).__init__()
        loadUi("resource_ui_files/game.ui", self)

        self.game = Game()

        self.boardWidget: QWidget = self.gameBoard
        self.board: QGridLayout = self.gameLayout

        self.fill_name_labels(player_1_name, player_2_name)
        self.fill_board()

        self.colored_cells = []
        self.current_piece = None

        self.step_progress = 1

    def fill_name_labels(self,  player_1_name, player_2_name):
        if self.get_first_player(player_1_name, player_2_name) == player_1_name:
            self.player1Name.setText(player_1_name)
            self.player2Name.setText(player_2_name)
        else:
            self.player1Name.setText(player_2_name)
            self.player2Name.setText(player_1_name)

    def fill_board(self):

        for i in range(0, 8):
            for j in range(0, 8):

                item = self.board.itemAtPosition(i, j).widget()
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



    def get_first_player(self, player_1_name, player_2_name):
        names = [player_1_name, player_2_name]
        return random.choice(names)

    @QtCore.pyqtSlot()
    def make_step(self):
        target = self.sender()

        pos = self.board.getItemPosition(self.board.indexOf(target))
        pos_x = pos[0]
        pos_y = pos[1]
        print(pos_x, pos_y)

        if self.step_progress == 1:
            if self.__is_correct_position(pos_x, pos_y):

                self.mark_possible_steps(pos_x, pos_y)
                self.step_progress = 2
                self.current_piece = target

        else:
            if "background-color: #3F704D" in target.styleSheet():
                start_pos = self.board.getItemPosition(self.board.indexOf(self.current_piece))

                start_cell = self.game.get_board_table()[start_pos[0]][start_pos[1]]
                target_cell = self.game.get_board_table()[pos_x][pos_y]

                self.game.move_piece(start_cell, target_cell)

                pixmap = self.current_piece.pixmap()
                target.setPixmap(pixmap)
                self.current_piece.clear()
                self.current_piece.update()
            else:
                self.step_progress = 1
            for i in self.colored_cells:
                i.setStyleSheet(i.styleSheet().replace("background-color: #3F704D", ""))
            self.colored_cells = []
            print(self.game.get_current_player())

    def mark_possible_steps(self, pos_x, pos_y):

        cells = self.game.get_possible_steps(pos_x, pos_y)

        for i in cells:
            piece = i.get_piece()
            item = self.board.itemAtPosition(piece.get_piece_x(), piece.get_piece_y()).widget()
            item.setStyleSheet(item.styleSheet() + "background-color: #3F704D")
            self.colored_cells.append(item)






    def __is_correct_position(self, pos_x, pos_y):

        owned_pieces = self.game.get_current_player().get_pieces_on_board()

        for i in owned_pieces:
            if pos_x == i.get_piece_x() and pos_y == i.get_piece_y():
                return True
        return False
