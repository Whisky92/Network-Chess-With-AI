#!/usr/bin/env python3
from model.game import Game
import copy

def main():
    game = Game()
    board = game.get_board()
    table = game.get_board_table()
    game.print_possible_steps(0, 4)
    game.get_possible_steps(7, 4)
    board.print_board()
    game.move_piece(table[6][4], table[4][4])
    print("------")
    board.print_board()
    print("........")
    game2 = copy.deepcopy(game)
    game2.get_board().print_board()













if __name__ == "__main__":
    main()
