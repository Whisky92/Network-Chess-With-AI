from player import Player
from colors import Color
from board import Board
from cell import Cell
from piece_type import PieceType
from piece import Piece

class Game:

    def __init__(self, white_direction, black_direction):
        self._white_player = Player(Color.WHITE, white_direction)
        self._black_player = Player(Color.BLACK, black_direction)
        self._current_player = self._white_player
        self._board = Board()
        self._last_step = None
        self.__add_to_player_pieces()

    def change_current_player(self):
        if self._current_player == self._white_player:
            self._current_player = self._black_player
        else:
            self._current_player = self._white_player

    def get_white_player(self):
        return self._white_player

    def get_black_player(self):
        return self._black_player

    def get_current_player(self):
        return self._current_player

    def get_board(self):
        return self._board

    def get_board_table(self):
        return self._board.get_board()

    def get_last_step(self):
        return self._last_step


    def __add_to_player_pieces(self):
        for i in range(0, 8):
            for j in range(0, 8):
                this_piece = self._board.get_board()[i][j].get_piece()
                if this_piece.get_direction() == self._white_player.get_direction():
                    self._white_player.add_to_pieces_on_board(this_piece)
                elif this_piece.get_direction() == self._black_player.get_direction():
                    self._black_player.add_to_pieces_on_board(this_piece)

    def move_piece(self, cell_to_move_from: Cell, target_cell: Cell):
        piece_to_move = cell_to_move_from.get_piece()
        x_target_coord = target_cell.get_piece().get_piece_x()
        y_target_coord = target_cell.get_piece().get_piece_y()
        if target_cell in piece_to_move.get_possible_steps(self._board.get_board(), self._last_step):
            if target_cell.get_piece().get_direction() != 0:
                target_cell.get_piece().set_piece_x(-1)
                target_cell.get_piece().set_piece_y(-1)
                current_player = self.__get_player_by_direction(target_cell.get_piece().get_direction())
                current_player.add_to_captured_pieces(target_cell.get_piece())
                current_player.remove_from_pieces_on_board(target_cell.get_piece())
            elif piece_to_move.get_en_passant_step() is not None \
                    and target_cell == piece_to_move.get_en_passant_step():
                piece_to_move.delete_last_en_passant_step()
                target_y = target_cell.get_piece().get_piece_y()
                target_x = target_cell.get_piece().get_piece_x() + 1 * piece_to_move.get_direction()
                cell_to_capture_from = self._board.get_board()[target_x][target_y]
                target_direction = cell_to_capture_from.get_piece().get_direction()
                cell_to_capture_from.get_piece().set_piece_x(-1)
                cell_to_capture_from.get_piece().set_piece_y(-1)
                current_player = self.__get_player_by_direction(target_direction)
                current_player.add_to_captured_pieces(cell_to_capture_from.get_piece())
                current_player.remove_from_pieces_on_board(cell_to_capture_from.get_piece())
                cell_to_capture_from.set_piece(Piece(target_x, target_y, PieceType.NO_TYPE, 0))
            if (piece_to_move.get_piece_x() == target_cell.get_piece().get_piece_x() - 2
                or piece_to_move.get_piece_x() == target_cell.get_piece().get_piece_x() + 2) \
                    and piece_to_move.get_piece_type() == PieceType.PAWN:
                self._last_step = target_cell
            elif self._last_step is not None:
                self._last_step = None
            cell_to_move_from.set_piece(Piece(piece_to_move.get_piece_x(), piece_to_move.get_piece_y(),
                                              PieceType.NO_TYPE, 0))
            piece_to_move.set_piece_x(x_target_coord)
            piece_to_move.set_piece_y(y_target_coord)
            piece_to_move.change_to_not_first_step()
            target_cell.set_piece(piece_to_move)

    def evolve_pawn(self, cell, p_type):
        piece = cell.get_piece()
        if piece.get_is_able_to_evolve():
            piece.set_to_not_able_to_evolve()
            piece.set_piece_type(p_type)
    def is_king_targeted(self, player):
        king_cell = self.__get_king_cell(player)
        return self.__is_cell_targeted(king_cell)
    def is_king_cells_targeted(self, player):
        king_cell = self.__get_king_cell(player)
        non_targeted_cells = []
        for i in king_cell.get_piece().get_possible_steps(self._board.get_board(), self._last_step):
            if not self.__is_cell_targeted(i):
                non_targeted_cells.append(i)
        return non_targeted_cells
    def __is_cell_targeted(self, cell):
        enemy_player = None
        if cell.get_piece().get_direction() == self._white_player.get_direction():
            enemy_player = self._black_player
        else:
            enemy_player = self._white_player
        for i in enemy_player.get_pieces_on_board():
            if cell in i.get_possible_steps():
                return True
        return False

    def __get_king_cell(self, player):
        for i in player.get_pieces_on_board():
            if i.get_piece_type() == PieceType.KING:
                return self._board.get_board()[i.get_piece_x()][i.get_piece_y()]

    def print_pieces(self):
        for i in self._black_player.get_pieces_on_board():
            print(i)

    def get_possible_steps(self, x, y):
        piece = self.get_board_table()[x][y].get_piece()
        return piece.get_possible_steps(self._board.get_board(), self._last_step)

    def get_player_by_direction(self, direction):
        if self._white_player.get_direction() == direction:
            return self._white_player
        return self._black_player
    def __get_player_by_direction(self, direction):
        if self._white_player.get_direction() == direction:
            return self._white_player
        return self._black_player

    def print_possible_steps(self, x, y):
        piece = self.get_board_table()[x][y].get_piece()
        for i in piece.get_possible_steps(self._board.get_board(), self._last_step):
            print(i.get_piece().get_piece_x(), i.get_piece().get_piece_y(),
                  "type:", i.get_piece().get_piece_type(), i.get_piece().get_direction())

