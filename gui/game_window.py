import sys
import random
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QWidget, QGridLayout, QLabel
from model.game import Game
from model.piece_type import PieceType
from PyQt5.QtWidgets import QSizePolicy

class GameWindow(QDialog):
    def __init__(self, player_1_name, player_2_name):

        super(GameWindow, self).__init__()
        loadUi("resource_ui_files/game.ui", self)

        self.game = Game()

        self.fill_name_labels(player_1_name, player_2_name)
        self.fill_board()

    def get_first_player(self, player_1_name, player_2_name):
        names = [player_1_name, player_2_name]
        return random.choice(names)

    def fill_name_labels(self, player_1_name, player_2_name):
        if self.get_first_player(player_1_name, player_2_name) == player_1_name:
            self.player1Name.setText(player_1_name)
            self.player2Name.setText(player_2_name)
        else:
            self.player1Name.setText(player_2_name)
            self.player2Name.setText(player_1_name)

    def fill_board(self):
        layout: QGridLayout = self.gameLayout
        for i in range(0, 8):
            for j in range(0, 8):

                item: QLabel = layout.itemAtPosition(i, j).widget()
                cell_type = self.game.get_board_table()[i][j].get_piece().get_piece_type()
                direction = self.game.get_board_table()[i][j].get_piece().get_direction()

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




