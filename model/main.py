#!/usr/bin/env python3
from model.game import Game

def main():
    game = Game()
    board = game.get_board()
    table = game.get_board_table()
    board.print_board()
    game.print_possible_steps(0, 4)
    s = game.get_board_table()[6][3]
    t = game.get_board_table()[4][3]
    game.move_piece(s, t)
    print("---")
    board.print_board()
    s = game.get_board_table()[1][3]
    t = game.get_board_table()[3][3]
    game.move_piece(s, t)
    print("---")
    board.print_board()












if __name__ == "__main__":
    main()
