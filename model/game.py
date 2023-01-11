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
        self._board = Board.get_instance()
        self._last_step = None

    def set_white_player_direction(self, direction):
        self._white_player.set_direction(direction)

    def set_black_player_direction(self, direction):
        self._black_player.set_direction(direction)

    def get_current_player(self):
        return self._current_player

    def move_piece(self, piece_to_move: Piece, target_piece: Piece):
        if target_piece in piece_to_move.get_possible_steps(self._last_step):
            if target_piece is not None:
                self.__get_player_by_direction(target_piece).add_to_captured_pieces(target_piece)
            target_piece = piece_to_move
            piece_to_move = None

    def __get_player_by_direction(self, direction):
        if self._white_player.get_direction() == direction:
            return self._white_player
        return self._black_player


