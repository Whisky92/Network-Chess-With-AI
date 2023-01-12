#!/usr/bin/env python3
from game import Game

def main():
    game = Game()
    board = game.get_board()
    table = game.get_board_table()
    game.print_possible_steps(table[1][0])
    print(table[2][0] in game.get_possible_steps(table[1][0]))
    game.move_piece(table[1][0], table[2][0])
    board.print_piece_data(table[2][0])
    board.print_board()
if __name__ == "__main__":
    main()
