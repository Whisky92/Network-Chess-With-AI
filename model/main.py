#!/usr/bin/env python3
import model.tests.test_tables
from model.game import Game
from model.cell import Cell
from model.piece import Piece
from model.piece_type import PieceType
from model.board import Board
from model.colors import Color
from ai.ai_logic import AiLogic


def main():
    # Main class is just for testing
    game = Game()
    board = game.get_board()
    table = game.get_board_table()
    board.print_board()
    game.move_piece(table[7][1], table[5][0])
    print()
    board.print_board()
    game.move_piece(table[1][1], table[2][1])
    print()
    board.print_board()
    game.move_piece(table[6][4], table[4][4])
    print()
    board.print_board()
    game.move_piece(table[1][2], table[2][2])
    print()
    board.print_board()
    game.move_piece(table[7][3], table[5][5])
    print()
    board.print_board()
    game.move_piece(table[1][3], table[2][3])
    game.print_possible_steps(7, 4)


if __name__ == "__main__":
    main()
