#!/usr/bin/env python3
from model.game import Game
import copy

def main():
    game = Game()
    board = game.get_board()
    table = game.get_board_table()
    print(game.is_stalemate())













if __name__ == "__main__":
    main()
