#!/usr/bin/env python3
from game import Game

def main():
    game = Game(-1, 1)
    board = game.get_board()
    table = game.get_board_table()
    game.print_possible_board(3, 3)







if __name__ == "__main__":
    main()
