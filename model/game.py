from player import Player
from colors import Color
from board import Board
from cell import Cell
from piece_type import PieceType
from piece import Piece

class Game:

    def __init__(self, white_direction, black_direction):
        self._white_player = Player(Color.WHITE, white_direction)
        self._black_player = Player(Color.BLACK, black_direction)
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


    def __add_to_player_pieces(self):
        for i in range(0, 8):
            for j in range(0, 8):
                this_piece = self._board.get_board()[i][j].get_piece()
                if this_piece.get_direction() == self._white_player.get_direction():
                    self._white_player.add_to_pieces_on_board(this_piece)
                elif this_piece.get_direction() == self._black_player.get_direction():
                    self._black_player.add_to_pieces_on_board(this_piece)

    def move_piece(self, cell_to_move_from: Cell, target_cell: Cell):
        piece_to_move = cell_to_move_from.get_piece()
        x_target_coord = target_cell.get_piece().get_piece_x()
        y_target_coord = target_cell.get_piece().get_piece_y()
        check_list = self.check_king_steps(cell_to_move_from) \
            if cell_to_move_from.get_piece().get_piece_type() == PieceType.KING \
            else piece_to_move.get_possible_steps(self._board.get_board(), self._last_step)
        if target_cell in check_list:
            if target_cell in self._castling_step:
                index = self.get_index_of_item(self._castling_step, target_cell)
                rook_y = self._rook_target[index].get_piece().get_piece_y()
                rook_direction = self._rook_target[index].get_piece().get_direction()
                self._rook_target[index].set_piece(self._castling_rook[index].get_piece())
                self._rook_target[index].get_piece().set_piece_y(rook_y)
                self._rook_target[index].get_piece().set_direction(rook_direction)
                self._castling_rook[index].set_piece(Piece(piece_to_move.get_piece_x(), piece_to_move.get_piece_y(),
                                                    PieceType.NO_TYPE, 0))
                self._castling_rook = []
                self._castling_step = []
                self._rook_target = []
            elif target_cell.get_piece().get_direction() != 0:
                target_cell.get_piece().set_piece_x(-1)
                target_cell.get_piece().set_piece_y(-1)
                current_player = self.__get_player_by_direction(target_cell.get_piece().get_direction())
                current_player.add_to_captured_pieces(target_cell.get_piece())
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
                current_player.add_to_captured_pieces(cell_to_capture_from.get_piece())
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

    def printing(self):
        print(len(self._castling_step))
        self._board.print_piece_data(self._castling_step[0])
        self._board.print_piece_data(self._castling_rook[0])
        self._board.print_piece_data(self._rook_target[0])
    def evolve_pawn(self, cell, p_type):
        piece = cell.get_piece()
        if piece.get_is_able_to_evolve():
            piece.set_to_not_able_to_evolve()
            piece.set_piece_type(p_type)
    def is_king_targeted(self, player):
        enemy_player = self._black_player if player == self._white_player else self._white_player
        king_cell = self.get_king_cell(player)
        return self.is_cell_targeted(king_cell, enemy_player)
    def is_king_cells_targeted(self, player):
        king_cell = self.get_king_cell(player)
        non_targeted_cells = []
        enemy_player = self._black_player if player == self._white_player else self._white_player
        for i in king_cell.get_piece().get_possible_steps(self._board.get_board(), self._last_step):
            if not self.is_cell_targeted(i, enemy_player):
                non_targeted_cells.append(i)
        return non_targeted_cells
    def is_cell_targeted(self, cell, enemy_player):
        player = self._black_player if enemy_player == self._white_player else self._white_player
        changed = False
        for i in enemy_player.get_pieces_on_board():
            if i.get_piece_type() == PieceType.PAWN and cell.get_piece().get_direction() == 0:
                changed = True
                cell.get_piece().set_direction(player.get_direction())
            result = cell in i.get_possible_steps(self._board.get_board(), self._last_step)
            if changed:
                cell.get_piece().set_direction(0)
            if result:
                return True
        return False
    def print_king(self, x, y):
        piece = self.get_board_table()[x][y]
        for i in self.check_king_steps(piece):
            print(i.get_piece().get_piece_x(), i.get_piece().get_piece_y(),
                  "type:", i.get_piece().get_piece_type(), i.get_piece().get_direction())

    def get_king_cell(self, player):
        for i in player.get_pieces_on_board():
            if i.get_piece_type() == PieceType.KING:
                return self._board.get_board()[i.get_piece_x()][i.get_piece_y()]

    def print_pieces(self):
        for i in self._black_player.get_pieces_on_board():
            print(i)

    def get_possible_steps(self, x, y):
        piece = self.get_board_table()[x][y].get_piece()
        return piece.get_possible_steps(self._board.get_board(), self._last_step)

    def print_possible_board(self, x, y):
        cell = self._board.get_board()[x][y]
        lst = cell.get_piece().get_possible_steps(self._board.get_board(), self._last_step)
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
        for i in piece.get_possible_steps(self._board.get_board(), self._last_step):
            print(i.get_piece().get_piece_x(), i.get_piece().get_piece_y(),
                  "type:", i.get_piece().get_piece_type(), i.get_piece().get_direction())

    def check_king_steps(self, cell):
        possible_cells = []
        player = self.get_player_by_direction(cell.get_piece().get_direction())
        possible_cells.extend(self.is_king_cells_targeted(player))
        possible_cells.extend(self.add_castling_steps_to_possible_steps(cell, cell.get_piece().get_piece_x(),
                                                                        cell.get_piece().get_piece_y() + 2))
        possible_cells.extend(self.add_castling_steps_to_possible_steps(cell, cell.get_piece().get_piece_x(),
                                                                        cell.get_piece().get_piece_y() - 2))
        return possible_cells

    def add_castling_steps_to_possible_steps(self, cell, x, y):
        possible_steps = []
        board = self.get_board().get_board()
        target_piece = board[x][y]
        if 7 - y < y - 0:
            castling = self.__check_castling_on_one_side(cell, target_piece, 7)
            if len(castling) != 0:
                if board[x][5] not in self._rook_target:
                    self._rook_target.append(board[x][5])
                possible_steps.extend(castling)
        else:
            castling = self.__check_castling_on_one_side(cell, target_piece, 0)
            if len(castling) != 0:
                if board[x][3] not in self._rook_target:
                    self._rook_target.append(board[x][3])
                possible_steps.extend(castling)
        return possible_steps


    def __check_castling_on_one_side(self, cell, target_piece, rook_y):
        possible_steps = []
        game_board = self.get_board()
        cell_y = cell.get_piece().get_piece_y()
        target_x = target_piece.get_piece().get_piece_x()
        target_y = target_piece.get_piece().get_piece_y()
        rook_cell = self.get_board().get_board()[target_x][rook_y]
        min_y = None
        max_y = None
        if cell_y > target_y:
            min_y = target_y
            max_y = cell_y
        else:
            min_y = cell_y
            max_y = target_y
        if rook_cell.get_piece().get_is_first_step() and cell.get_piece().get_is_first_step():
            enemy_player = self._black_player if cell.get_piece().get_direction() == \
                                                 self._white_player.get_direction() else self._white_player
            for i in range(min_y + 1, max_y):
                current_cell = game_board.get_board()[target_x][i]
                if current_cell.get_piece().get_piece_type() != PieceType.NO_TYPE:
                    return possible_steps
            for i in range(min_y, max_y + 1):
                current_cell = game_board.get_board()[target_x][i]
                if self.is_cell_targeted(current_cell, enemy_player):
                    return possible_steps
            if target_piece not in self._castling_step:
                self._castling_rook.append(rook_cell)
                self._castling_step.append(target_piece)
            possible_steps.append(target_piece)
        return possible_steps

    def get_index_of_item(self, lst, item):
        for i in range(0, len(lst)):
            if lst[i] == item:
                return i
        return -1