from piece import Piece
from piece_type import PieceType


class Board:

    def __init__(self):
        self._board: list[list[int]] = list()
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
            self._board.insert(i, [Piece(i, 0, PieceType.NO_TYPE, 0), Piece(i, 1, PieceType.NO_TYPE, 0),
                                   Piece(i, 2, PieceType.NO_TYPE, 0), Piece(i, 3, PieceType.NO_TYPE, 0),
                                   Piece(i, 4, PieceType.NO_TYPE, 0), Piece(i, 5, PieceType.NO_TYPE, 0),
                                   Piece(i, 5, PieceType.NO_TYPE, 0), Piece(i, 6, PieceType.NO_TYPE, 0)])

        self._board.insert(6, [Piece(6, 0, PieceType.PAWN, 1), Piece(6, 1, PieceType.PAWN, 1),
                               Piece(6, 2, PieceType.PAWN, 1), Piece(6, 3, PieceType.PAWN, 1),
                               Piece(6, 4, PieceType.PAWN, 1), Piece(6, 5, PieceType.PAWN, 1),
                               Piece(6, 6, PieceType.PAWN, 1), Piece(6, 7, PieceType.PAWN, 1)])
        self._board[2][1] = Piece(2, 1, PieceType.PAWN, 1)



    def get_cell_of_board(self, x, y):
        return self._board[x][y]


    def get_possible_steps(self, x, y):
        return self._board[x][y].get_possible_steps(self._board, self._last_step)


    def print_possible_steps(self, x, y):
        for i in self._board[x][y].get_possible_steps(self._board, self._last_step):
            print(i)


    def print_board(self):
        for i in range(0,8):
            for j in range(0,8):
                self.print_coords(self._board[i][j])
            print()


    def print_piece_data(self, piece):
        print(piece.get_piece_x(), piece.get_piece_y(), piece.get_piece_type(), piece.get_direction())



    def print_coords(self, piece):
            print(piece.get_piece_type(), piece.get_direction(), end=" ")
