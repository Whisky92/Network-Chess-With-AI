from model.piece import Piece
from model.piece_type import PieceType
from model.cell import Cell


class Board:
    """
    A class for representing the game board
    """

    def __init__(self, *args):

        if len(args) == 0:
            self._board = list()
            self.__fill_board()

        elif type(args[0]) == list:
            self._board = args[0]

    def get_board(self):
        return self._board

    def __fill_board(self):
        """
        Fills the board with piece cells
        """
        self._board = [[Cell(Piece(0, 0, PieceType.ROOK, -1)), Cell(Piece(0, 1, PieceType.KNIGHT, -1)),
                        Cell(Piece(0, 2, PieceType.BISHOP, -1)), Cell(Piece(0, 3, PieceType.QUEEN, -1)),
                        Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.BISHOP, -1)),
                        Cell(Piece(0, 6, PieceType.KNIGHT, -1)), Cell(Piece(0, 7, PieceType.ROOK, -1))],
                       [Cell(Piece(7, 0, PieceType.ROOK, 1)), Cell(Piece(7, 1, PieceType.KNIGHT, 1)),
                        Cell(Piece(7, 2, PieceType.BISHOP, 1)), Cell(Piece(7, 3, PieceType.QUEEN, 1)),
                        Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.BISHOP, 1)),
                        Cell(Piece(7, 6, PieceType.KNIGHT, 1)), Cell(Piece(7, 7, PieceType.ROOK, 1))]]

        self._board.insert(1, [Cell(Piece(1, 0, PieceType.PAWN, -1)), Cell(Piece(1, 1, PieceType.PAWN, -1)),
                               Cell(Piece(1, 2, PieceType.PAWN, -1)), Cell(Piece(1, 3, PieceType.PAWN, -1)),
                               Cell(Piece(1, 4, PieceType.PAWN, -1)), Cell(Piece(1, 5, PieceType.PAWN, -1)),
                               Cell(Piece(1, 6, PieceType.PAWN, -1)), Cell(Piece(1, 7, PieceType.PAWN, -1))])

        for i in range(2, 6):
            self._board.insert(i, [Cell(Piece(i, 0, PieceType.NO_TYPE, 0)), Cell(Piece(i, 1, PieceType.NO_TYPE, 0)),
                                   Cell(Piece(i, 2, PieceType.NO_TYPE, 0)), Cell(Piece(i, 3, PieceType.NO_TYPE, 0)),
                                   Cell(Piece(i, 4, PieceType.NO_TYPE, 0)), Cell(Piece(i, 5, PieceType.NO_TYPE, 0)),
                                   Cell(Piece(i, 6, PieceType.NO_TYPE, 0)),
                                   Cell(Piece(i, 7, PieceType.NO_TYPE, 0))])

        self._board.insert(6, [Cell(Piece(6, 0, PieceType.PAWN, 1)), Cell(Piece(6, 1, PieceType.PAWN, 1)),
                               Cell(Piece(6, 2, PieceType.PAWN, 1)), Cell(Piece(6, 3, PieceType.PAWN, 1)),
                               Cell(Piece(6, 4, PieceType.PAWN, 1)), Cell(Piece(6, 5, PieceType.PAWN, 1)),
                               Cell(Piece(6, 6, PieceType.PAWN, 1)), Cell(Piece(6, 7, PieceType.PAWN, 1))])

    def set_board(self, board):
        self._board = board
    def __eq__(self, other):
        for i in range(0, 8):
            for j in range(0, 8):

                if self._board[i][j].get_piece().get_piece_x() \
                        != other[i][j].get_piece().get_piece_x() or \
                        self._board[i][j].get_piece().get_piece_y() \
                        != other[i][j].get_piece().get_piece_y() or \
                        self._board[i][j].get_piece().get_piece_type() != \
                        other[i][j].get_piece().get_piece_type() or \
                        self._board[i][j].get_piece().get_direction() != \
                        other[i][j].get_piece().get_direction():

                    return False

        return True
