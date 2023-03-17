import unittest
from model.king_step_checker import KingStepChecker
from test_tables import TestTables
from model.game import Game

class TestKingStepChecker(unittest.TestCase):

    def test_check_king_steps_when_castling_is_not_possible(self):

        game = Game(TestTables.table_for_check_king_steps)

        board = game.get_board_table()

        steps = KingStepChecker.check_king_steps(board, 6, 4, game.get_white_player(),
                                                 game.get_black_player(), game.get_last_step(),
                                                 game.get_castling_step(), game.get_castling_rook(),
                                                 game.get_rook_target())

        expected_steps = [board[7][4], board[5][4], board[6][3], board[6][5],
                          board[7][3], board[7][5], board[5][3], board[5][5]]

        self.assertTrue(TestKingStepChecker.__correct_expected_steps(expected_steps, steps))

    def test_check_king_steps_when_castling_is_possible(self):

        game = Game(TestTables.table2_for_check_king_steps)

        board = game.get_board_table()

        KingStepChecker.check_king_steps(board, 7, 4, game.get_white_player(),
                                         game.get_black_player(), game.get_last_step(),
                                         game.get_castling_step(), game.get_castling_rook(),
                                         game.get_rook_target())

        steps = KingStepChecker.check_king_steps(board, 7, 4, game.get_white_player(),
                                                 game.get_black_player(), game.get_last_step(),
                                                 game.get_castling_step(), game.get_castling_rook(),
                                                 game.get_rook_target())

        expected_steps = [board[6][3], board[6][5], board[6][4],
                          board[7][3], board[7][5], board[7][2], board[7][6]]

        self.assertTrue(TestKingStepChecker.__correct_expected_steps(expected_steps, steps))

    def test_check_king_steps_all_king_cells_are_occupied(self):

        game = Game()

        steps = KingStepChecker.check_king_steps(game.get_board_table(), 7, 4, game.get_white_player(),
                                                 game.get_black_player(), game.get_last_step(),
                                                 game.get_castling_step(), game.get_castling_rook(),
                                                 game.get_rook_target())

        self.assertEqual([], steps)

    def test_get_king_cell(self):

        game = Game()

        king_cell = KingStepChecker.get_king_cell(game.get_board_table(), game.get_current_player())

        self.assertEqual(game.get_board_table()[7][4], king_cell)

    def test_check_steps_when_cell_is_out_of_board(self):

        game = Game()

        cell = game.get_board_table()[7][4]

        actual_result = KingStepChecker.check_cell(game.get_board_table(), cell, 8, 4)
        expected_result = []

        self.assertEqual(expected_result, actual_result)

    def test_check_steps_when_cell_belongs_to_ally_piece(self):

        game = Game()

        cell = game.get_board_table()[7][4]

        actual_result = KingStepChecker.check_cell(game.get_board_table(), cell, 7, 3)
        expected_result = []

        self.assertEqual(expected_result, actual_result)

    def test_check_steps_when_there_are_correct_cells(self):

        game = Game()

        cell = game.get_board_table()[6][2]

        actual_result = KingStepChecker.check_cell(game.get_board_table(), cell, 5, 2)
        expected_result = [game.get_board_table()[5][2]]

        self.assertEqual(expected_result, actual_result)

    def test_get_non_targeted_king_cells_when_there_are_targeted_cells(self):

        game = Game(TestTables.table_for_get_non_targeted_king_cells)

        board = game.get_board_table()

        actual_result = KingStepChecker.check_king_steps(board, 7, 4, game.get_white_player(),
                                                         game.get_black_player(), game.get_last_step(),
                                                         game.get_castling_step(), game.get_castling_rook(),
                                                         game.get_rook_target())
        expected_result = [board[7][3], board[7][5], board[6][4]]

        self.assertTrue(TestKingStepChecker.__correct_expected_steps(expected_result, actual_result))

    def test_get_non_targeted_king_cells_when_all_cells_are_targeted(self):

        game = Game(TestTables.table2_for_get_non_targeted_king_cells)

        actual_result = KingStepChecker.check_king_steps(game.get_board_table(), 5, 4, game.get_white_player(),
                                                         game.get_black_player(), game.get_last_step(),
                                                         game.get_castling_step(), game.get_castling_rook(),
                                                         game.get_rook_target())
        expected_result = []

        self.assertEqual(expected_result, actual_result)

    def test_add_castling_steps_to_possible_steps_when_king_is_targeted(self):

        game = Game(TestTables.table_for_castling_steps)

        board = game.get_board_table()


        actual_result = KingStepChecker.check_king_steps(board, 7, 4, game.get_white_player(),
                                                         game.get_black_player(), game.get_last_step(),
                                                         game.get_castling_step(), game.get_castling_rook(),
                                                         game.get_rook_target())

        expected_result = [board[7][3], board[7][5], board[6][4]]

        self.assertTrue(TestKingStepChecker.__correct_expected_steps(expected_result, actual_result))

    def test_add_castling_steps_to_possible_steps_when_inner_cells_are_targeted(self):

        game = Game(TestTables.table2_for_castling_steps)

        board = game.get_board_table()

        actual_result = KingStepChecker.check_king_steps(board, 7, 4, game.get_white_player(),
                                                         game.get_black_player(), game.get_last_step(),
                                                         game.get_castling_step(), game.get_castling_rook(),
                                                         game.get_rook_target())
        expected_result = [board[6][4]]

        self.assertEqual(expected_result, actual_result)

    def test_get_player_by_direction(self):

        game = Game()

        expected_result = game.get_white_player()
        actual_result = KingStepChecker.get_player_by_direction(game.get_current_player().get_direction(),
                                                                game.get_white_player(), game.get_black_player())

        self.assertEqual(expected_result, actual_result)

        game.change_current_player()

        expected_result = game.get_black_player()
        actual_result = KingStepChecker.get_player_by_direction(game.get_current_player().get_direction(),
                                                                game.get_white_player(), game.get_black_player())

        self.assertEqual(expected_result, actual_result)


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



