import random
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QWidget, QGridLayout, QMessageBox, QPushButton
from model.game import Game
from model.piece_type import PieceType
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

        self.player_1_current_capture_cell = 0
        self.player_2_current_capture_cell = 0

        self.player1Surrender.clicked.connect(lambda: self.surrender_message_box(self.player2Name.text()))
        self.player2Surrender.clicked.connect(lambda: self.surrender_message_box(self.player1Name.text()))

        self.player1DrawRequest.clicked.connect(lambda: self.draw_request_message_box(self.player2Name.text()))
        self.player2DrawRequest.clicked.connect(lambda: self.draw_request_message_box(self.player1Name.text()))

        self.makePlayer1Surrender.clicked.connect(lambda:
                                                  self.make_enemy_surrender_message_box(self.player1Name.text()))
        self.makePlayer2Surrender.clicked.connect(lambda:
                                                  self.make_enemy_surrender_message_box(self.player2Name.text()))

        self.step_progress = 1

    def printer(self, megyen):
        print(megyen)

    def fill_name_labels(self,  player_1_name, player_2_name):
        if GameWindow.get_first_player(player_1_name, player_2_name) == player_1_name:
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
    @staticmethod
    def get_first_player(player_1_name, player_2_name):
        names = [player_1_name, player_2_name]
        return random.choice(names)

    @QtCore.pyqtSlot()
    def make_step(self):
        target = self.sender()

        pos = self.board.getItemPosition(self.board.indexOf(target))
        pos_x = pos[0]
        pos_y = pos[1]
        print(pos_x, pos_y)

        cells = self.game.steps_if_king_is_targeted()

        if self.step_progress == 1:
            if self.__is_correct_position(pos_x, pos_y):

                if self.game.is_king_targeted(self.game.get_current_player()):

                    cell = self.game.get_board_table()[pos_x][pos_y]

                    self.game.print_king_targeted_steps()

                    if len(cells) != 0:
                        self.game.print_king_targeted_steps()

                        current_check_counter_start = self.game.contains_start_cell(cells, cell)

                        if current_check_counter_start is None:
                            self.still_check_message_box()
                            return

                        else:
                            self.mark_possible_steps(current_check_counter_start[1])

                else:
                    self.mark_possible_steps(self.game.get_possible_steps(pos_x, pos_y))
                self.step_progress = 2
                self.current_piece = target

        else:
            if "background-color: #3F704D" in target.styleSheet():
                start_pos = self.board.getItemPosition(self.board.indexOf(self.current_piece))

                start_cell = self.game.get_board_table()[start_pos[0]][start_pos[1]]
                target_cell = self.game.get_board_table()[pos_x][pos_y]

                if start_cell.get_piece().get_en_passant_step() is not None and target_cell == \
                        start_cell.get_piece().get_en_passant_step():

                    cell_to_capture_from_y = target_cell.get_piece().get_piece_y()
                    cell_to_capture_from_x = target_cell.get_piece().get_piece_x() + 1\
                                             * start_cell.get_piece().get_direction()

                    cell_to_capture_from = self.board.itemAtPosition(cell_to_capture_from_x, cell_to_capture_from_y)\
                        .widget()

                    self.capture(cell_to_capture_from.pixmap())
                    cell_to_capture_from.clear()
                    cell_to_capture_from.update()

                elif target_cell in self.game.get_castling_step():
                    index = Game.get_index_of_item(self.game.get_castling_step(), target_cell)

                    x = start_cell.get_piece().get_piece_x()

                    rook_start_y = self.game.get_castling_rook()[index].get_piece().get_piece_y()
                    rook_start_pos = self.board.itemAtPosition(x, rook_start_y).widget()

                    rook_target_y = self.game.get_rook_target()[index].get_piece().get_piece_y()
                    rook_target_pos = self.board.itemAtPosition(x, rook_target_y).widget()

                    rook_target_pos.setPixmap(rook_start_pos.pixmap())
                    rook_start_pos.clear()
                    rook_start_pos.update()

                pixmap = self.current_piece.pixmap()
                target_pixmap = target.pixmap()

                if target_pixmap is not None:
                    self.capture(target_pixmap)

                target.setPixmap(pixmap)
                self.current_piece.clear()
                self.current_piece.update()

                self.game.move_piece(start_cell, target_cell)
                if target_cell.get_piece().get_direction() == 1:
                    enemy_border = 0
                else:
                    enemy_border = 7

                if target_cell.get_piece().get_piece_type() == PieceType.PAWN and \
                        target_cell.get_piece().get_piece_x() == enemy_border:
                    self.promote_message_box(target_cell, target)
                    print(target_cell.get_piece().get_piece_type())

                if self.game.is_stalemate():
                    self.stalemate_message_box()

                if self.game.is_king_targeted(self.game.get_current_player()):
                    for i in self.colored_cells:
                        i.setStyleSheet(i.styleSheet().replace("background-color: #3F704D", ""))
                    self.colored_cells = []

                    if len(self.game.steps_if_king_is_targeted()) == 0:
                        winner = self.player2Name.text() if self.game.get_current_player() == self.game.get_white_player() \
                            else self.player1Name.text()
                        self.checkmate_message_box(winner)

                    self.check_message_box()

            self.step_progress = 1

            for i in self.colored_cells:
                i.setStyleSheet(i.styleSheet().replace("background-color: #3F704D", ""))
            self.colored_cells = []

        print(self.step_progress)

    def capture(self, target_pixmap):
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

    def promote_message_box(self, cell, gui_cell):
        msgbox = QMessageBox()
        msgbox.setWindowTitle("Promotion")
        msgbox.setText('Choose the type of piece you would like to promote the pawn to')
        msgbox.setWindowModality(QtCore.Qt.ApplicationModal)

        queen_b = QPushButton("Queen")
        rook_b = QPushButton("Rook")
        bishop_b = QPushButton("Bishop")
        knight_b = QPushButton("Knight")

        msgbox.addButton(queen_b, QMessageBox.YesRole)
        msgbox.addButton(rook_b, QMessageBox.NoRole)
        msgbox.addButton(bishop_b, QMessageBox.RejectRole)
        msgbox.addButton(knight_b, QMessageBox.AcceptRole)

        msgbox.exec_()

        if msgbox.clickedButton() == queen_b:

            self.game.promote_pawn(cell, PieceType.QUEEN)
            if cell.get_piece().get_direction() == 1:
                pixmap = QPixmap("./resource_images/pieces/w_queen.png")
            else:
                pixmap = QPixmap("./resource_images/pieces/b_queen.png")
            gui_cell.setPixmap(pixmap)

        elif msgbox.clickedButton() == rook_b:

            self.game.promote_pawn(cell, PieceType.ROOK)
            if cell.get_piece().get_direction() == 1:
                pixmap = QPixmap("./resource_images/pieces/w_rook.png")
            else:
                pixmap = QPixmap("./resource_images/pieces/b_rook.png")
            gui_cell.setPixmap(pixmap)

        elif msgbox.clickedButton() == bishop_b:

            self.game.promote_pawn(cell, PieceType.BISHOP)
            if cell.get_piece().get_direction() == 1:
                pixmap = QPixmap("./resource_images/pieces/w_bishop.png")
            else:
                pixmap = QPixmap("./resource_images/pieces/b_bishop.png")
            gui_cell.setPixmap(pixmap)

        elif msgbox.clickedButton() == knight_b:

            self.game.promote_pawn(cell, PieceType.KNIGHT)
            if cell.get_piece().get_direction() == 1:
                pixmap = QPixmap("./resource_images/pieces/w_knight.png")
            else:
                pixmap = QPixmap("./resource_images/pieces/b_knight.png")
            gui_cell.setPixmap(pixmap)

    def surrender_message_box(self, enemy_player_name):
        msgbox = QMessageBox()
        msgbox.setWindowTitle("Surrender?")
        msgbox.setText('Do you really want to surrender?')
        msgbox.setWindowModality(QtCore.Qt.ApplicationModal)

        yes_button = QPushButton("Yes")
        no_button = QPushButton("No")

        msgbox.addButton(yes_button, QMessageBox.YesRole)
        msgbox.addButton(no_button, QMessageBox.NoRole)

        msgbox.exec_()

        if msgbox.clickedButton() == yes_button:
            self.end_game_message_box(enemy_player_name)

    def check_message_box(self):

        name = self.player1Name.text() if self.game.get_current_player() == self.game.get_white_player() \
            else self.player2Name.text()

        msgbox = QMessageBox()
        msgbox.setWindowTitle("Warning ")
        msgbox.setText(name + "! Your king is in check.")
        msgbox.setWindowModality(QtCore.Qt.ApplicationModal)

        msgbox.addButton(QPushButton("OK"), QMessageBox.YesRole)

        msgbox.exec_()

    def still_check_message_box(self):
        msgbox = QMessageBox()
        msgbox.setWindowTitle("Warning")
        msgbox.setText("Your king is in check. You can't step with this piece.")
        msgbox.setWindowModality(QtCore.Qt.ApplicationModal)

        msgbox.addButton(QPushButton("OK"), QMessageBox.YesRole)

        msgbox.exec_()


    def make_enemy_surrender_message_box(self, player_name):
        msgbox = QMessageBox()
        msgbox.setWindowTitle("Agree to surrender?")
        msgbox.setText('Do you agree to surrender?')
        msgbox.setWindowModality(QtCore.Qt.ApplicationModal)

        yes_button = QPushButton("Yes")
        no_button = QPushButton("No")

        msgbox.addButton(yes_button, QMessageBox.YesRole)
        msgbox.addButton(no_button, QMessageBox.NoRole)

        msgbox.exec_()

        if msgbox.clickedButton() == yes_button:
            self.end_game_message_box(player_name)


    def draw_request_message_box(self, enemy_player_name):
        msgbox = QMessageBox()
        msgbox.setWindowTitle("Draw?")
        msgbox.setText("Do " + enemy_player_name + " agree with a draw?")
        msgbox.setWindowModality(QtCore.Qt.ApplicationModal)

        yes_button = QPushButton("Yes")
        no_button = QPushButton("No")

        msgbox.addButton(yes_button, QMessageBox.YesRole)
        msgbox.addButton(no_button, QMessageBox.NoRole)

        msgbox.exec_()

        if msgbox.clickedButton() == yes_button:
            self.end_game_message_box("Draw")

    def checkmate_message_box(self, game_result):
        if game_result != "Draw":
            game_result = game_result + "'s victory"
        msgbox = QMessageBox()
        msgbox.setWindowTitle("CheckMate!")
        msgbox.setText('The result of the game is: ' + game_result)
        msgbox.setWindowModality(QtCore.Qt.ApplicationModal)

        return_btn = QPushButton("Return to main page")

        msgbox.addButton(return_btn, QMessageBox.YesRole)

        msgbox.exec_()

        if msgbox.clickedButton() == return_btn:
            print("Game finished")

    def end_game_message_box(self, game_result):
        if game_result != "Draw":
            game_result = game_result + "'s victory"
        msgbox = QMessageBox()
        msgbox.setWindowTitle("Game Finished")
        msgbox.setText('The result of the game is: ' + game_result)
        msgbox.setWindowModality(QtCore.Qt.ApplicationModal)

        return_btn = QPushButton("Return to main page")

        msgbox.addButton(return_btn, QMessageBox.YesRole)

        msgbox.exec_()

        if msgbox.clickedButton() == return_btn:
            print("Game finished")


    def stalemate_message_box(self):
        msgbox = QMessageBox()
        msgbox.setWindowTitle("Stalemate")
        msgbox.setText('The result of the game is stalemate')
        msgbox.setWindowModality(QtCore.Qt.ApplicationModal)

        return_btn = QPushButton("Return to main page")

        msgbox.addButton(return_btn, QMessageBox.YesRole)

        msgbox.exec_()

        if msgbox.clickedButton() == return_btn:
            print("Game finished")

    def mark_possible_steps(self, cells):

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
