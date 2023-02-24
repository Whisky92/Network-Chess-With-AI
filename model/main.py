#!/usr/bin/env python3
from model.game import Game

def main():
    game = Game()
    board = game.get_board()
    table = game.get_board_table()
    typer = game.get_board_table()[0][1].get_piece().get_piece_type()
    print(typer)
    d = game.get_board_table()[0][0].get_piece().get_direction()
    print(d)








if __name__ == "__main__":
    main()
