from player import Player
from colors import Color
from piece import Piece
from piece_type import PieceType


class Game:

    def __init__(self):
        self._white_player = Player(Color.WHITE)
        self._black_player = Player(Color.BLACK)
        self._current_player = self._white_player
        self._board = None
        self._last_step = None
        self.fill_board()

    def get_board(self):
        return self._board

    def set_white_player_direction(self, direction):
        self._white_player.set_direction(direction)

    def set_black_player_direction(self, direction):
        self._black_player.set_direction(direction)

    def get_current_player(self):
        return self._current_player

    def fill_board(self):
        self._board = [[Piece(0, 0, PieceType.ROOK, -1), Piece(0, 1, PieceType.KNIGHT, -1),
                        Piece(0, 2, PieceType.BISHOP, -1), Piece(0, 3, PieceType.QUEEN, -1),
                        Piece(0, 4, PieceType.KING, -1), Piece(0, 5, PieceType.BISHOP, -1),
                        Piece(0, 6, PieceType.KNIGHT, -1), Piece(0, 7, PieceType.ROOK, -1)],
                       [Piece(7, 0, PieceType.ROOK, 1), Piece(7, 1, PieceType.KNIGHT, 1),
                        Piece(7, 2, PieceType.BISHOP, 1), Piece(7, 3, PieceType.QUEEN, 1),
                        Piece(7, 4, PieceType.KING, 1), Piece(7, 5, PieceType.BISHOP, 1),
                        Piece(7, 6, PieceType.KNIGHT, 1), Piece(7, 7, PieceType.ROOK, 1)]]

        self._board.insert(1, [Piece(1, 0, PieceType.PAWN, -1), Piece(1, 1, PieceType.PAWN, -1),
                               Piece(1, 2, PieceType.PAWN, -1), Piece(1, 3, PieceType.PAWN, -1),
                               Piece(1, 4, PieceType.PAWN, -1), Piece(1, 5, PieceType.PAWN, -1),
                               Piece(1, 6, PieceType.PAWN, -1), Piece(1, 7, PieceType.PAWN, -1)])

        for i in range(2, 6):
            self._board.insert(i, [Piece(i, 0, PieceType.NO_TYPE, 0), Piece(i, 1, PieceType.NO_TYPE, 0),
                                   Piece(i, 2, PieceType.NO_TYPE, 0), Piece(i, 3, PieceType.NO_TYPE, 0),
                                   Piece(i, 4, PieceType.NO_TYPE, 0), Piece(i, 5, PieceType.NO_TYPE, 0),
                                   Piece(i, 6, PieceType.NO_TYPE, 0), Piece(i, 7, PieceType.NO_TYPE, 0)])

        self._board.insert(6, [Piece(6, 0, PieceType.PAWN, 1), Piece(6, 1, PieceType.PAWN, 1),
                               Piece(6, 2, PieceType.PAWN, 1), Piece(6, 3, PieceType.PAWN, 1),
                               Piece(6, 4, PieceType.PAWN, 1), Piece(6, 5, PieceType.PAWN, 1),
                               Piece(6, 6, PieceType.PAWN, 1), Piece(6, 7, PieceType.PAWN, 1)])

    def get_possible_steps(self, piece):
        possible_cells = []
        x = piece.get_piece_x()
        y = piece.get_piece_y()
        p_type = piece.get_piece_type()
        if p_type == PieceType.KNIGHT:
            possible_cells.extend(self.check_knight_steps(piece, x, y))
        elif p_type == PieceType.KING:
            possible_cells.extend(self.check_king_steps(piece, x, y))
        elif p_type == PieceType.ROOK:
            possible_cells.extend(self.check_rook_steps(piece))
        elif p_type == PieceType.PAWN:
            if piece.get_direction() == 1:
                if piece.get_is_first_step():
                    possible_cells.extend([x+2, y])
                possible_cells.append([x+1, y])
            elif piece.get_direction() == -1:
                if piece.get_is_first_step():
                    possible_cells.append([x-2, y])
                possible_cells.append([x+2, y])
        elif p_type == PieceType.BISHOP:
            possible_cells.extend(self.check_bishop_steps(piece))
        elif p_type == PieceType.QUEEN:
            possible_cells.extend(self.check_bishop_steps(piece))
            possible_cells.extend(self.__check_adjacent_cells(piece, piece.get_piece_x(), piece.get_piece_y()))
        return possible_cells

    def check_bishop_steps(self, piece):
        possible_steps = []
        possible_steps.extend(self.check_bishop_steps_diagonally(piece, 1, 1))
        possible_steps.extend(self.check_bishop_steps_diagonally(piece, 1, -1))
        possible_steps.extend(self.check_bishop_steps_diagonally(piece, -1, 1))
        possible_steps.extend(self.check_bishop_steps_diagonally(piece, -1, -1))
        return possible_steps

    def check_rook_steps(self, piece):
        possible_steps = []
        possible_steps.extend(self.check_rook_steps_vertical(piece, piece.get_piece_x(), 8, 1))
        possible_steps.extend(self.check_rook_steps_vertical(piece, piece.get_piece_x(), -1, -1))
        possible_steps.extend(self.check_rook_steps_horizontal(piece, piece.get_piece_y(), 8, 1))
        possible_steps.extend(self.check_rook_steps_horizontal(piece, piece.get_piece_y(), -1, -1))
        return possible_steps

    def check_knight_steps(self, piece, x, y):
        possible_steps = []
        possible_steps.extend(self.__check_cell(piece, x - 3, y + 1))
        possible_steps.extend(self.__check_cell(piece, x - 3, y - 1))
        possible_steps.extend(self.__check_cell(piece, x + 3, y + 1))
        possible_steps.extend(self.__check_cell(piece, x + 3, y - 1))
        possible_steps.extend(self.__check_cell(piece, x + 1, y + 3))
        possible_steps.extend(self.__check_cell(piece, x + 1, y - 3))
        possible_steps.extend(self.__check_cell(piece, x - 1, y + 3))
        possible_steps.extend(self.__check_cell(piece, x - 1, y - 3))
        return possible_steps

    def check_king_steps(self, piece, x, y):
        possible_steps = []
        possible_steps.extend(self.__check_cell(piece, x + 1, y + 1))
        possible_steps.extend(self.__check_cell(piece, x + 1, y - 1))
        possible_steps.extend(self.__check_cell(piece, x - 1, y + 1))
        possible_steps.extend(self.__check_cell(piece, x - 1, y - 1))
        possible_steps.extend(self.__check_adjacent_cells(piece, x, y))
        return possible_steps

    def check_rook_steps_vertical(self, piece, begin, end, step_distance):
        possible_steps = []
        for i in range(begin, end, step_distance):
            current_piece = self._board[i][piece.get_piece_y()]
            if current_piece.get_direction() != 0 and current_piece.get_direction != piece.get_direction():
                possible_steps.append(current_piece)
                break
            elif current_piece.get_direction() != 0:
                break
            else:
                possible_steps.append(current_piece)
        return possible_steps

    def check_rook_steps_horizontal(self, piece, begin, end, step_distance):
        possible_steps = []
        for i in range(begin, end, step_distance):
            current_piece = self._board[piece.get_piece_x()][i]
            if current_piece.get_direction() != 0 and current_piece.get_direction != piece.get_direction():
                possible_steps.append(current_piece)
                break
            elif current_piece.get_direction() != 0:
                break
            else:
                possible_steps.append(current_piece)
        return possible_steps

    def check_bishop_steps_diagonally(self, piece, x_incr_val, y_incr_val):
        possible_steps = []
        current_x = piece.get_piece_x() + x_incr_val
        current_y = piece.get_piece_y() + y_incr_val
        while current_x < 8 and current_y < 8:
            current_piece = self._board[current_x][current_y]
            if current_piece.get_direction() != 0 and current_piece.get_direction != piece.get_direction():
                possible_steps.append(current_piece)
                break
            elif current_piece.get_direction() != 0:
                break
            else:
                possible_steps.append(current_piece)
        current_x += x_incr_val
        current_y += y_incr_val
        return possible_steps

    def __check_adjacent_cells(self, piece, x, y):
        possible_steps = []
        possible_steps.extend(self.__check_cell(piece, x + 1, y))
        possible_steps.extend(self.__check_cell(piece, x - 1, y))
        possible_steps.extend(self.__check_cell(piece, x, y + 1))
        possible_steps.extend(self.__check_cell(piece, x, y - 1))
        return possible_steps

    def check_pawn_steps(self, piece, x, y):
        possible_steps = []
        possible_steps.extend(self.is_correct_pawn_step(piece, x+1, y))
        possible_steps.extend(self.is_correct_pawn_step(piece, x + 2, y))
        possible_steps.extend(self.is_correct_pawn_step(piece, x + 1, y+1))
        possible_steps.extend(self.is_correct_pawn_step(piece, x + 1, y-1))
        possible_steps.extend(self.is_en_passant(piece))
        return possible_steps

    def is_correct_pawn_step(self, piece, x, y):
        possible_steps = []
        if -1 < x < 8 and -1 < y < 8:
            current = self._board[x][y]
            if current.get_piece_y() != piece.get_piece_y():
                if current.get_direction() != 0 and current.get_direction != piece.get_direction():
                    possible_steps.append(current)
            else:
                if current.get_direction == 0:
                    if current.get_piece_y() == piece.get_piece_y() + 1 * piece.get_direction():
                        possible_steps.append(current)
                    else:
                        if self._board[piece.get_piece_x()+1][piece.get_piece_y()].get_direction() == 0 \
                                and piece.get_is_first_step():
                            possible_steps.append(current)

        return possible_steps

    def is_en_passant(self, piece):
        possible_steps = []
        if self._last_step is not None:
            if self._last_step.get_direction() != piece.get_direction():
                if self._last_step.get_piece_x() == piece.get_piece_x() \
                        and self._last_step.get_piece_y() == (piece.get_piece_y() + 1 or piece.get_piece_y - 1):
                    possible_steps.append(self._last_step)
        return possible_steps


    def __check_cell(self, piece, x, y):
        steps = []
        if -1 < x < 8 and -1 < y < 8:
            current = self._board[x][y]
            if current.get_direction() != piece.get_direction():
                steps.append(current)
        return steps

    def print_coords(self, piece):
        print(piece.get_piece_x(), piece.get_piece_y())