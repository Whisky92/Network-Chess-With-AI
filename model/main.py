#!/usr/bin/env python3
from game import Game

def main():
    game = Game(-1, 1)
    board = game.get_board()
    table = game.get_board_table()
    board.print_board()
    game.print_king(0, 4)
    game.move_piece(table[0][4], table[0][2])
    print()
    board.print_board()
    game.print_possible_steps(0, 2)
    game.is_king_cells_targeted(game.get_white_player())
    print(table[0][1].get_piece().get_direction())







if __name__ == "__main__":
    main()
