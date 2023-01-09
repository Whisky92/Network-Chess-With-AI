from player import Player
from colors import Color
from piece import Piece
from piece_type import PieceType


class Game:

    def __init__(self):
        self._white_player = Player(Color.WHITE)
        self._black_player = Player(Color.BLACK)
        self._current_player = self._white_player
        self._board = None
        self.fill_board()

    def set_white_player_direction(self, direction):
        self._white_player.set_direction(direction)

    def set_black_player_direction(self, direction):
        self._black_player.set_direction(direction)

    def get_current_player(self):
        return self._current_player

    def fill_board(self):
        self._board = [[Piece(PieceType.ROOK, -1), Piece(PieceType.KNIGHT, -1),
                        Piece(PieceType.BISHOP, -1), Piece(PieceType.QUEEN, -1),
                        Piece(PieceType.KING, -1), Piece(PieceType.BISHOP, -1),
                        Piece(PieceType.KNIGHT, -1), Piece(PieceType.ROOK, -1)],
                       [Piece(PieceType.ROOK, 1), Piece(PieceType.KNIGHT, 1),
                        Piece(PieceType.BISHOP, 1), Piece(PieceType.QUEEN, 1),
                        Piece(PieceType.KING, 1), Piece(PieceType.BISHOP, 1),
                        Piece(PieceType.KNIGHT, 1), Piece(PieceType.ROOK, 1)]]

        self._board.insert(1, [Piece(PieceType.PAWN, -1), Piece(PieceType.PAWN, -1),
                               Piece(PieceType.PAWN, -1), Piece(PieceType.PAWN, -1),
                               Piece(PieceType.PAWN, -1), Piece(PieceType.PAWN, -1),
                               Piece(PieceType.PAWN, -1), Piece(PieceType.PAWN, -1)])

        for i in range(2, 6):
            self._board.insert(i, [Piece(PieceType.NO_TYPE, 1), Piece(PieceType.NO_TYPE, 1),
                                   Piece(PieceType.NO_TYPE, 1), Piece(PieceType.NO_TYPE, 1),
                                   Piece(PieceType.NO_TYPE, 1), Piece(PieceType.NO_TYPE, 1),
                                   Piece(PieceType.NO_TYPE, 1), Piece(PieceType.NO_TYPE, 1)])

        self._board.insert(6, [Piece(PieceType.PAWN, 1), Piece(PieceType.PAWN, 1),
                               Piece(PieceType.PAWN, 1), Piece(PieceType.PAWN, 1),
                               Piece(PieceType.PAWN, 1), Piece(PieceType.PAWN, 1),
                               Piece(PieceType.PAWN, 1), Piece(PieceType.PAWN, 1)])

    def print_table(self):
        for i in range(0, len(self._board)):
            for j in range(0, 8):
                print(self._board[i][j]._p_type, self._board[i][j].direction, end=" ")
            print()

    def __check_steps(self, ):
        pass
