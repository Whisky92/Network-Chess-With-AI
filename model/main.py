#!/usr/bin/env python3
from model.game import Game

def main():
    game = Game()
    board = game.get_board()
    table = game.get_board_table()
    board.print_board()
    game.print_possible_steps(0, 4)











if __name__ == "__main__":
    main()
