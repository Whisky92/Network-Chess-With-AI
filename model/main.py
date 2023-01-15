#!/usr/bin/env python3
from game import Game

def main():
    game = Game(-1, 1)
    board = game.get_board()
    table = game.get_board_table()
    game.move_piece(table[1][0], table[3][0])
    print(game.get_last_step())
    print(table[3][0])
    board.print_board()
    game.print_possible_steps(3, 1)
    game.move_piece(table[3][1], table[2][0])
    print(game.get_last_step())
    print(game.get_black_player().get_direction())
    print(game.get_white_player().get_direction())

    board.print_board()
    print()
    game.print_possible_steps(2, 0)
    print(game.get_white_player().get_captured_pieces()[0], "adasdasdas")
    board.print_board()
    game.move_piece(table[2][0], table[1][1])
    print()
    board.print_board()
    print()
    print(game.get_white_player().get_captured_pieces()[1], "adasdasdas")
    print(len(game.get_white_player().get_pieces_on_board()))
    print(len(game.get_black_player().get_pieces_on_board()))



if __name__ == "__main__":
    main()
