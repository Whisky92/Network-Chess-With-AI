import unittest
from model.game import Game
from test_tables import TestTables
from model.piece_type import PieceType


class TestGame(unittest.TestCase):

    def test_change_current_player(self):

        game = Game()

        self.assertEqual(game.get_current_player(), game.get_white_player())

        game.change_current_player()
        self.assertEqual(game.get_current_player(), game.get_black_player())

        game.change_current_player()
        self.assertEqual(game.get_current_player(), game.get_white_player())

    def test_move_piece_with_normal_move(self):

        game = Game()

        cell_to_move_from = game.get_board_table()[6][0]
        piece = cell_to_move_from.get_piece()

        cell_to_move_to = game.get_board_table()[4][0]

        self.assertTrue(piece.get_is_first_step())

        game.get_possible_steps(6, 0)
        game.move_piece(cell_to_move_from, cell_to_move_to)

        self.assertEqual(piece, cell_to_move_to.get_piece())
        self.assertEqual(game.get_board(), TestTables.table_for_game_test_one)

        self.assertFalse(piece.get_is_first_step())

        self.assertEqual(cell_to_move_to.get_piece().get_piece_x(), 4)
        self.assertEqual(cell_to_move_to.get_piece().get_piece_y(), 0)

    def test_move_piece_in_case_of_castling(self):

        game = Game(TestTables.table_for_game_test_castling)

        rook_start_cell = game.get_board_table()[7][0]
        rook = rook_start_cell.get_piece()

        cell_to_move_from = game.get_board_table()[7][4]
        piece = cell_to_move_from.get_piece()

        cell_to_move_to = game.get_board_table()[7][2]

        game.get_possible_steps(7, 4)
        game.move_piece(cell_to_move_from, cell_to_move_to)

        self.assertEqual(rook_start_cell.get_piece().get_piece_type(), PieceType.NO_TYPE)
        self.assertEqual(rook_start_cell.get_piece().get_direction(), 0)

        self.assertEqual(cell_to_move_from.get_piece().get_piece_type(), PieceType.NO_TYPE)
        self.assertEqual(cell_to_move_from.get_piece().get_direction(), 0)

        self.assertEqual(cell_to_move_to.get_piece(), piece)

        self.assertEqual(game.get_board_table()[7][3].get_piece(), rook)

        self.assertEqual(game.get_board(), TestTables.table2_for_game_test_castling)

    def test_move_piece_in_case_target_cell_is_occupied(self):

        game = Game(TestTables.table_for_game_test_when_target_cell_is_occupied)

        cell_to_move_from = game.get_board_table()[4][0]
        piece = cell_to_move_from.get_piece()

        cell_to_move_to = game.get_board_table()[3][1]
        target_piece = cell_to_move_to.get_piece()

        self.assertTrue(target_piece in game.get_black_player().get_pieces_on_board())

        game.get_possible_steps(4, 0)
        game.move_piece(cell_to_move_from, cell_to_move_to)

        self.assertEqual(cell_to_move_from.get_piece().get_piece_type(), PieceType.NO_TYPE)
        self.assertEqual(cell_to_move_from.get_piece().get_direction(), 0)

        self.assertTrue(target_piece not in game.get_current_player().get_pieces_on_board())

        self.assertEqual(cell_to_move_to.get_piece(), piece)

        self.assertEqual(game.get_board(), TestTables.table2_for_game_test_when_target_cell_is_occupied)

    def test_move_piece_in_case_of_en_passant(self):

        game = Game(TestTables.table_for_game_test_in_case_of_en_passant_step)

        game.change_current_player()

        cell_to_move_from = game.get_board_table()[3][0]
        piece = cell_to_move_from.get_piece()

        enemy_pawn_cell = game.get_board_table()[3][1]

        cell_to_move_to = game.get_board_table()[2][1]

        game.move_piece(game.get_board_table()[1][1], enemy_pawn_cell)

        self.assertEqual(game.get_last_step(), enemy_pawn_cell)

        target_piece = enemy_pawn_cell.get_piece()

        self.assertTrue(target_piece in game.get_black_player().get_pieces_on_board())

        game.move_piece(cell_to_move_from, cell_to_move_to)

        self.assertEqual(game.get_board(), TestTables.table2_for_game_test_in_case_of_en_passant_step)

        self.assertEqual(enemy_pawn_cell.get_piece().get_piece_type(), PieceType.NO_TYPE)
        self.assertEqual(enemy_pawn_cell.get_piece().get_direction(), 0)

        self.assertEqual(cell_to_move_to.get_piece(), piece)

        self.assertEqual(cell_to_move_from.get_piece().get_piece_type(), PieceType.NO_TYPE)
        self.assertEqual(cell_to_move_from.get_piece().get_direction(), 0)

        self.assertTrue(target_piece not in game.get_current_player().get_pieces_on_board())

        self.assertIsNone(game.get_last_step())

    def test_promote_pawn(self):

        game = Game(TestTables.table_for_game_test_promote_pawn)
        cell_to_move_to = game.get_board_table()[0][1]

        game.move_piece(game.get_board_table()[1][0], cell_to_move_to)

        self.assertEqual(cell_to_move_to.get_piece().get_piece_type(), PieceType.PAWN)

        game.promote_pawn(cell_to_move_to, PieceType.QUEEN)

        self.assertEqual(cell_to_move_to.get_piece().get_piece_type(), PieceType.QUEEN)

    def test_is_king_targeted(self):

        game = Game()

        self.assertFalse(game.is_king_targeted(game.get_current_player()))

        game2 = Game(TestTables.table_for_game_test_is_king_targeted)

        self.assertTrue(game2.is_king_targeted(game2.get_current_player()))

    def filter_wrong_moves(self):

        game = Game(TestTables.table_for_game_test_filter_wrong_moves)
        moves = game.filter_wrong_moves(6, 4)

        self.assertEqual(moves, [])

        game2 = Game(TestTables.table2_for_game_test_filter_wrong_moves)
        moves = game2.filter_wrong_moves(6, 5)

        self.assertEqual(moves, [game2.get_board_table()[5][5], game2.get_board_table()[4][5]])

    def test_get_possible_steps(self):

        game = Game()

        game.change_current_player()

        moves = game.get_possible_steps(1, 0)

        self.assertEqual(moves, [game.get_board_table()[2][0], game.get_board_table()[3][0]])

    def test_is_stalemate_when_king_is_targeted(self):

        game = Game(TestTables.table_for_game_test_is_stalemate)

        self.assertFalse(game.is_stalemate())

    def test_is_stalemate_when_other_pieces_can_move_free(self):

        game = Game()

        self.assertFalse(game.is_stalemate())

    def test_is_stalemate_when_king_can_move_free(self):

        game = Game(TestTables.table2_for_game_test_is_stalemate)

        self.assertFalse(game.is_stalemate())

    def test_is_stalemate_when_game_state_is_stalemate(self):

        game = Game(TestTables.table3_for_game_test_is_stalemate)

        self.assertTrue(game.is_stalemate())

    def test_steps_if_king_is_targeted_and_checkmate(self):

        game = Game(TestTables.table_for_steps_if_king_is_targeted)

        self.assertEqual(game.steps_if_king_is_targeted(), [])

    def test_steps_if_king_is_targeted_and_no_checkmate(self):

        game = Game(TestTables.table2_for_steps_if_king_is_targeted)

        expected_steps = [(game.get_board_table()[7][5], [game.get_board_table()[5][7]]),
                          (game.get_board_table()[7][6], [game.get_board_table()[6][7]]),
                          (game.get_board_table()[7][7], [game.get_board_table()[6][6]])]

        steps = game.steps_if_king_is_targeted()

        self.assertEqual(steps, expected_steps)

    def test_contains_start_cell_when_cell_contains_it(self):

        game = Game(TestTables.table2_for_steps_if_king_is_targeted)

        steps = game.steps_if_king_is_targeted()

        self.assertEqual(game.contains_start_cell(steps, game.get_board_table()[7][5]),
                         (game.get_board_table()[7][5], [game.get_board_table()[5][7]]))

    def test_contains_start_cell_when_cell_does_not_contain_it(self):

        game = Game(TestTables.table2_for_steps_if_king_is_targeted)

        steps = game.steps_if_king_is_targeted()

        self.assertIsNone(game.contains_start_cell(steps, game.get_board_table()[7][0]))

    def test_get_index_of_item_when_it_contains_the_cell(self):

        game = Game(TestTables.table_for_get_index_of_item)

        game.filter_wrong_moves(7, 4)

        index = Game.get_index_of_item(game.get_castling_step(), game.get_board_table()[7][6])
        expected_index = 0

        self.assertEqual(expected_index, index)

    def test_get_index_of_item_when_it_does_not_contain_the_cell(self):

        game = Game(TestTables.table2_for_get_index_of_item)

        game.filter_wrong_moves(7, 4)

        index = Game.get_index_of_item(game.get_castling_step(), game.get_board_table()[7][6])
        expected_index = -1

        self.assertEqual(expected_index, index)

if __name__ == "__main__":
    unittest.main()
