#!/usr/bin/env python3
from model.game import Game

def main():
    game = Game()
    board = game.get_board()
    table = game.get_board_table()
    board.print_board()
    game.print_possible_steps(0, 4)
    game.get_possible_steps(7, 4)
    print()
    print(game.get_rook_target()[0].get_piece().get_piece_x(), game.get_rook_target()[0].get_piece().get_piece_y())
    print(game.get_castling_rook()[0].get_piece().get_piece_x(), game.get_castling_rook()[0].get_piece().get_piece_y())
    print(game.get_castling_step()[0].get_piece().get_piece_x(), game.get_castling_step()[0].get_piece().get_piece_y())
    print(".......")
    game.move_piece(game.get_board_table()[7][4], game.get_board_table()[7][2])
    board.print_board()













if __name__ == "__main__":
    main()
