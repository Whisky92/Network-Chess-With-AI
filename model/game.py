from model.player import Player
from model.colors import Color
from model.board import Board
from model.cell import Cell
from model.piece_type import PieceType
from model.piece import Piece
from model.king_step_checker import KingStepChecker
import copy


class Game:

    def __init__(self, *args):

        self._white_player = Player(Color.WHITE, 1)
        self._black_player = Player(Color.BLACK, -1)
        self._current_player = self._white_player

        if len(args) == 0:
            self._board = Board()
        else:
            self._board = Board(args[0])

        self._last_step = None

        self.__add_to_player_pieces()

        self._castling_step = []
        self._castling_rook = []
        self._rook_target = []
        self._self_checkmate = False

    def change_current_player(self):
        """
        Changes the current player from white to black / black to white
        """
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

    def get_self_checkmate(self):
        return self._self_checkmate

    def set_self_checkmate(self):
        self._self_checkmate = False

    def filter_wrong_moves(self, x, y):
        """
        Selects the legal moves from the moves of piece indexed by the given coordinates,
        to prevent the current player's own king getting targeted because of wrong step.

        :param x: the x coordinate of the cell to be checked
        :param y: the y coordinate of the cell to be checked

        :return: the list of legal moves
        """
        piece = self.get_board_table()[x][y].get_piece()
        possible_moves = []

        for i in self.get_possible_steps(x, y):
            if not self.__cause_king_to_be_targeted(piece, i):
                possible_moves.append(i)

        return possible_moves

    def get_possible_steps(self, x, y):
        """
        Returns the possible moves of the piece indexed by the given coordinates

        :param x: the x coordinate of the cell to be checked
        :param y: the y coordinate of the cell to be checked

        :return: the list of possible moves
        """
        cell = self.get_board_table()[x][y]
        return cell.get_piece().get_possible_steps(self._board.get_board(), self._last_step, self._white_player,
                                                   self._black_player, self._castling_step, self._castling_rook,
                                                   self._rook_target)

    def move_piece(self, cell_to_move_from: Cell, target_cell: Cell):
        """
        Moves the piece from start cell to target cell, checks for stalemate and changes current player

        :param cell_to_move_from: the cell to move the piece from
        :param target_cell: the cell to move to
        """

        self.move(cell_to_move_from, target_cell)

        if self.is_stalemate():
            self._current_player.set_can_stalemate(True)

        self.change_current_player()

    def move(self, cell_to_move_from: Cell, target_cell: Cell):
        """
        Moves the piece to the target cell from the start cell

        :param cell_to_move_from: the cell to move the piece from
        :param target_cell: the cell to move to
        """

        piece_to_move = cell_to_move_from.get_piece()
        x_target_coord = target_cell.get_piece().get_piece_x()
        y_target_coord = target_cell.get_piece().get_piece_y()

        if target_cell in self._castling_step:

            self.move_piece_in_case_of_castling(x_target_coord, target_cell)

        elif target_cell.get_piece().get_direction() != 0:

            self.move_piece_if_target_cell_is_occupied(target_cell)

        elif piece_to_move.get_en_passant_step() is not None \
                and target_cell == piece_to_move.get_en_passant_step():
            self.move_piece_in_case_of_en_passant(piece_to_move, target_cell)

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

    def move_piece_in_case_of_castling(self, x_target_coord, target_cell):
        """
        Moves the piece in case of castling

        :param x_target_coord: the x coordinate of the target cell
        :param target_cell: the cell to move to
        """

        index = Game.get_index_of_item(self._castling_step, target_cell)

        rook_y = self._rook_target[index].get_piece().get_piece_y()
        rook_old_y = self._castling_rook[0].get_piece().get_piece_y()

        self._castling_rook[0].get_piece().set_piece_y(rook_y)
        self._rook_target[0].set_piece(self._castling_rook[0].get_piece())
        self._castling_rook[0].set_piece(Piece(x_target_coord, rook_old_y, PieceType.NO_TYPE, 0))

    def move_piece_if_target_cell_is_occupied(self, target_cell):
        """
        Moves the piece if the target cell is occupied

        :param target_cell: the cell to move to
        """
        target_cell.get_piece().set_piece_x(-1)
        target_cell.get_piece().set_piece_y(-1)

        current_player = KingStepChecker.get_player_by_direction(target_cell.get_piece().get_direction(),
                                                                 self._white_player, self._black_player)

        current_player.remove_from_pieces_on_board(target_cell.get_piece())

    def move_piece_in_case_of_en_passant(self, piece_to_move, target_cell):
        """
        Moves the piece in case of en passant

        :param piece_to_move: the piece to move
        :param target_cell: the cell to move to
        """
        piece_to_move.delete_last_en_passant_step()

        target_y = target_cell.get_piece().get_piece_y()
        target_x = target_cell.get_piece().get_piece_x() + 1 * piece_to_move.get_direction()
        cell_to_capture_from = self._board.get_board()[target_x][target_y]
        target_direction = cell_to_capture_from.get_piece().get_direction()

        cell_to_capture_from.get_piece().set_piece_x(-1)
        cell_to_capture_from.get_piece().set_piece_y(-1)

        current_player = KingStepChecker.get_player_by_direction(target_direction,
                                                                 self._white_player,
                                                                 self._black_player)

        current_player.remove_from_pieces_on_board(cell_to_capture_from.get_piece())
        cell_to_capture_from.set_piece(Piece(target_x, target_y, PieceType.NO_TYPE, 0))

    def __cause_king_to_be_targeted(self, piece, target):
        """
        Returns whether the current step would cause the king to be targeted

        :param piece: the piece to step with
        :param target: the target of the step

        :return: the logical value whether the step would cause the king to be targeted
        """

        piece_x = piece.get_piece_x()
        piece_y = piece.get_piece_y()

        target_x = target.get_piece().get_piece_x()
        target_y = target.get_piece().get_piece_y()

        test_game = copy.deepcopy(self)

        cell_to_move_from = test_game.get_board_table()[piece_x][piece_y]
        target_cell = test_game.get_board_table()[target_x][target_y]

        test_game.move(cell_to_move_from, target_cell)

        if test_game.is_king_targeted(test_game.get_current_player()):
            return True
        return False

    def steps_if_king_is_targeted(self):
        """
        Returns a list of tuples in which there are the possible pieces and the corresponding
        legal moves that would save the king from check

        :return: the list of tuples with the pieces and the corresponding legal moves
        """

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

    def is_king_targeted(self, player):
        """
        Returns whether the given player's king is targeted

        :param player: the player whose king is to be checked

        :return: the logical value whether the player's king is checked
        """
        enemy_player = self._black_player if player == self._white_player else self._white_player
        king_cell = KingStepChecker.get_king_cell(self.get_board_table(), player)

        return KingStepChecker.is_cell_targeted(self.get_board_table(), king_cell, enemy_player, self._white_player,
                                                self._black_player, self._last_step, self._castling_step,
                                                self._castling_rook, self._rook_target)

    def is_stalemate(self):
        """
        Returns whether the current state of the game is a stalemate

        :return: logical value whether the current state of the game is a stalemate
        """

        if self.is_king_targeted(self.get_current_player()):
            return False

        for i in self._current_player.get_pieces_on_board():

            steps = self.get_possible_steps(i.get_piece_x(), i.get_piece_y())

            if i.get_piece_type() != PieceType.KING:
                if len(steps) != 0 and not self.__cause_king_to_be_targeted(i, steps[0]):
                    return False
            else:
                if len(steps) != 0:
                    return False

        return True

    def contains_start_cell(self, lst, target):
        """
        Returns the correct tuple if the list contains the target,
        else returns None

        :param lst: the list of possible tuples
        :param target: the element to check

        :return: the element's tuple if it can be found in the list, else None
        """

        for i in lst:
            if i[0] == target:
                return i
        return None

    def promote_pawn(self, cell, p_type):
        """
        Promotes a pawn to the selected piece type

        :param cell: the cell of the pawn
        :param p_type: the type to promote to
        """
        piece = cell.get_piece()
        piece.set_piece_type(p_type)

    @staticmethod
    def get_index_of_item(lst, item):
        """
        Returns the index of the given item

        :param lst: the list in which the item index must be determined
        :param item: the item to be checked

        :return: the index of the item
        """
        for i in range(0, len(lst)):
            if lst[i] == item:
                return i
        return -1

    def __add_to_player_pieces(self):
        """
        Adds the pieces on board to the corresponding player's owned pieces list
        """
        for i in range(0, 8):
            for j in range(0, 8):
                this_piece = self._board.get_board()[i][j].get_piece()
                if this_piece.get_direction() == self._white_player.get_direction():
                    self._white_player.add_to_pieces_on_board(this_piece)
                elif this_piece.get_direction() == self._black_player.get_direction():
                    self._black_player.add_to_pieces_on_board(this_piece)
