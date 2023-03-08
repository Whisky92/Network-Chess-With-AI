from model.piece import Piece
from model.piece_type import PieceType
from model.cell import Cell


class Board:

    def __init__(self):
        self._board = list()
        self.fill_board()

    def get_board(self):
        return self._board

    def fill_board(self):
        self._board = [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
                        Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.QUEEN, -1)),
                        Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.NO_TYPE, 0)),
                        Cell(Piece(0, 6, PieceType.NO_TYPE, 0)), Cell(Piece(0, 7, PieceType.NO_TYPE, 0))],

                       [Cell(Piece(1, 0, PieceType.NO_TYPE, 0)), Cell(Piece(1, 1, PieceType.NO_TYPE, 0)),
                        Cell(Piece(1, 2, PieceType.NO_TYPE, 0)), Cell(Piece(1, 3, PieceType.NO_TYPE, 0)),
                        Cell(Piece(1, 4, PieceType.NO_TYPE, 0)), Cell(Piece(1, 5, PieceType.NO_TYPE, 0)),
                        Cell(Piece(1, 6, PieceType.NO_TYPE, 0)), Cell(Piece(1, 7, PieceType.NO_TYPE, 0))],

                       [Cell(Piece(2, 0, PieceType.NO_TYPE, 0)), Cell(Piece(2, 1, PieceType.NO_TYPE, 0)),
                        Cell(Piece(2, 2, PieceType.NO_TYPE, 0)), Cell(Piece(2, 3, PieceType.NO_TYPE, 0)),
                        Cell(Piece(2, 4, PieceType.NO_TYPE, 0)), Cell(Piece(2, 5, PieceType.NO_TYPE, 0)),
                        Cell(Piece(2, 6, PieceType.NO_TYPE, 0)), Cell(Piece(2, 7, PieceType.NO_TYPE, 0))],

                       [Cell(Piece(3, 0, PieceType.NO_TYPE, 0)), Cell(Piece(3, 1, PieceType.NO_TYPE, 0)),
                        Cell(Piece(3, 2, PieceType.NO_TYPE, 0)), Cell(Piece(3, 3, PieceType.NO_TYPE, 0)),
                        Cell(Piece(3, 4, PieceType.NO_TYPE, 0)), Cell(Piece(3, 5, PieceType.NO_TYPE, 0)),
                        Cell(Piece(3, 6, PieceType.NO_TYPE, 0)), Cell(Piece(3, 7, PieceType.NO_TYPE, 0))],

                       [Cell(Piece(4, 0, PieceType.NO_TYPE, 0)), Cell(Piece(4, 1, PieceType.NO_TYPE, 0)),
                        Cell(Piece(4, 2, PieceType.NO_TYPE, 0)), Cell(Piece(4, 3, PieceType.NO_TYPE, 0)),
                        Cell(Piece(4, 4, PieceType.NO_TYPE, 0)), Cell(Piece(4, 5, PieceType.NO_TYPE, 0)),
                        Cell(Piece(4, 6, PieceType.NO_TYPE, 0)), Cell(Piece(4, 7, PieceType.NO_TYPE, 0))],

                       [Cell(Piece(5, 0, PieceType.NO_TYPE, 0)), Cell(Piece(5, 1, PieceType.NO_TYPE, 0)),
                        Cell(Piece(5, 2, PieceType.NO_TYPE, 0)), Cell(Piece(5, 3, PieceType.NO_TYPE, 0)),
                        Cell(Piece(5, 4, PieceType.NO_TYPE, 0)), Cell(Piece(5, 5, PieceType.NO_TYPE, 0)),
                        Cell(Piece(5, 6, PieceType.NO_TYPE, 0)), Cell(Piece(5, 7, PieceType.NO_TYPE, 0))],

                       [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.NO_TYPE, 0)),
                        Cell(Piece(6, 2, PieceType.NO_TYPE, 0)), Cell(Piece(6, 3, PieceType.NO_TYPE, 0)),
                        Cell(Piece(6, 4, PieceType.NO_TYPE, 0)), Cell(Piece(6, 5, PieceType.NO_TYPE, 0)),
                        Cell(Piece(6, 6, PieceType.NO_TYPE, 0)), Cell(Piece(6, 7, PieceType.NO_TYPE, 0))],

                       [Cell(Piece(7, 0, PieceType.NO_TYPE, 0)), Cell(Piece(7, 1, PieceType.KNIGHT, 1)),
                        Cell(Piece(7, 2, PieceType.BISHOP, 1)), Cell(Piece(7, 3, PieceType.QUEEN, 1)),
                        Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.NO_TYPE, 0)),
                        Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.NO_TYPE, 0))]]



    def get_cell_of_board(self, x, y):
        return self._board[x][y]



    def print_board(self):
        for i in range(0,8):
            for j in range(0,8):
                self.print_coords(self._board[i][j].get_piece())
            print()


    def print_piece_data(self, cell):
        piece = cell.get_piece()
        print(piece.get_piece_x(), piece.get_piece_y(), piece.get_piece_type(), piece.get_direction())



    def print_coords(self, piece):
            print(piece.get_piece_type(), piece.get_direction(), end=" ")
