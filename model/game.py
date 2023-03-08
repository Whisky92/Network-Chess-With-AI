from model.player import Player
from model.colors import Color
from model.board import Board
from model.cell import Cell
from model.piece_type import PieceType
from model.piece import Piece
from model.king_step_checker import KingStepChecker
import copy


class Game:

    def __init__(self):
        self._white_player = Player(Color.WHITE, 1)
        self._black_player = Player(Color.BLACK, -1)
        self._current_player = self._white_player
        self._board = Board()
        self._last_step = None
        self.__add_to_player_pieces()
        self._castling_step = []
        self._castling_rook = []
        self._rook_target = []

    def change_current_player(self):
        if self._current_player == self._white_player:
            self._current_player = self._black_player
        else:
            self._current_player = self._white_player

    def get_white_player(self):
        return self._white_player

    def get_black_player(self):
        return self._black_player

    def get_current_player(self):
        return self._current_player

    def get_board(self):
        return self._board

    def get_board_table(self):
        return self._board.get_board()

    def get_last_step(self):
        return self._last_step

    def get_castling_step(self):
        return self._castling_step

    def get_castling_rook(self):
        return self._castling_rook

    def get_rook_target(self):
        return self._rook_target

    def __add_to_player_pieces(self):
        for i in range(0, 8):
            for j in range(0, 8):
                this_piece = self._board.get_board()[i][j].get_piece()
                if this_piece.get_direction() == self._white_player.get_direction():
                    self._white_player.add_to_pieces_on_board(this_piece)
                elif this_piece.get_direction() == self._black_player.get_direction():
                    self._black_player.add_to_pieces_on_board(this_piece)

    def move_piece(self, cell_to_move_from: Cell, target_cell: Cell):

        self.move(cell_to_move_from, target_cell)

        if self.__is_player_king_cells_targeted(self._white_player) and not self.is_king_targeted(self._white_player)\
                and len(self._white_player.get_pieces_on_board()) == 1:
            self._white_player.set_can_stalemate(True)

        if self.__is_player_king_cells_targeted(self._black_player) and not self.is_king_targeted(self._black_player)\
                and len(self._black_player.get_pieces_on_board()) == 1:
            self._black_player.set_can_stalemate(True)

        self.change_current_player()

    def printing(self):
        print(len(self._castling_step))
        self._board.print_piece_data(self._castling_step[0])
        self._board.print_piece_data(self._castling_rook[0])
        self._board.print_piece_data(self._rook_target[0])

    def promote_pawn(self, cell, p_type):
        piece = cell.get_piece()
        piece.set_piece_type(p_type)

    def is_king_targeted(self, player):
        enemy_player = self._black_player if player == self._white_player else self._white_player
        king_cell = KingStepChecker.get_king_cell(self.get_board_table(), player)
        return KingStepChecker.is_cell_targeted(self.get_board_table(), king_cell, enemy_player, self._white_player,
                                                self._black_player, self._last_step, self._castling_step,
                                                self._castling_rook, self._rook_target)

    def print_pieces(self):
        for i in self._black_player.get_pieces_on_board():
            print(i)

    def get_possible_steps(self, x, y):
        cell = self.get_board_table()[x][y]
        return cell.get_piece().get_possible_steps(self._board.get_board(), self._last_step, self._white_player,
                           self._black_player, self._castling_step, self._castling_rook,
                           self._rook_target)

    def print_possible_board(self, x, y):
        cell = self._board.get_board()[x][y]
        player = self.get_player_by_direction(cell.get_piece().get_direction())
        lst = KingStepChecker.is_king_cells_targeted(self.get_board_table(), player, self._white_player,
                                                     self._black_player, self._last_step, self._castling_step,
                                                     self._castling_rook, self._rook_target)
        for i in range(0, 8):
            for j in range(0, 8):
                if self._board.get_board()[i][j] == cell:
                    print("X", end=" ")
                elif self._board.get_board()[i][j] in lst:
                    print("x", end=" ")
                else:
                    print("-", end=" ")
            print()

    def get_player_by_direction(self, direction):
        if self._white_player.get_direction() == direction:
            return self._white_player
        return self._black_player

    def __get_player_by_direction(self, direction):
        if self._white_player.get_direction() == direction:
            return self._white_player
        return self._black_player

    def print_possible_steps(self, x, y):
        piece = self.get_board_table()[x][y].get_piece()
        for i in piece.get_possible_steps(self._board.get_board(), self._last_step, self._white_player,
                                          self._black_player, self._castling_step, self._castling_rook, self._rook_target):
            print(i.get_piece().get_piece_x(), i.get_piece().get_piece_y(),
                  "type:", i.get_piece().get_piece_type(), i.get_piece().get_direction())

    def steps_if_king_is_targeted(self):

        steps = []

        for i in self._current_player.get_pieces_on_board():

            piece_x = i.get_piece_x()
            piece_y = i.get_piece_y()

            start_c = None
            dest_c = []

            for j in self.get_possible_steps(piece_x, piece_y):

                target_x = j.get_piece().get_piece_x()
                target_y = j.get_piece().get_piece_y()

                test_game = copy.deepcopy(self)

                piece_to_move = test_game.get_board_table()[piece_x][piece_y]
                target_piece = test_game.get_board_table()[target_x][target_y]

                test_game.move(piece_to_move, target_piece)

                if not test_game.is_king_targeted(test_game.get_current_player()):

                    start_c = self.get_board_table()[piece_x][piece_y]
                    dest_c.append(self.get_board_table()[target_x][target_y])

            if start_c is not None:
                tup = (start_c, dest_c)
                steps.append(tup)

        return steps

    def move(self, cell_to_move_from: Cell, target_cell: Cell):

        piece_to_move = cell_to_move_from.get_piece()
        x_target_coord = target_cell.get_piece().get_piece_x()
        y_target_coord = target_cell.get_piece().get_piece_y()

        if target_cell in self._castling_step:
            index = Game.get_index_of_item(self._castling_step, target_cell)
            rook_y = self._rook_target[index].get_piece().get_piece_y()
            rook_old_y = self._castling_rook[0].get_piece().get_piece_y()
            self._castling_rook[0].get_piece().set_piece_y(rook_y)
            self._rook_target[0].set_piece(self._castling_rook[0].get_piece())
            self._castling_rook[0].set_piece(Piece(x_target_coord, rook_old_y, PieceType.NO_TYPE, 0))

        elif target_cell.get_piece().get_direction() != 0:
            target_cell.get_piece().set_piece_x(-1)
            target_cell.get_piece().set_piece_y(-1)
            current_player = self.__get_player_by_direction(target_cell.get_piece().get_direction())
            current_player.remove_from_pieces_on_board(target_cell.get_piece())
        elif piece_to_move.get_en_passant_step() is not None \
                and target_cell == piece_to_move.get_en_passant_step():
            piece_to_move.delete_last_en_passant_step()
            target_y = target_cell.get_piece().get_piece_y()
            target_x = target_cell.get_piece().get_piece_x() + 1 * piece_to_move.get_direction()
            cell_to_capture_from = self._board.get_board()[target_x][target_y]
            target_direction = cell_to_capture_from.get_piece().get_direction()
            cell_to_capture_from.get_piece().set_piece_x(-1)
            cell_to_capture_from.get_piece().set_piece_y(-1)
            current_player = self.__get_player_by_direction(target_direction)
            current_player.remove_from_pieces_on_board(cell_to_capture_from.get_piece())
            cell_to_capture_from.set_piece(Piece(target_x, target_y, PieceType.NO_TYPE, 0))
        if (piece_to_move.get_piece_x() == target_cell.get_piece().get_piece_x() - 2
            or piece_to_move.get_piece_x() == target_cell.get_piece().get_piece_x() + 2) \
                and piece_to_move.get_piece_type() == PieceType.PAWN:
            self._last_step = target_cell
        elif self._last_step is not None:
            self._last_step = None
        cell_to_move_from.set_piece(Piece(piece_to_move.get_piece_x(), piece_to_move.get_piece_y(),
                                          PieceType.NO_TYPE, 0))
        piece_to_move.set_piece_x(x_target_coord)
        piece_to_move.set_piece_y(y_target_coord)
        piece_to_move.change_to_not_first_step()
        target_cell.set_piece(piece_to_move)

    def contains_cell(self, lst, target):
        for i in lst:
            if i[0] == target:
                return True
        return False

    def print_king_targeted_steps(self):

        for i in self.steps_if_king_is_targeted():
            print("Start Cell:")
            self._board.print_piece_data(i[0])
            print("Targets:")
            for j in i[1]:
                self._board.print_piece_data(j)

    @staticmethod
    def get_index_of_item(lst, item):
        for i in range(0, len(lst)):
            if lst[i] == item:
                return i
        return -1

    def __is_player_king_cells_targeted(self, player):
        return len(KingStepChecker.is_king_cells_targeted
                   (self.get_board_table(), player, self._white_player,
                    self._black_player, self._last_step, self._castling_step,
                    self._castling_rook, self._rook_target)) == 0


