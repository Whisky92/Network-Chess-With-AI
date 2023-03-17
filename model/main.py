#!/usr/bin/env python3
import model.tests.test_tables
from model.game import Game
from model.cell import Cell
from model.piece import Piece
from model.piece_type import PieceType
from model.board import Board


def main():
    # Main class is just for testing
    game = Game(model.tests.test_tables.TestTables.table_for_game_test_castling)
    board = game.get_board()
    table = game.get_board_table()
    board.print_board()
    game.get_possible_steps(7, 4)
    game.get_possible_steps(7, 4)
    game.get_possible_steps(7, 4)
    game.get_possible_steps(7, 4)
    game.move_piece(game.get_board_table()[7][4], game.get_board_table()[7][2])
    board.print_board()


if __name__ == "__main__":
    main()
