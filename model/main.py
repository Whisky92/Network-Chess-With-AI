#!/usr/bin/env python3
from game import Game

def main():
    game = Game()
    board = game.get_board()
    table = game.get_board_table()
    game.move_piece(table[1][0], table[3][0])
    print(game.get_last_step())
    print(table[3][0])
    board.print_board()
    game.print_possible_steps(3, 1)
    game.move_piece(table[3][1], table[2][0])
    print(game.get_last_step())
    print(game.get_player_by_direction(table[2][0].get_piece().get_direction()).get_captured_pieces()[0].get_piece_x())
    board.print_board()
    print()
    game.print_possible_steps(2, 0)



if __name__ == "__main__":
    main()
