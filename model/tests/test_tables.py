from model.cell import Cell
from model.piece import Piece
from model.piece_type import PieceType


class TestTables:

    table_for_game_test_one = \
                        [[Cell(Piece(0, 0, PieceType.ROOK, -1)), Cell(Piece(0, 1, PieceType.KNIGHT, -1)),
                         Cell(Piece(0, 2, PieceType.BISHOP, -1)), Cell(Piece(0, 3, PieceType.QUEEN, -1)),
                         Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.BISHOP, -1)),
                         Cell(Piece(0, 6, PieceType.KNIGHT, -1)), Cell(Piece(0, 7, PieceType.ROOK, -1))],

                        [Cell(Piece(1, 0, PieceType.PAWN, -1)), Cell(Piece(1, 1, PieceType.PAWN, -1)),
                         Cell(Piece(1, 2, PieceType.PAWN, -1)), Cell(Piece(1, 3, PieceType.PAWN, -1)),
                         Cell(Piece(1, 4, PieceType.PAWN, -1)), Cell(Piece(1, 5, PieceType.PAWN, -1)),
                         Cell(Piece(1, 6, PieceType.PAWN, -1)), Cell(Piece(1, 7, PieceType.PAWN, -1))],

                        [Cell(Piece(2, 0, PieceType.NO_TYPE, 0)), Cell(Piece(2, 1, PieceType.NO_TYPE, 0)),
                         Cell(Piece(2, 2, PieceType.NO_TYPE, 0)), Cell(Piece(2, 3, PieceType.NO_TYPE, 0)),
                         Cell(Piece(2, 4, PieceType.NO_TYPE, 0)), Cell(Piece(2, 5, PieceType.NO_TYPE, 0)),
                         Cell(Piece(2, 6, PieceType.NO_TYPE, 0)), Cell(Piece(2, 7, PieceType.NO_TYPE, 0))],

                        [Cell(Piece(3, 0, PieceType.NO_TYPE, 0)), Cell(Piece(3, 1, PieceType.NO_TYPE, 0)),
                         Cell(Piece(3, 2, PieceType.NO_TYPE, 0)), Cell(Piece(3, 3, PieceType.NO_TYPE, 0)),
                         Cell(Piece(3, 4, PieceType.NO_TYPE, 0)), Cell(Piece(3, 5, PieceType.NO_TYPE, 0)),
                         Cell(Piece(3, 6, PieceType.NO_TYPE, 0)), Cell(Piece(3, 7, PieceType.NO_TYPE, 0))],

                        [Cell(Piece(4, 0, PieceType.PAWN, 1)), Cell(Piece(4, 1, PieceType.NO_TYPE, 0)),
                         Cell(Piece(4, 2, PieceType.NO_TYPE, 0)), Cell(Piece(4, 3, PieceType.NO_TYPE, 0)),
                         Cell(Piece(4, 4, PieceType.NO_TYPE, 0)), Cell(Piece(4, 5, PieceType.NO_TYPE, 0)),
                         Cell(Piece(4, 6, PieceType.NO_TYPE, 0)), Cell(Piece(4, 7, PieceType.NO_TYPE, 0))],

                        [Cell(Piece(5, 0, PieceType.NO_TYPE, 0)), Cell(Piece(5, 1, PieceType.NO_TYPE, 0)),
                         Cell(Piece(5, 2, PieceType.NO_TYPE, 0)), Cell(Piece(5, 3, PieceType.NO_TYPE, 0)),
                         Cell(Piece(5, 4, PieceType.NO_TYPE, 0)), Cell(Piece(5, 5, PieceType.NO_TYPE, 0)),
                         Cell(Piece(5, 6, PieceType.NO_TYPE, 0)), Cell(Piece(5, 7, PieceType.NO_TYPE, 0))],

                        [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.PAWN, 1)),
                         Cell(Piece(6, 2, PieceType.PAWN, 1)), Cell(Piece(6, 3, PieceType.PAWN, 1)),
                         Cell(Piece(6, 4, PieceType.PAWN, 1)), Cell(Piece(6, 5, PieceType.PAWN, 1)),
                         Cell(Piece(6, 6, PieceType.PAWN, 1)), Cell(Piece(6, 7, PieceType.PAWN, 1))],

                        [Cell(Piece(7, 0, PieceType.ROOK, 1)), Cell(Piece(7, 1, PieceType.KNIGHT, 1)),
                         Cell(Piece(7, 2, PieceType.BISHOP, 1)), Cell(Piece(7, 3, PieceType.QUEEN, 1)),
                         Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.BISHOP, 1)),
                         Cell(Piece(7, 6, PieceType.KNIGHT, 1)), Cell(Piece(7, 7, PieceType.ROOK, 1))]]

    table_for_game_test_castling = \
                        [[Cell(Piece(0, 0, PieceType.ROOK, -1)), Cell(Piece(0, 1, PieceType.KNIGHT, -1)),
                         Cell(Piece(0, 2, PieceType.BISHOP, -1)), Cell(Piece(0, 3, PieceType.QUEEN, -1)),
                         Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.BISHOP, -1)),
                         Cell(Piece(0, 6, PieceType.KNIGHT, -1)), Cell(Piece(0, 7, PieceType.ROOK, -1))],

                        [Cell(Piece(1, 0, PieceType.PAWN, -1)), Cell(Piece(1, 1, PieceType.PAWN, -1)),
                         Cell(Piece(1, 2, PieceType.PAWN, -1)), Cell(Piece(1, 3, PieceType.PAWN, -1)),
                         Cell(Piece(1, 4, PieceType.PAWN, -1)), Cell(Piece(1, 5, PieceType.PAWN, -1)),
                         Cell(Piece(1, 6, PieceType.PAWN, -1)), Cell(Piece(1, 7, PieceType.PAWN, -1))],

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

                        [Cell(Piece(6, 0, PieceType.PAWN, 1)), Cell(Piece(6, 1, PieceType.PAWN, 1)),
                         Cell(Piece(6, 2, PieceType.PAWN, 1)), Cell(Piece(6, 3, PieceType.PAWN, 1)),
                         Cell(Piece(6, 4, PieceType.PAWN, 1)), Cell(Piece(6, 5, PieceType.PAWN, 1)),
                         Cell(Piece(6, 6, PieceType.PAWN, 1)), Cell(Piece(6, 7, PieceType.PAWN, 1))],

                        [Cell(Piece(7, 0, PieceType.ROOK, 1)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
                         Cell(Piece(7, 2, PieceType.NO_TYPE, 0)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
                         Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.BISHOP, 1)),
                         Cell(Piece(7, 6, PieceType.KNIGHT, 1)), Cell(Piece(7, 7, PieceType.ROOK, 1))]]

    table2_for_game_test_castling = \
        [[Cell(Piece(0, 0, PieceType.ROOK, -1)), Cell(Piece(0, 1, PieceType.KNIGHT, -1)),
          Cell(Piece(0, 2, PieceType.BISHOP, -1)), Cell(Piece(0, 3, PieceType.QUEEN, -1)),
          Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.BISHOP, -1)),
          Cell(Piece(0, 6, PieceType.KNIGHT, -1)), Cell(Piece(0, 7, PieceType.ROOK, -1))],

         [Cell(Piece(1, 0, PieceType.PAWN, -1)), Cell(Piece(1, 1, PieceType.PAWN, -1)),
          Cell(Piece(1, 2, PieceType.PAWN, -1)), Cell(Piece(1, 3, PieceType.PAWN, -1)),
          Cell(Piece(1, 4, PieceType.PAWN, -1)), Cell(Piece(1, 5, PieceType.PAWN, -1)),
          Cell(Piece(1, 6, PieceType.PAWN, -1)), Cell(Piece(1, 7, PieceType.PAWN, -1))],

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

         [Cell(Piece(6, 0, PieceType.PAWN, 1)), Cell(Piece(6, 1, PieceType.PAWN, 1)),
          Cell(Piece(6, 2, PieceType.PAWN, 1)), Cell(Piece(6, 3, PieceType.PAWN, 1)),
          Cell(Piece(6, 4, PieceType.PAWN, 1)), Cell(Piece(6, 5, PieceType.PAWN, 1)),
          Cell(Piece(6, 6, PieceType.PAWN, 1)), Cell(Piece(6, 7, PieceType.PAWN, 1))],

         [Cell(Piece(7, 0, PieceType.NO_TYPE, 0)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
          Cell(Piece(7, 2, PieceType.KING, 1)), Cell(Piece(7, 3, PieceType.ROOK, 1)),
          Cell(Piece(7, 4, PieceType.NO_TYPE, 0)), Cell(Piece(7, 5, PieceType.BISHOP, 1)),
          Cell(Piece(7, 6, PieceType.KNIGHT, 1)), Cell(Piece(7, 7, PieceType.ROOK, 1))]]

    table_for_game_test_when_target_cell_is_occupied = \
        [[Cell(Piece(0, 0, PieceType.ROOK, -1)), Cell(Piece(0, 1, PieceType.KNIGHT, -1)),
          Cell(Piece(0, 2, PieceType.BISHOP, -1)), Cell(Piece(0, 3, PieceType.QUEEN, -1)),
          Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.BISHOP, -1)),
          Cell(Piece(0, 6, PieceType.KNIGHT, -1)), Cell(Piece(0, 7, PieceType.ROOK, -1))],

         [Cell(Piece(1, 0, PieceType.PAWN, -1)), Cell(Piece(1, 1, PieceType.NO_TYPE, -1)),
          Cell(Piece(1, 2, PieceType.PAWN, -1)), Cell(Piece(1, 3, PieceType.PAWN, -1)),
          Cell(Piece(1, 4, PieceType.PAWN, -1)), Cell(Piece(1, 5, PieceType.PAWN, -1)),
          Cell(Piece(1, 6, PieceType.PAWN, -1)), Cell(Piece(1, 7, PieceType.PAWN, -1))],

         [Cell(Piece(2, 0, PieceType.NO_TYPE, 0)), Cell(Piece(2, 1, PieceType.NO_TYPE, 0)),
          Cell(Piece(2, 2, PieceType.NO_TYPE, 0)), Cell(Piece(2, 3, PieceType.NO_TYPE, 0)),
          Cell(Piece(2, 4, PieceType.NO_TYPE, 0)), Cell(Piece(2, 5, PieceType.NO_TYPE, 0)),
          Cell(Piece(2, 6, PieceType.NO_TYPE, 0)), Cell(Piece(2, 7, PieceType.NO_TYPE, 0))],

         [Cell(Piece(3, 0, PieceType.NO_TYPE, 0)), Cell(Piece(3, 1, PieceType.PAWN, -1)),
          Cell(Piece(3, 2, PieceType.NO_TYPE, 0)), Cell(Piece(3, 3, PieceType.NO_TYPE, 0)),
          Cell(Piece(3, 4, PieceType.NO_TYPE, 0)), Cell(Piece(3, 5, PieceType.NO_TYPE, 0)),
          Cell(Piece(3, 6, PieceType.NO_TYPE, 0)), Cell(Piece(3, 7, PieceType.NO_TYPE, 0))],

         [Cell(Piece(4, 0, PieceType.PAWN, 1)), Cell(Piece(4, 1, PieceType.NO_TYPE, 0)),
          Cell(Piece(4, 2, PieceType.NO_TYPE, 0)), Cell(Piece(4, 3, PieceType.NO_TYPE, 0)),
          Cell(Piece(4, 4, PieceType.NO_TYPE, 0)), Cell(Piece(4, 5, PieceType.NO_TYPE, 0)),
          Cell(Piece(4, 6, PieceType.NO_TYPE, 0)), Cell(Piece(4, 7, PieceType.NO_TYPE, 0))],

         [Cell(Piece(5, 0, PieceType.NO_TYPE, 0)), Cell(Piece(5, 1, PieceType.NO_TYPE, 0)),
          Cell(Piece(5, 2, PieceType.NO_TYPE, 0)), Cell(Piece(5, 3, PieceType.NO_TYPE, 0)),
          Cell(Piece(5, 4, PieceType.NO_TYPE, 0)), Cell(Piece(5, 5, PieceType.NO_TYPE, 0)),
          Cell(Piece(5, 6, PieceType.NO_TYPE, 0)), Cell(Piece(5, 7, PieceType.NO_TYPE, 0))],

         [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.PAWN, 1)),
          Cell(Piece(6, 2, PieceType.PAWN, 1)), Cell(Piece(6, 3, PieceType.PAWN, 1)),
          Cell(Piece(6, 4, PieceType.PAWN, 1)), Cell(Piece(6, 5, PieceType.PAWN, 1)),
          Cell(Piece(6, 6, PieceType.PAWN, 1)), Cell(Piece(6, 7, PieceType.PAWN, 1))],

         [Cell(Piece(7, 0, PieceType.NO_TYPE, 0)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
          Cell(Piece(7, 2, PieceType.KING, 1)), Cell(Piece(7, 3, PieceType.ROOK, 1)),
          Cell(Piece(7, 4, PieceType.NO_TYPE, 0)), Cell(Piece(7, 5, PieceType.BISHOP, 1)),
          Cell(Piece(7, 6, PieceType.KNIGHT, 1)), Cell(Piece(7, 7, PieceType.ROOK, 1))]]

    table2_for_game_test_when_target_cell_is_occupied = \
        [[Cell(Piece(0, 0, PieceType.ROOK, -1)), Cell(Piece(0, 1, PieceType.KNIGHT, -1)),
          Cell(Piece(0, 2, PieceType.BISHOP, -1)), Cell(Piece(0, 3, PieceType.QUEEN, -1)),
          Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.BISHOP, -1)),
          Cell(Piece(0, 6, PieceType.KNIGHT, -1)), Cell(Piece(0, 7, PieceType.ROOK, -1))],

         [Cell(Piece(1, 0, PieceType.PAWN, -1)), Cell(Piece(1, 1, PieceType.NO_TYPE, -1)),
          Cell(Piece(1, 2, PieceType.PAWN, -1)), Cell(Piece(1, 3, PieceType.PAWN, -1)),
          Cell(Piece(1, 4, PieceType.PAWN, -1)), Cell(Piece(1, 5, PieceType.PAWN, -1)),
          Cell(Piece(1, 6, PieceType.PAWN, -1)), Cell(Piece(1, 7, PieceType.PAWN, -1))],

         [Cell(Piece(2, 0, PieceType.NO_TYPE, 0)), Cell(Piece(2, 1, PieceType.NO_TYPE, 0)),
          Cell(Piece(2, 2, PieceType.NO_TYPE, 0)), Cell(Piece(2, 3, PieceType.NO_TYPE, 0)),
          Cell(Piece(2, 4, PieceType.NO_TYPE, 0)), Cell(Piece(2, 5, PieceType.NO_TYPE, 0)),
          Cell(Piece(2, 6, PieceType.NO_TYPE, 0)), Cell(Piece(2, 7, PieceType.NO_TYPE, 0))],

         [Cell(Piece(3, 0, PieceType.NO_TYPE, 0)), Cell(Piece(3, 1, PieceType.PAWN, 1)),
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

         [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.PAWN, 1)),
          Cell(Piece(6, 2, PieceType.PAWN, 1)), Cell(Piece(6, 3, PieceType.PAWN, 1)),
          Cell(Piece(6, 4, PieceType.PAWN, 1)), Cell(Piece(6, 5, PieceType.PAWN, 1)),
          Cell(Piece(6, 6, PieceType.PAWN, 1)), Cell(Piece(6, 7, PieceType.PAWN, 1))],

         [Cell(Piece(7, 0, PieceType.NO_TYPE, 0)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
          Cell(Piece(7, 2, PieceType.KING, 1)), Cell(Piece(7, 3, PieceType.ROOK, 1)),
          Cell(Piece(7, 4, PieceType.NO_TYPE, 0)), Cell(Piece(7, 5, PieceType.BISHOP, 1)),
          Cell(Piece(7, 6, PieceType.KNIGHT, 1)), Cell(Piece(7, 7, PieceType.ROOK, 1))]]

    table_for_game_test_in_case_of_en_passant_step = \
        [[Cell(Piece(0, 0, PieceType.ROOK, -1)), Cell(Piece(0, 1, PieceType.KNIGHT, -1)),
          Cell(Piece(0, 2, PieceType.BISHOP, -1)), Cell(Piece(0, 3, PieceType.QUEEN, -1)),
          Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.BISHOP, -1)),
          Cell(Piece(0, 6, PieceType.KNIGHT, -1)), Cell(Piece(0, 7, PieceType.ROOK, -1))],

         [Cell(Piece(1, 0, PieceType.PAWN, -1)), Cell(Piece(1, 1, PieceType.PAWN, -1)),
          Cell(Piece(1, 2, PieceType.PAWN, -1)), Cell(Piece(1, 3, PieceType.PAWN, -1)),
          Cell(Piece(1, 4, PieceType.PAWN, -1)), Cell(Piece(1, 5, PieceType.PAWN, -1)),
          Cell(Piece(1, 6, PieceType.PAWN, -1)), Cell(Piece(1, 7, PieceType.PAWN, -1))],

         [Cell(Piece(2, 0, PieceType.NO_TYPE, 0)), Cell(Piece(2, 1, PieceType.NO_TYPE, 0)),
          Cell(Piece(2, 2, PieceType.NO_TYPE, 0)), Cell(Piece(2, 3, PieceType.NO_TYPE, 0)),
          Cell(Piece(2, 4, PieceType.NO_TYPE, 0)), Cell(Piece(2, 5, PieceType.NO_TYPE, 0)),
          Cell(Piece(2, 6, PieceType.NO_TYPE, 0)), Cell(Piece(2, 7, PieceType.NO_TYPE, 0))],

         [Cell(Piece(3, 0, PieceType.PAWN, 1)), Cell(Piece(3, 1, PieceType.NO_TYPE, 0)),
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

         [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.PAWN, 1)),
          Cell(Piece(6, 2, PieceType.PAWN, 1)), Cell(Piece(6, 3, PieceType.PAWN, 1)),
          Cell(Piece(6, 4, PieceType.PAWN, 1)), Cell(Piece(6, 5, PieceType.PAWN, 1)),
          Cell(Piece(6, 6, PieceType.PAWN, 1)), Cell(Piece(6, 7, PieceType.PAWN, 1))],

         [Cell(Piece(7, 0, PieceType.ROOK, 1)), Cell(Piece(7, 1, PieceType.KNIGHT, 1)),
          Cell(Piece(7, 2, PieceType.BISHOP, 1)), Cell(Piece(7, 3, PieceType.QUEEN, 1)),
          Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.BISHOP, 1)),
          Cell(Piece(7, 6, PieceType.KNIGHT, 1)), Cell(Piece(7, 7, PieceType.ROOK, 1))]]

    table2_for_game_test_in_case_of_en_passant_step = \
        [[Cell(Piece(0, 0, PieceType.ROOK, -1)), Cell(Piece(0, 1, PieceType.KNIGHT, -1)),
          Cell(Piece(0, 2, PieceType.BISHOP, -1)), Cell(Piece(0, 3, PieceType.QUEEN, -1)),
          Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.BISHOP, -1)),
          Cell(Piece(0, 6, PieceType.KNIGHT, -1)), Cell(Piece(0, 7, PieceType.ROOK, -1))],

         [Cell(Piece(1, 0, PieceType.PAWN, -1)), Cell(Piece(1, 1, PieceType.NO_TYPE, 0)),
          Cell(Piece(1, 2, PieceType.PAWN, -1)), Cell(Piece(1, 3, PieceType.PAWN, -1)),
          Cell(Piece(1, 4, PieceType.PAWN, -1)), Cell(Piece(1, 5, PieceType.PAWN, -1)),
          Cell(Piece(1, 6, PieceType.PAWN, -1)), Cell(Piece(1, 7, PieceType.PAWN, -1))],

         [Cell(Piece(2, 0, PieceType.NO_TYPE, 0)), Cell(Piece(2, 1, PieceType.PAWN, 1)),
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

         [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.PAWN, 1)),
          Cell(Piece(6, 2, PieceType.PAWN, 1)), Cell(Piece(6, 3, PieceType.PAWN, 1)),
          Cell(Piece(6, 4, PieceType.PAWN, 1)), Cell(Piece(6, 5, PieceType.PAWN, 1)),
          Cell(Piece(6, 6, PieceType.PAWN, 1)), Cell(Piece(6, 7, PieceType.PAWN, 1))],

         [Cell(Piece(7, 0, PieceType.ROOK, 1)), Cell(Piece(7, 1, PieceType.KNIGHT, 1)),
          Cell(Piece(7, 2, PieceType.BISHOP, 1)), Cell(Piece(7, 3, PieceType.QUEEN, 1)),
          Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.BISHOP, 1)),
          Cell(Piece(7, 6, PieceType.KNIGHT, 1)), Cell(Piece(7, 7, PieceType.ROOK, 1))]]

    table_for_game_test_promote_pawn = \
        [[Cell(Piece(0, 0, PieceType.ROOK, -1)), Cell(Piece(0, 1, PieceType.KNIGHT, -1)),
          Cell(Piece(0, 2, PieceType.BISHOP, -1)), Cell(Piece(0, 3, PieceType.QUEEN, -1)),
          Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.BISHOP, -1)),
          Cell(Piece(0, 6, PieceType.KNIGHT, -1)), Cell(Piece(0, 7, PieceType.ROOK, -1))],

         [Cell(Piece(1, 0, PieceType.PAWN, 1)), Cell(Piece(1, 1, PieceType.PAWN, -1)),
          Cell(Piece(1, 2, PieceType.PAWN, -1)), Cell(Piece(1, 3, PieceType.PAWN, -1)),
          Cell(Piece(1, 4, PieceType.PAWN, -1)), Cell(Piece(1, 5, PieceType.PAWN, -1)),
          Cell(Piece(1, 6, PieceType.PAWN, -1)), Cell(Piece(1, 7, PieceType.PAWN, -1))],

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

         [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.PAWN, 1)),
          Cell(Piece(6, 2, PieceType.PAWN, 1)), Cell(Piece(6, 3, PieceType.PAWN, 1)),
          Cell(Piece(6, 4, PieceType.PAWN, 1)), Cell(Piece(6, 5, PieceType.PAWN, 1)),
          Cell(Piece(6, 6, PieceType.PAWN, 1)), Cell(Piece(6, 7, PieceType.PAWN, 1))],

         [Cell(Piece(7, 0, PieceType.ROOK, 1)), Cell(Piece(7, 1, PieceType.KNIGHT, 1)),
          Cell(Piece(7, 2, PieceType.BISHOP, 1)), Cell(Piece(7, 3, PieceType.QUEEN, 1)),
          Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.BISHOP, 1)),
          Cell(Piece(7, 6, PieceType.KNIGHT, 1)), Cell(Piece(7, 7, PieceType.ROOK, 1))]]

    table_for_game_test_is_king_targeted = \
     [[Cell(Piece(0, 0, PieceType.ROOK, -1)), Cell(Piece(0, 1, PieceType.KNIGHT, -1)),
       Cell(Piece(0, 2, PieceType.BISHOP, -1)), Cell(Piece(0, 3, PieceType.QUEEN, -1)),
       Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.BISHOP, -1)),
       Cell(Piece(0, 6, PieceType.KNIGHT, -1)), Cell(Piece(0, 7, PieceType.ROOK, -1))],

      [Cell(Piece(1, 0, PieceType.PAWN, 1)), Cell(Piece(1, 1, PieceType.PAWN, -1)),
       Cell(Piece(1, 2, PieceType.PAWN, -1)), Cell(Piece(1, 3, PieceType.PAWN, -1)),
       Cell(Piece(1, 4, PieceType.PAWN, -1)), Cell(Piece(1, 5, PieceType.PAWN, -1)),
       Cell(Piece(1, 6, PieceType.PAWN, -1)), Cell(Piece(1, 7, PieceType.PAWN, -1))],

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

      [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.PAWN, 1)),
       Cell(Piece(6, 2, PieceType.PAWN, 1)), Cell(Piece(6, 3, PieceType.PAWN, 1)),
       Cell(Piece(6, 4, PieceType.PAWN, 1)), Cell(Piece(6, 5, PieceType.PAWN, -1)),
       Cell(Piece(6, 6, PieceType.PAWN, 1)), Cell(Piece(6, 7, PieceType.PAWN, 1))],

      [Cell(Piece(7, 0, PieceType.ROOK, 1)), Cell(Piece(7, 1, PieceType.KNIGHT, 1)),
       Cell(Piece(7, 2, PieceType.BISHOP, 1)), Cell(Piece(7, 3, PieceType.QUEEN, 1)),
       Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.BISHOP, 1)),
       Cell(Piece(7, 6, PieceType.KNIGHT, 1)), Cell(Piece(7, 7, PieceType.ROOK, 1))]]

    table_for_game_test_filter_wrong_moves = \
     [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 6, PieceType.NO_TYPE, 0)), Cell(Piece(0, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(1, 0, PieceType.NO_TYPE, 0)), Cell(Piece(1, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 2, PieceType.NO_TYPE, 0)), Cell(Piece(1, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 4, PieceType.ROOK, -1)), Cell(Piece(1, 5, PieceType.NO_TYPE, 0)),
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
       Cell(Piece(6, 4, PieceType.BISHOP, 1)), Cell(Piece(6, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 6, PieceType.NO_TYPE, 0)), Cell(Piece(6, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(7, 0, PieceType.NO_TYPE, 0)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 2, PieceType.NO_TYPE, 0)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.NO_TYPE, 0))]]

    table2_for_game_test_filter_wrong_moves = \
     [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 6, PieceType.NO_TYPE, 0)), Cell(Piece(0, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(1, 0, PieceType.NO_TYPE, 0)), Cell(Piece(1, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 2, PieceType.NO_TYPE, 0)), Cell(Piece(1, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 4, PieceType.KNIGHT, -1)), Cell(Piece(1, 5, PieceType.NO_TYPE, 0)),
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
       Cell(Piece(5, 4, PieceType.NO_TYPE, 0)), Cell(Piece(5, 5, PieceType.PAWN, 1)),
       Cell(Piece(5, 6, PieceType.NO_TYPE, 0)), Cell(Piece(5, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 2, PieceType.NO_TYPE, 0)), Cell(Piece(6, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 4, PieceType.NO_TYPE, 0)), Cell(Piece(6, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 6, PieceType.NO_TYPE, 0)), Cell(Piece(6, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(7, 0, PieceType.NO_TYPE, 0)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 2, PieceType.NO_TYPE, 0)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.NO_TYPE, 0))]]

    table_for_game_test_is_stalemate = \
     [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 6, PieceType.NO_TYPE, 0)), Cell(Piece(0, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(1, 0, PieceType.NO_TYPE, 0)), Cell(Piece(1, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 2, PieceType.NO_TYPE, 0)), Cell(Piece(1, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 4, PieceType.ROOK, -1)), Cell(Piece(1, 5, PieceType.NO_TYPE, 0)),
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
       Cell(Piece(5, 4, PieceType.NO_TYPE, 0)), Cell(Piece(5, 5, PieceType.PAWN, 1)),
       Cell(Piece(5, 6, PieceType.NO_TYPE, 0)), Cell(Piece(5, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 2, PieceType.NO_TYPE, 0)), Cell(Piece(6, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 4, PieceType.NO_TYPE, 0)), Cell(Piece(6, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 6, PieceType.NO_TYPE, 0)), Cell(Piece(6, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(7, 0, PieceType.NO_TYPE, 0)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 2, PieceType.NO_TYPE, 0)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.NO_TYPE, 0))]]

    table2_for_game_test_is_stalemate = \
     [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 6, PieceType.NO_TYPE, 0)), Cell(Piece(0, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(1, 0, PieceType.NO_TYPE, 0)), Cell(Piece(1, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 2, PieceType.NO_TYPE, 0)), Cell(Piece(1, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 4, PieceType.PAWN, -1)), Cell(Piece(1, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 6, PieceType.NO_TYPE, 0)), Cell(Piece(1, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(2, 0, PieceType.NO_TYPE, 0)), Cell(Piece(2, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(2, 2, PieceType.NO_TYPE, 0)), Cell(Piece(2, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(2, 4, PieceType.PAWN, 1)), Cell(Piece(2, 5, PieceType.NO_TYPE, 0)),
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

      [Cell(Piece(7, 0, PieceType.NO_TYPE, 0)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 2, PieceType.NO_TYPE, 0)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.NO_TYPE, 0))]]

    table3_for_game_test_is_stalemate = \
     [[Cell(Piece(0, 0, PieceType.KING, -1)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 4, PieceType.NO_TYPE, 0)), Cell(Piece(0, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 6, PieceType.QUEEN, -1)), Cell(Piece(0, 7, PieceType.ROOK, -1))],

      [Cell(Piece(1, 0, PieceType.NO_TYPE, 0)), Cell(Piece(1, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 2, PieceType.NO_TYPE, 0)), Cell(Piece(1, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 4, PieceType.NO_TYPE, 0)), Cell(Piece(1, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 6, PieceType.NO_TYPE, 0)), Cell(Piece(1, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(2, 0, PieceType.NO_TYPE, 0)), Cell(Piece(2, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(2, 2, PieceType.KNIGHT, -1)), Cell(Piece(2, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(2, 4, PieceType.NO_TYPE, 0)), Cell(Piece(2, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(2, 6, PieceType.NO_TYPE, 0)), Cell(Piece(2, 7, PieceType.BISHOP, 1))],

      [Cell(Piece(3, 0, PieceType.PAWN, -1)), Cell(Piece(3, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(3, 2, PieceType.PAWN, 1)), Cell(Piece(3, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(3, 4, PieceType.NO_TYPE, 0)), Cell(Piece(3, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(3, 6, PieceType.NO_TYPE, 0)), Cell(Piece(3, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(4, 0, PieceType.PAWN, 1)), Cell(Piece(4, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(4, 2, PieceType.NO_TYPE, 0)), Cell(Piece(4, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(4, 4, PieceType.NO_TYPE, 0)), Cell(Piece(4, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(4, 6, PieceType.NO_TYPE, 0)), Cell(Piece(4, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(5, 0, PieceType.NO_TYPE, 0)), Cell(Piece(5, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 2, PieceType.NO_TYPE, 0)), Cell(Piece(5, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 4, PieceType.NO_TYPE, 0)), Cell(Piece(5, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 6, PieceType.NO_TYPE, 0)), Cell(Piece(5, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(6, 0, PieceType.ROOK, -1)), Cell(Piece(6, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 2, PieceType.NO_TYPE, 0)), Cell(Piece(6, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 4, PieceType.NO_TYPE, 0)), Cell(Piece(6, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 6, PieceType.NO_TYPE, 0)), Cell(Piece(6, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(7, 0, PieceType.NO_TYPE, -0)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 2, PieceType.NO_TYPE, 0)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.NO_TYPE, 0)), Cell(Piece(7, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.KING, 1))]]

    table_for_steps_if_king_is_targeted = \
     [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 4, PieceType.NO_TYPE, 0)), Cell(Piece(0, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 6, PieceType.NO_TYPE, 0)), Cell(Piece(0, 7, PieceType.KING, 1))],

      [Cell(Piece(1, 0, PieceType.NO_TYPE, 0)), Cell(Piece(1, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 2, PieceType.NO_TYPE, 0)), Cell(Piece(1, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 4, PieceType.NO_TYPE, 0)), Cell(Piece(1, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 6, PieceType.NO_TYPE, 0)), Cell(Piece(1, 7, PieceType.PAWN, 1))],

      [Cell(Piece(2, 0, PieceType.NO_TYPE, 0)), Cell(Piece(2, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(2, 2, PieceType.NO_TYPE, 0)), Cell(Piece(2, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(2, 4, PieceType.NO_TYPE, 0)), Cell(Piece(2, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(2, 6, PieceType.NO_TYPE, 0)), Cell(Piece(2, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(3, 0, PieceType.NO_TYPE, 0)), Cell(Piece(3, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(3, 2, PieceType.NO_TYPE, 0)), Cell(Piece(3, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(3, 4, PieceType.NO_TYPE, 0)), Cell(Piece(3, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(3, 6, PieceType.NO_TYPE, 0)), Cell(Piece(3, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(4, 0, PieceType.NO_TYPE, 0)), Cell(Piece(4, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(4, 2, PieceType.NO_TYPE, 0)), Cell(Piece(4, 3, PieceType.BISHOP, -1)),
       Cell(Piece(4, 4, PieceType.NO_TYPE, 0)), Cell(Piece(4, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(4, 6, PieceType.NO_TYPE, 0)), Cell(Piece(4, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(5, 0, PieceType.NO_TYPE, 0)), Cell(Piece(5, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 2, PieceType.NO_TYPE, 0)), Cell(Piece(5, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 4, PieceType.NO_TYPE, 0)), Cell(Piece(5, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 6, PieceType.ROOK, -1)), Cell(Piece(5, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 2, PieceType.NO_TYPE, 0)), Cell(Piece(6, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 4, PieceType.NO_TYPE, 0)), Cell(Piece(6, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 6, PieceType.NO_TYPE, 0)), Cell(Piece(6, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(7, 0, PieceType.NO_TYPE, 0)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 2, PieceType.NO_TYPE, 0)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.NO_TYPE, 0)), Cell(Piece(7, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.KING, -1))]]

    table2_for_steps_if_king_is_targeted = \
     [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
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
       Cell(Piece(5, 6, PieceType.NO_TYPE, 0)), Cell(Piece(5, 7, PieceType.ROOK, -1))],

      [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 2, PieceType.NO_TYPE, 0)), Cell(Piece(6, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 4, PieceType.NO_TYPE, 0)), Cell(Piece(6, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 6, PieceType.NO_TYPE, 0)), Cell(Piece(6, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(7, 0, PieceType.PAWN, 1)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 2, PieceType.NO_TYPE, 0)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.NO_TYPE, 0)), Cell(Piece(7, 5, PieceType.BISHOP, 1)),
       Cell(Piece(7, 6, PieceType.BISHOP, 1)), Cell(Piece(7, 7, PieceType.KING, 1))]]

    table_for_get_index_of_item = \
     [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
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
       Cell(Piece(5, 6, PieceType.NO_TYPE, 0)), Cell(Piece(5, 7, PieceType.PAWN, -1))],

      [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 2, PieceType.NO_TYPE, 0)), Cell(Piece(6, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 4, PieceType.NO_TYPE, 0)), Cell(Piece(6, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 6, PieceType.NO_TYPE, 0)), Cell(Piece(6, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(7, 0, PieceType.ROOK, 1)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 2, PieceType.NO_TYPE, 0)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.ROOK, 1))]]


    table2_for_get_index_of_item = \
     [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
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
       Cell(Piece(5, 6, PieceType.NO_TYPE, 0)), Cell(Piece(5, 7, PieceType.PAWN, -1))],

      [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 2, PieceType.NO_TYPE, 0)), Cell(Piece(6, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 4, PieceType.NO_TYPE, 0)), Cell(Piece(6, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 6, PieceType.NO_TYPE, 0)), Cell(Piece(6, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(7, 0, PieceType.ROOK, 1)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 2, PieceType.NO_TYPE, 0)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.BISHOP, 1)),
       Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.ROOK, 1))]]


    table_for_check_king_steps = \
     [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.PAWN, -1)),
       Cell(Piece(0, 6, PieceType.PAWN, -1)), Cell(Piece(0, 7, PieceType.NO_TYPE, 0))],

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
       Cell(Piece(6, 4, PieceType.KING, 1)), Cell(Piece(6, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 6, PieceType.NO_TYPE, 0)), Cell(Piece(6, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(7, 0, PieceType.PAWN, -1)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 2, PieceType.NO_TYPE, 0)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.NO_TYPE, 0)), Cell(Piece(7, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.PAWN, -1))]]

    table2_for_check_king_steps = \
     [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.PAWN, -1)),
       Cell(Piece(0, 6, PieceType.PAWN, -1)), Cell(Piece(0, 7, PieceType.NO_TYPE, 0))],

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

      [Cell(Piece(7, 0, PieceType.ROOK, 1)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 2, PieceType.NO_TYPE, 0)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.ROOK, 1))]]

    table_for_get_non_targeted_king_cells = \
     [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.PAWN, -1)),
       Cell(Piece(0, 6, PieceType.PAWN, -1)), Cell(Piece(0, 7, PieceType.NO_TYPE, 0))],

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
       Cell(Piece(5, 2, PieceType.PAWN, -1)), Cell(Piece(5, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 4, PieceType.NO_TYPE, 0)), Cell(Piece(5, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 6, PieceType.PAWN, -1)), Cell(Piece(5, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 2, PieceType.NO_TYPE, 0)), Cell(Piece(6, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 4, PieceType.NO_TYPE, 0)), Cell(Piece(6, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 6, PieceType.NO_TYPE, 0)), Cell(Piece(6, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(7, 0, PieceType.PAWN, 1)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 2, PieceType.NO_TYPE, 0)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.PAWN, 1))]]

    table2_for_get_non_targeted_king_cells = \
     [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.PAWN, -1)),
       Cell(Piece(0, 6, PieceType.PAWN, -1)), Cell(Piece(0, 7, PieceType.NO_TYPE, 0))],

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
       Cell(Piece(3, 4, PieceType.PAWN, -1)), Cell(Piece(3, 5, PieceType.PAWN, -1)),
       Cell(Piece(3, 6, PieceType.NO_TYPE, 0)), Cell(Piece(3, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(4, 0, PieceType.NO_TYPE, 0)), Cell(Piece(4, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(4, 2, PieceType.NO_TYPE, 0)), Cell(Piece(4, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(4, 4, PieceType.NO_TYPE, 0)), Cell(Piece(4, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(4, 6, PieceType.PAWN, -1)), Cell(Piece(4, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(5, 0, PieceType.NO_TYPE, 0)), Cell(Piece(5, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 2, PieceType.PAWN, -1)), Cell(Piece(5, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 4, PieceType.KING, 1)), Cell(Piece(5, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 6, PieceType.PAWN, -1)), Cell(Piece(5, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 2, PieceType.NO_TYPE, 0)), Cell(Piece(6, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 4, PieceType.NO_TYPE, 0)), Cell(Piece(6, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 6, PieceType.NO_TYPE, 0)), Cell(Piece(6, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(7, 0, PieceType.PAWN, 1)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 2, PieceType.NO_TYPE, 0)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.NO_TYPE, 0)), Cell(Piece(7, 5, PieceType.BISHOP, -1)),
       Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.PAWN, 1))]]

    table_for_castling_steps = \
     [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.PAWN, -1)),
       Cell(Piece(0, 6, PieceType.PAWN, -1)), Cell(Piece(0, 7, PieceType.NO_TYPE, 0))],

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
       Cell(Piece(5, 2, PieceType.PAWN, -1)), Cell(Piece(5, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 4, PieceType.NO_TYPE, 0)), Cell(Piece(5, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 6, PieceType.PAWN, -1)), Cell(Piece(5, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 2, PieceType.NO_TYPE, 0)), Cell(Piece(6, 3, PieceType.PAWN, -1)),
       Cell(Piece(6, 4, PieceType.NO_TYPE, 0)), Cell(Piece(6, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 6, PieceType.NO_TYPE, 0)), Cell(Piece(6, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(7, 0, PieceType.ROOK, 1)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 2, PieceType.NO_TYPE, 0)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.ROOK, 1))]]

    table2_for_castling_steps = \
     [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.PAWN, -1)),
       Cell(Piece(0, 6, PieceType.PAWN, -1)), Cell(Piece(0, 7, PieceType.NO_TYPE, 0))],

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
       Cell(Piece(5, 2, PieceType.PAWN, -1)), Cell(Piece(5, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 4, PieceType.NO_TYPE, 0)), Cell(Piece(5, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 6, PieceType.PAWN, -1)), Cell(Piece(5, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 2, PieceType.PAWN, -1)), Cell(Piece(6, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 4, PieceType.NO_TYPE, 0)), Cell(Piece(6, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 6, PieceType.PAWN, -1)), Cell(Piece(6, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(7, 0, PieceType.ROOK, 1)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 2, PieceType.NO_TYPE, 0)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.ROOK, 1))]]

    table_for_possible_knight_steps = \
     [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.PAWN, -1)),
       Cell(Piece(0, 6, PieceType.PAWN, -1)), Cell(Piece(0, 7, PieceType.NO_TYPE, 0))],

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

      [Cell(Piece(5, 0, PieceType.PAWN, 1)), Cell(Piece(5, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 2, PieceType.PAWN, 1)), Cell(Piece(5, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 4, PieceType.NO_TYPE, 0)), Cell(Piece(5, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 6, PieceType.NO_TYPE, 0)), Cell(Piece(5, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 2, PieceType.NO_TYPE, 0)), Cell(Piece(6, 3, PieceType.KNIGHT, 1)),
       Cell(Piece(6, 4, PieceType.NO_TYPE, 0)), Cell(Piece(6, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 6, PieceType.NO_TYPE, 0)), Cell(Piece(6, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(7, 0, PieceType.NO_TYPE, 0)), Cell(Piece(7, 1, PieceType.KNIGHT, 1)),
       Cell(Piece(7, 2, PieceType.NO_TYPE, 0)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.NO_TYPE, 0))]]

    table2_for_possible_knight_steps = \
     [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.PAWN, -1)),
       Cell(Piece(0, 6, PieceType.NO_TYPE, 0)), Cell(Piece(0, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(1, 0, PieceType.NO_TYPE, 0)), Cell(Piece(1, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 2, PieceType.NO_TYPE, 0)), Cell(Piece(1, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 4, PieceType.NO_TYPE, 0)), Cell(Piece(1, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 6, PieceType.NO_TYPE, 0)), Cell(Piece(1, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(2, 0, PieceType.NO_TYPE, 0)), Cell(Piece(2, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(2, 2, PieceType.NO_TYPE, 0)), Cell(Piece(2, 3, PieceType.PAWN, -1)),
       Cell(Piece(2, 4, PieceType.NO_TYPE, 0)), Cell(Piece(2, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(2, 6, PieceType.NO_TYPE, 0)), Cell(Piece(2, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(3, 0, PieceType.NO_TYPE, 0)), Cell(Piece(3, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(3, 2, PieceType.NO_TYPE, 0)), Cell(Piece(3, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(3, 4, PieceType.NO_TYPE, 0)), Cell(Piece(3, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(3, 6, PieceType.NO_TYPE, 0)), Cell(Piece(3, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(4, 0, PieceType.NO_TYPE, 0)), Cell(Piece(4, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(4, 2, PieceType.NO_TYPE, 0)), Cell(Piece(4, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(4, 4, PieceType.KNIGHT, 1)), Cell(Piece(4, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(4, 6, PieceType.NO_TYPE, 0)), Cell(Piece(4, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(5, 0, PieceType.NO_TYPE, 0)), Cell(Piece(5, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 2, PieceType.NO_TYPE, 0)), Cell(Piece(5, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 4, PieceType.NO_TYPE, 0)), Cell(Piece(5, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 6, PieceType.NO_TYPE, 0)), Cell(Piece(5, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 2, PieceType.NO_TYPE, 0)), Cell(Piece(6, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 4, PieceType.NO_TYPE, 0)), Cell(Piece(6, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 6, PieceType.NO_TYPE, 0)), Cell(Piece(6, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(7, 0, PieceType.NO_TYPE, 0)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 2, PieceType.NO_TYPE, 0)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.NO_TYPE, 0))]]

    table_for_possible_rook_steps = \
     [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.PAWN, -1)),
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

      [Cell(Piece(4, 0, PieceType.PAWN, 1)), Cell(Piece(4, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(4, 2, PieceType.NO_TYPE, 0)), Cell(Piece(4, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(4, 4, PieceType.NO_TYPE, 0)), Cell(Piece(4, 5, PieceType.ROOK, 1)),
       Cell(Piece(4, 6, PieceType.NO_TYPE, 0)), Cell(Piece(4, 7, PieceType.PAWN, -1))],

      [Cell(Piece(5, 0, PieceType.NO_TYPE, 0)), Cell(Piece(5, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 2, PieceType.NO_TYPE, 0)), Cell(Piece(5, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 4, PieceType.NO_TYPE, 0)), Cell(Piece(5, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 6, PieceType.NO_TYPE, 0)), Cell(Piece(5, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 2, PieceType.NO_TYPE, 0)), Cell(Piece(6, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 4, PieceType.NO_TYPE, 0)), Cell(Piece(6, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 6, PieceType.NO_TYPE, 0)), Cell(Piece(6, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(7, 0, PieceType.NO_TYPE, 0)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 2, PieceType.NO_TYPE, 0)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.PAWN, 1)),
       Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.NO_TYPE, 0))]]

    table_for_possible_pawn_steps = \
     [[Cell(Piece(0, 0, PieceType.ROOK, -1)), Cell(Piece(0, 1, PieceType.KNIGHT, -1)),
      Cell(Piece(0, 2, PieceType.BISHOP, -1)), Cell(Piece(0, 3, PieceType.QUEEN, -1)),
      Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.BISHOP, -1)),
      Cell(Piece(0, 6, PieceType.KNIGHT, -1)), Cell(Piece(0, 7, PieceType.ROOK, -1))],

     [Cell(Piece(1, 0, PieceType.NO_TYPE, 0)), Cell(Piece(1, 1, PieceType.PAWN, -1)),
      Cell(Piece(1, 2, PieceType.NO_TYPE, 0)), Cell(Piece(1, 3, PieceType.PAWN, -1)),
      Cell(Piece(1, 4, PieceType.PAWN, -1)), Cell(Piece(1, 5, PieceType.PAWN, -1)),
      Cell(Piece(1, 6, PieceType.PAWN, -1)), Cell(Piece(1, 7, PieceType.PAWN, -1))],

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

     [Cell(Piece(5, 0, PieceType.PAWN, -1)), Cell(Piece(5, 1, PieceType.NO_TYPE, 0)),
      Cell(Piece(5, 2, PieceType.PAWN, -1)), Cell(Piece(5, 3, PieceType.NO_TYPE, 0)),
      Cell(Piece(5, 4, PieceType.NO_TYPE, 0)), Cell(Piece(5, 5, PieceType.NO_TYPE, 0)),
      Cell(Piece(5, 6, PieceType.NO_TYPE, 0)), Cell(Piece(5, 7, PieceType.NO_TYPE, 0))],

     [Cell(Piece(6, 0, PieceType.PAWN, 1)), Cell(Piece(6, 1, PieceType.PAWN, 1)),
      Cell(Piece(6, 2, PieceType.PAWN, 1)), Cell(Piece(6, 3, PieceType.PAWN, 1)),
      Cell(Piece(6, 4, PieceType.PAWN, 1)), Cell(Piece(6, 5, PieceType.PAWN, 1)),
      Cell(Piece(6, 6, PieceType.PAWN, 1)), Cell(Piece(6, 7, PieceType.PAWN, 1))],

     [Cell(Piece(7, 0, PieceType.ROOK, 1)), Cell(Piece(7, 1, PieceType.KNIGHT, 1)),
      Cell(Piece(7, 2, PieceType.BISHOP, 1)), Cell(Piece(7, 3, PieceType.QUEEN, 1)),
      Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.BISHOP, 1)),
      Cell(Piece(7, 6, PieceType.KNIGHT, 1)), Cell(Piece(7, 7, PieceType.ROOK, 1))]]

    table2_for_possible_pawn_steps = \
     [[Cell(Piece(0, 0, PieceType.ROOK, -1)), Cell(Piece(0, 1, PieceType.KNIGHT, -1)),
       Cell(Piece(0, 2, PieceType.BISHOP, -1)), Cell(Piece(0, 3, PieceType.QUEEN, -1)),
       Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.BISHOP, -1)),
       Cell(Piece(0, 6, PieceType.KNIGHT, -1)), Cell(Piece(0, 7, PieceType.ROOK, -1))],

      [Cell(Piece(1, 0, PieceType.PAWN, -1)), Cell(Piece(1, 1, PieceType.PAWN, -1)),
       Cell(Piece(1, 2, PieceType.PAWN, -1)), Cell(Piece(1, 3, PieceType.PAWN, -1)),
       Cell(Piece(1, 4, PieceType.PAWN, -1)), Cell(Piece(1, 5, PieceType.PAWN, -1)),
       Cell(Piece(1, 6, PieceType.PAWN, -1)), Cell(Piece(1, 7, PieceType.PAWN, -1))],

      [Cell(Piece(2, 0, PieceType.NO_TYPE, 0)), Cell(Piece(2, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(2, 2, PieceType.NO_TYPE, 0)), Cell(Piece(2, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(2, 4, PieceType.NO_TYPE, 0)), Cell(Piece(2, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(2, 6, PieceType.NO_TYPE, 0)), Cell(Piece(2, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(3, 0, PieceType.NO_TYPE, 0)), Cell(Piece(3, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(3, 2, PieceType.PAWN, 1)), Cell(Piece(3, 3, PieceType.PAWN, 1)),
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

      [Cell(Piece(6, 0, PieceType.PAWN, 1)), Cell(Piece(6, 1, PieceType.PAWN, 1)),
       Cell(Piece(6, 2, PieceType.PAWN, 1)), Cell(Piece(6, 3, PieceType.PAWN, 1)),
       Cell(Piece(6, 4, PieceType.PAWN, 1)), Cell(Piece(6, 5, PieceType.PAWN, 1)),
       Cell(Piece(6, 6, PieceType.PAWN, 1)), Cell(Piece(6, 7, PieceType.PAWN, 1))],

      [Cell(Piece(7, 0, PieceType.ROOK, 1)), Cell(Piece(7, 1, PieceType.KNIGHT, 1)),
       Cell(Piece(7, 2, PieceType.BISHOP, 1)), Cell(Piece(7, 3, PieceType.QUEEN, 1)),
       Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.BISHOP, 1)),
       Cell(Piece(7, 6, PieceType.KNIGHT, 1)), Cell(Piece(7, 7, PieceType.ROOK, 1))]]

    table_for_possible_bishop_steps = \
     [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 6, PieceType.NO_TYPE, 0)), Cell(Piece(0, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(1, 0, PieceType.NO_TYPE, 0)), Cell(Piece(1, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 2, PieceType.NO_TYPE, 0)), Cell(Piece(1, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 4, PieceType.NO_TYPE, 0)), Cell(Piece(1, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 6, PieceType.NO_TYPE, 0)), Cell(Piece(1, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(2, 0, PieceType.NO_TYPE, 0)), Cell(Piece(2, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(2, 2, PieceType.NO_TYPE, 0)), Cell(Piece(2, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(2, 4, PieceType.NO_TYPE, 0)), Cell(Piece(2, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(2, 6, PieceType.NO_TYPE, 0)), Cell(Piece(2, 7, PieceType.PAWN, -1))],

      [Cell(Piece(3, 0, PieceType.NO_TYPE, 0)), Cell(Piece(3, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(3, 2, PieceType.NO_TYPE, 0)), Cell(Piece(3, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(3, 4, PieceType.NO_TYPE, 0)), Cell(Piece(3, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(3, 6, PieceType.NO_TYPE, 0)), Cell(Piece(3, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(4, 0, PieceType.NO_TYPE, 0)), Cell(Piece(4, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(4, 2, PieceType.NO_TYPE, 0)), Cell(Piece(4, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(4, 4, PieceType.NO_TYPE, 0)), Cell(Piece(4, 5, PieceType.BISHOP, 1)),
       Cell(Piece(4, 6, PieceType.NO_TYPE, 0)), Cell(Piece(4, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(5, 0, PieceType.NO_TYPE, 0)), Cell(Piece(5, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 2, PieceType.NO_TYPE, 0)), Cell(Piece(5, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 4, PieceType.NO_TYPE, 0)), Cell(Piece(5, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 6, PieceType.NO_TYPE, 0)), Cell(Piece(5, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 2, PieceType.NO_TYPE, 0)), Cell(Piece(6, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 4, PieceType.NO_TYPE, 0)), Cell(Piece(6, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 6, PieceType.NO_TYPE, 0)), Cell(Piece(6, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(7, 0, PieceType.NO_TYPE, 0)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 2, PieceType.PAWN, 1)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.NO_TYPE, 0))]]

    table_for_possible_queen_steps = \
     [[Cell(Piece(0, 0, PieceType.NO_TYPE, 0)), Cell(Piece(0, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 2, PieceType.NO_TYPE, 0)), Cell(Piece(0, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 4, PieceType.KING, -1)), Cell(Piece(0, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(0, 6, PieceType.NO_TYPE, 0)), Cell(Piece(0, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(1, 0, PieceType.NO_TYPE, 0)), Cell(Piece(1, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 2, PieceType.NO_TYPE, 0)), Cell(Piece(1, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 4, PieceType.NO_TYPE, 0)), Cell(Piece(1, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(1, 6, PieceType.NO_TYPE, 0)), Cell(Piece(1, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(2, 0, PieceType.NO_TYPE, 0)), Cell(Piece(2, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(2, 2, PieceType.NO_TYPE, 0)), Cell(Piece(2, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(2, 4, PieceType.NO_TYPE, 0)), Cell(Piece(2, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(2, 6, PieceType.NO_TYPE, 0)), Cell(Piece(2, 7, PieceType.PAWN, -1))],

      [Cell(Piece(3, 0, PieceType.NO_TYPE, 0)), Cell(Piece(3, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(3, 2, PieceType.NO_TYPE, 0)), Cell(Piece(3, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(3, 4, PieceType.NO_TYPE, 0)), Cell(Piece(3, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(3, 6, PieceType.NO_TYPE, 0)), Cell(Piece(3, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(4, 0, PieceType.PAWN, -1)), Cell(Piece(4, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(4, 2, PieceType.NO_TYPE, 0)), Cell(Piece(4, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(4, 4, PieceType.NO_TYPE, 0)), Cell(Piece(4, 5, PieceType.QUEEN, 1)),
       Cell(Piece(4, 6, PieceType.NO_TYPE, 0)), Cell(Piece(4, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(5, 0, PieceType.NO_TYPE, 0)), Cell(Piece(5, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 2, PieceType.NO_TYPE, 0)), Cell(Piece(5, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 4, PieceType.NO_TYPE, 0)), Cell(Piece(5, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(5, 6, PieceType.NO_TYPE, 0)), Cell(Piece(5, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(6, 0, PieceType.NO_TYPE, 0)), Cell(Piece(6, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 2, PieceType.NO_TYPE, 0)), Cell(Piece(6, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 4, PieceType.NO_TYPE, 0)), Cell(Piece(6, 5, PieceType.NO_TYPE, 0)),
       Cell(Piece(6, 6, PieceType.NO_TYPE, 0)), Cell(Piece(6, 7, PieceType.NO_TYPE, 0))],

      [Cell(Piece(7, 0, PieceType.NO_TYPE, 0)), Cell(Piece(7, 1, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 2, PieceType.PAWN, 1)), Cell(Piece(7, 3, PieceType.NO_TYPE, 0)),
       Cell(Piece(7, 4, PieceType.KING, 1)), Cell(Piece(7, 5, PieceType.PAWN, 1)),
       Cell(Piece(7, 6, PieceType.NO_TYPE, 0)), Cell(Piece(7, 7, PieceType.NO_TYPE, 0))]]