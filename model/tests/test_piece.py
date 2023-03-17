import unittest
from model.game import Game
from model.piece import Piece
from test_tables import TestTables

class TestPiece(unittest.TestCase):

    def test_delete_change_not_to_first_step(self):

        game = Game()

        cell_to_move_from = game.get_board_table()[6][0]
        piece = cell_to_move_from.get_piece()

        self.assertTrue(piece.get_is_first_step())

        game.move_piece(cell_to_move_from, game.get_board_table()[4][0])

        self.assertFalse(piece.get_is_first_step())

    def test_get_possible_steps_of_knight_when_it_can_step(self):

        game = Game(TestTables.table2_for_possible_knight_steps)
        board = game.get_board_table()

        piece: Piece = board[4][4].get_piece()
        actual_steps = piece.get_possible_steps(board, game.get_last_step(),
                                                game.get_white_player(), game.get_black_player(),
                                                game.get_castling_step(), game.get_castling_rook(),
                                                game.get_rook_target())

        expected_steps = [board[2][3], board[2][5], board[3][2], board[3][6],
                          board[6][3], board[6][5], board[5][2], board[5][6]]

        print(expected_steps)
        print(actual_steps)

        self.assertTrue(TestPiece.__correct_expected_steps(expected_steps, actual_steps))

    def test_get_possible_steps_of_knight_when_it_cannot_step(self):

        game = Game(TestTables.table_for_possible_knight_steps)
        board = game.get_board_table()

        piece: Piece = board[7][1].get_piece()
        actual_steps = piece.get_possible_steps(board, game.get_last_step(),
                                                game.get_white_player(), game.get_black_player(),
                                                game.get_castling_step(), game.get_castling_rook(),
                                                game.get_rook_target())
        expected_steps = []

        self.assertTrue(TestPiece.__correct_expected_steps(expected_steps, actual_steps))

    def test_get_possible_steps_of_king(self):

        game = Game()
        board = game.get_board_table()

        piece: Piece = board[7][4].get_piece()

        actual_steps = piece.get_possible_steps(board, game.get_last_step(),
                                                game.get_white_player(), game.get_black_player(),
                                                game.get_castling_step(), game.get_castling_rook(),
                                                game.get_rook_target)

        expected_steps = []

        self.assertEqual(expected_steps, actual_steps)

    def test_get_possible_steps_of_rook_when_it_cannot_step(self):

        game = Game()
        board = game.get_board_table()

        piece: Piece = board[7][0].get_piece()

        actual_steps = piece.get_possible_steps(board, game.get_last_step(),
                                                game.get_white_player(), game.get_black_player(),
                                                game.get_castling_step(), game.get_castling_rook(),
                                                game.get_rook_target)

        expected_steps = []

        self.assertEqual(expected_steps, actual_steps)

    def test_get_possible_steps_of_rook_when_it_can_step(self):

        game = Game(TestTables.table_for_possible_rook_steps)
        board = game.get_board_table()

        piece: Piece = board[4][5].get_piece()

        actual_steps = piece.get_possible_steps(board, game.get_last_step(),
                                                game.get_white_player(), game.get_black_player(),
                                                game.get_castling_step(), game.get_castling_rook(),
                                                game.get_rook_target)

        expected_steps = [board[4][1], board[4][2], board[4][3], board[4][4],
                          board[4][6], board[4][7], board[0][5], board[1][5],
                          board[2][5], board[3][5], board[5][5], board[6][5]]

        self.assertTrue(TestPiece.__correct_expected_steps(expected_steps, actual_steps))

    def test_get_possible_steps_of_pawn_when_it_can_step_and_it_is_first_step(self):

        game = Game(TestTables.table_for_possible_pawn_steps)
        board = game.get_board_table()

        piece: Piece = board[6][1].get_piece()

        actual_steps = piece.get_possible_steps(board, game.get_last_step(),
                                                game.get_white_player(), game.get_black_player(),
                                                game.get_castling_step(), game.get_castling_rook(),
                                                game.get_rook_target)

        expected_steps = [board[5][0], board[5][1], board[5][2], board[4][1]]

        self.assertTrue(TestPiece.__correct_expected_steps(expected_steps, actual_steps))

    def test_get_possible_steps_of_pawn_when_in_case_of_en_passant_on_left_side(self):

        game = Game(TestTables.table2_for_possible_pawn_steps)
        board = game.get_board_table()

        piece1: Piece = board[3][2].get_piece()

        piece1.change_to_not_first_step()

        p1_actual_steps = piece1.get_possible_steps(board, game.get_last_step(),
                                                    game.get_white_player(), game.get_black_player(),
                                                    game.get_castling_step(), game.get_castling_rook(),
                                                    game.get_rook_target)

        p1_expected_steps = [board[2][2]]

        self.assertEqual(p1_expected_steps, p1_actual_steps)

        game.move_piece(game.get_board_table()[1][0], game.get_board_table()[3][0])

        p1_actual_steps = piece1.get_possible_steps(board, game.get_last_step(),
                                                    game.get_white_player(), game.get_black_player(),
                                                    game.get_castling_step(), game.get_castling_rook(),
                                                    game.get_rook_target)

        p1_expected_steps = [board[2][2]]

        self.assertEqual(p1_expected_steps, p1_actual_steps)

        game.change_current_player()
        game.move_piece(game.get_board_table()[1][1], game.get_board_table()[3][1])

        p1_actual_steps = piece1.get_possible_steps(board, game.get_last_step(),
                                                    game.get_white_player(), game.get_black_player(),
                                                    game.get_castling_step(), game.get_castling_rook(),
                                                    game.get_rook_target)
        p1_expected_steps = [board[2][1], board[2][2]]

        self.assertTrue(TestPiece.__correct_expected_steps(p1_expected_steps, p1_actual_steps))

    def test_get_possible_steps_of_pawn_when_in_case_of_en_passant_on_right_side(self):

        game = Game(TestTables.table2_for_possible_pawn_steps)
        board = game.get_board_table()

        piece2: Piece = board[3][3].get_piece()

        piece2.change_to_not_first_step()

        p2_actual_steps = piece2.get_possible_steps(board, game.get_last_step(),
                                                    game.get_white_player(), game.get_black_player(),
                                                    game.get_castling_step(), game.get_castling_rook(),
                                                    game.get_rook_target)
        p2_expected_steps = [board[2][3]]

        self.assertEqual(p2_expected_steps, p2_actual_steps)

        game.move_piece(game.get_board_table()[1][5], game.get_board_table()[3][5])

        p2_actual_steps = piece2.get_possible_steps(board, game.get_last_step(),
                                                    game.get_white_player(), game.get_black_player(),
                                                    game.get_castling_step(), game.get_castling_rook(),
                                                    game.get_rook_target)
        p2_expected_steps = [board[2][3]]

        self.assertEqual(p2_expected_steps, p2_actual_steps)

        game.change_current_player()
        game.move_piece(game.get_board_table()[1][4], game.get_board_table()[3][4])

        p2_actual_steps = piece2.get_possible_steps(board, game.get_last_step(),
                                                    game.get_white_player(), game.get_black_player(),
                                                    game.get_castling_step(), game.get_castling_rook(),
                                                    game.get_rook_target)
        p2_expected_steps = [board[2][3], board[2][4]]

        self.assertTrue(self.__correct_expected_steps(p2_expected_steps, p2_actual_steps))

    def test_get_possible_steps_of_bishop_when_it_cannot_step(self):

        game = Game()
        board = game.get_board_table()

        piece: Piece = board[7][2].get_piece()

        actual_steps = piece.get_possible_steps(board, game.get_last_step(),
                                                game.get_white_player(), game.get_black_player(),
                                                game.get_castling_step(), game.get_castling_rook(),
                                                game.get_rook_target)

        expected_steps = []

        self.assertEqual(expected_steps, actual_steps)

    def test_get_possible_steps_of_bishop_when_it_can_step(self):

        game = Game(TestTables.table_for_possible_bishop_steps)
        board = game.get_board_table()

        piece: Piece = board[4][5].get_piece()

        actual_steps = piece.get_possible_steps(board, game.get_last_step(),
                                                game.get_white_player(), game.get_black_player(),
                                                game.get_castling_step(), game.get_castling_rook(),
                                                game.get_rook_target)

        expected_steps = [board[0][1], board[1][2], board[2][3], board[3][4],
                          board[3][6], board[2][7], board[5][4], board[5][6],
                          board[6][3], board[6][7]]

        self.assertTrue(TestPiece.__correct_expected_steps(expected_steps, actual_steps))

    def test_get_possible_steps_of_queen_when_it_cannot_step(self):

        game = Game()
        board = game.get_board_table()

        piece: Piece = board[7][3].get_piece()

        actual_steps = piece.get_possible_steps(board, game.get_last_step(),
                                                game.get_white_player(), game.get_black_player(),
                                                game.get_castling_step(), game.get_castling_rook(),
                                                game.get_rook_target)

        expected_steps = []

        self.assertEqual(expected_steps, actual_steps)

    def test_get_possible_steps_of_queen_when_it_can_step(self):

        game = Game(TestTables.table_for_possible_queen_steps)
        board = game.get_board_table()

        piece: Piece = board[4][5].get_piece()

        actual_steps = piece.get_possible_steps(board, game.get_last_step(),
                                                game.get_white_player(), game.get_black_player(),
                                                game.get_castling_step(), game.get_castling_rook(),
                                                game.get_rook_target)

        expected_steps = [board[0][1], board[1][2], board[2][3], board[3][4],
                          board[3][6], board[2][7], board[5][4], board[5][6],
                          board[6][3], board[6][7], board[4][0], board[4][1],
                          board[4][2], board[4][3], board[4][4], board[4][6],
                          board[4][7], board[0][5], board[1][5], board[2][5],
                          board[3][5], board[5][5], board[6][5]]

        self.assertTrue(TestPiece.__correct_expected_steps(expected_steps, actual_steps))




    @staticmethod
    def __correct_expected_steps(expected_steps, steps):

        if len(expected_steps) != len(steps):
            return False

        for i in expected_steps:

            if i not in steps:
                return False

        return True


if __name__ == "__main__":
    unittest.main()

