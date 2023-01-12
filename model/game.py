from player import Player
from colors import Color
from board import Board
from piece import Piece
from piece_type import PieceType


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

    def move_piece(self, piece_to_move: Piece, target_piece: Piece):
        if target_piece in piece_to_move.get_possible_steps(self._board.get_board(), self._last_step):
            if target_piece.get_direction() != 0:
                self.__get_player_by_direction(target_piece).add_to_captured_pieces(target_piece.get_piece_type())
                target_piece = piece_to_move
                print(target_piece)
            elif piece_to_move.get_en_passant_step() is not None \
                    and target_piece == piece_to_move.get_en_passant_step():
                piece_to_move.delete_last_en_passant_step()
                target_y = target_piece.get_piece_y()
                target_x = target_piece.get_piece_x() + 1 * piece_to_move.get_direction()
                self.__get_player_by_direction(target_piece).\
                    add_to_captured_pieces(self._board.get_board()[target_x][target_y].get_piece_type())

            if (piece_to_move.get_piece_x() == target_piece.get_piece_x() - 2
                or piece_to_move.get_piece_x() == target_piece.get_piece_x() + 2)\
                    and piece_to_move.get_piece_type() == PieceType.PAWN:
                self._last_step = target_piece
            elif self._last_step is not None:
                self._last_step = None
            target_piece.set_piece_type(piece_to_move.get_piece_type())
            target_piece.set_direction(piece_to_move.get_direction())
            piece_to_move.set_direction(0)
            piece_to_move.set_piece_type(PieceType.NO_TYPE)

    def get_possible_steps(self, piece):
        return piece.get_possible_steps(self._board.get_board(), self._last_step)

    def __get_player_by_direction(self, direction):
        if self._white_player.get_direction() == direction:
            return self._white_player
        return self._black_player

    def print_possible_steps(self, piece):
        for i in piece.get_possible_steps(self._board.get_board(), self._last_step):
            print(i.get_piece_x(), i.get_piece_y(), "type:", i.get_piece_type(), end=" | ")

