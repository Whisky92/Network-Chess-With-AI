#!/usr/bin/env python3
from game import Game

def main():
    game = Game()
    game.set_black_player_direction(-1)
    game.set_white_player_direction(1)
    game.print_table()


if __name__ == "__main__":
    main()
