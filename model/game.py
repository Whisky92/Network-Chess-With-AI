from player import Player
from colors import Color
from board import Board
from cell import Cell
from piece_type import PieceType
from piece import Piece

class Game:

    def __init__(self):
        self._white_player = Player(Color.WHITE)
        self._black_player = Player(Color.BLACK)
        self._current_player = self._white_player
        self._board = Board()
        self._last_step = None

    def set_white_player_direction(self, direction):
        self._white_player.set_direction(direction)

    def set_black_player_direction(self, direction):
        self._black_player.set_direction(direction)

    def get_current_player(self):
        return self._current_player

    def get_board(self):
        return self._board

    def get_board_table(self):
        return self._board.get_board()

    def get_last_step(self):
        return self._last_step

    def move_piece(self, cell_to_move_from: Cell, target_cell: Cell):
        piece_to_move = cell_to_move_from.get_piece()
        x_target_coord = target_cell.get_piece().get_piece_x()
        y_target_coord = target_cell.get_piece().get_piece_y()
        if target_cell in piece_to_move.get_possible_steps(self._board.get_board(), self._last_step):
            if target_cell.get_piece().get_direction() != 0:
                target_cell.get_piece().set_piece_x(-1)
                target_cell.get_piece().set_piece_y(-1)
                self.__get_player_by_direction(target_cell.get_piece()).add_to_captured_pieces(target_cell.get_piece())
            elif piece_to_move.get_en_passant_step() is not None \
                    and target_cell == piece_to_move.get_en_passant_step():
                piece_to_move.delete_last_en_passant_step()
                target_y = target_cell.get_piece().get_piece_y()
                target_x = target_cell.get_piece().get_piece_x() + 1 * piece_to_move.get_direction()
                piece_to_capture = self._board.get_board()[target_x][target_y].get_piece()
                piece_to_capture.set_piece_x(-1)
                piece_to_capture.set_piece_y(-1)
                self.__get_player_by_direction(target_cell).\
                    add_to_captured_pieces(piece_to_capture)
            if (piece_to_move.get_piece_x() == target_cell.get_piece().get_piece_x() - 2
                or piece_to_move.get_piece_x() == target_cell.get_piece().get_piece_x() + 2) \
                    and piece_to_move.get_piece_type() == PieceType.PAWN:
                self._last_step = target_cell
            elif self._last_step is not None:
                self._last_step = None
            cell_to_move_from.set_piece(Piece(piece_to_move.get_piece_x(), piece_to_move.get_piece_y(), PieceType.NO_TYPE, 0))
            piece_to_move.set_piece_x(x_target_coord)
            piece_to_move.set_piece_y(y_target_coord)
            piece_to_move.change_to_not_first_step()
            target_cell.set_piece(piece_to_move)


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

