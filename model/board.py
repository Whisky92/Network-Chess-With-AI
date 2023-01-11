from piece import Piece
from piece_type import PieceType


class Board:
    __board_instance = None

    @classmethod
    def get_instance(cls):
        if Board.__board_instance is None:
            Board.__board_instance = Board()
        return Board.__board_instance

    def __init__(self):
        self._board = None
        self.fill_board()
        self._last_step = None

    def get_board(self):
        return self._board

    def get_last_step(self):
        return self._last_step

    def fill_board(self):
        self._board = [[Piece(0, 0, PieceType.ROOK, -1), Piece(0, 1, PieceType.KNIGHT, -1),
                        Piece(0, 2, PieceType.BISHOP, -1), Piece(0, 3, PieceType.QUEEN, -1),
                        Piece(0, 4, PieceType.KING, -1), Piece(0, 5, PieceType.BISHOP, -1),
                        Piece(0, 6, PieceType.KNIGHT, -1), Piece(0, 7, PieceType.ROOK, -1)],
                       [Piece(7, 0, PieceType.ROOK, 1), Piece(7, 1, PieceType.KNIGHT, 1),
                        Piece(7, 2, PieceType.BISHOP, 1), Piece(7, 3, PieceType.QUEEN, 1),
                        Piece(7, 4, PieceType.KING, 1), Piece(7, 5, PieceType.BISHOP, 1),
                        Piece(7, 6, PieceType.KNIGHT, 1), Piece(7, 7, PieceType.ROOK, 1)]]

        self._board.insert(1, [Piece(1, 0, PieceType.PAWN, -1), Piece(1, 1, PieceType.PAWN, -1),
                               Piece(1, 2, PieceType.PAWN, -1), Piece(1, 3, PieceType.PAWN, -1),
                               Piece(1, 4, PieceType.PAWN, -1), Piece(1, 5, PieceType.PAWN, -1),
                               Piece(1, 6, PieceType.PAWN, -1), Piece(1, 7, PieceType.PAWN, -1)])

        for i in range(2, 6):
            self._board.insert(i, [None, None,
                                   None, None,
                                   None, None,
                                   None, None])

        self._board.insert(6, [Piece(6, 0, PieceType.PAWN, 1), Piece(6, 1, PieceType.PAWN, 1),
                               Piece(6, 2, PieceType.PAWN, 1), Piece(6, 3, PieceType.PAWN, 1),
                               Piece(6, 4, PieceType.PAWN, 1), Piece(6, 5, PieceType.PAWN, 1),
                               Piece(6, 6, PieceType.PAWN, 1), Piece(6, 7, PieceType.PAWN, 1)])














    def print_coords(self, piece):
        print(piece.get_piece_x(), piece.get_piece_y())