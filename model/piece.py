from piece_type import PieceType
from board import Board


class Piece:
    def __init__(self, x, y, p_type, direction):
        self._x = x
        self._y = y
        self._p_type = p_type
        self._direction = direction
        self._is_first_step = True
        self.board = Board.get_instance()

    def get_piece_x(self):
        return self._x

    def get_piece_y(self):
        return self._y

    def set_piece_x(self, x):
        self._x = x

    def set_piece_y(self, y):
        self._y = y

    def get_piece_type(self):
        return self._p_type

    def set_piece_type(self, p_type):
        self._p_type = p_type

    def get_direction(self):
        return self._direction

    def set_direction(self, direction):
        self._direction = direction

    def get_is_first_step(self):
        return self._is_first_step

    def change_to_not_first_step(self):
        self._is_first_step = False

    def get_possible_steps(self, last_step):
        possible_cells = []
        x = self._x
        y = self._y
        p_type = self.get_piece_type()
        if p_type == PieceType.KNIGHT:
            possible_cells.extend(self.__check_knight_steps(x, y))
        elif p_type == PieceType.KING:
            possible_cells.extend(self.__check_king_steps(x, y))
        elif p_type == PieceType.ROOK:
            possible_cells.extend(self.__check_rook_steps(x, y))
        elif p_type == PieceType.PAWN:
            possible_cells.extend(self.__check_pawn_steps(x, y, last_step))
        elif p_type == PieceType.BISHOP:
            possible_cells.extend(self.__check_bishop_steps())
        elif p_type == PieceType.QUEEN:
            possible_cells.extend(self.__check_queen_steps(x, y))
        return possible_cells

    def __check_bishop_steps(self):
        possible_steps = []
        possible_steps.extend(self.__check_bishop_steps_diagonally(1, 1))
        possible_steps.extend(self.__check_bishop_steps_diagonally(1, -1))
        possible_steps.extend(self.__check_bishop_steps_diagonally(1, 1))
        possible_steps.extend(self.__check_bishop_steps_diagonally(-1, -1))
        return possible_steps

    def __check_rook_steps(self, x, y):
        possible_steps = []
        possible_steps.extend(self.__check_rook_steps_vertical(x, 8, 1))
        possible_steps.extend(self.__check_rook_steps_vertical(x, -1, -1))
        possible_steps.extend(self.__check_rook_steps_horizontal(y, 8, 1))
        possible_steps.extend(self.__check_rook_steps_horizontal(y, -1, -1))
        return possible_steps

    def __check_knight_steps(self, x, y):
        possible_steps = []
        possible_steps.extend(self.__check_cell(x - 3, y + 1))
        possible_steps.extend(self.__check_cell(x - 3, y - 1))
        possible_steps.extend(self.__check_cell(x + 3, y + 1))
        possible_steps.extend(self.__check_cell(x + 3, y - 1))
        possible_steps.extend(self.__check_cell(x + 1, y + 3))
        possible_steps.extend(self.__check_cell(x + 1, y - 3))
        possible_steps.extend(self.__check_cell(x - 1, y + 3))
        possible_steps.extend(self.__check_cell(x - 1, y - 3))
        return possible_steps

    def __check_king_steps(self, x, y):
        possible_steps = []
        possible_steps.extend(self.__check_cell(x + 1, y + 1))
        possible_steps.extend(self.__check_cell(x + 1, y - 1))
        possible_steps.extend(self.__check_cell(x - 1, y + 1))
        possible_steps.extend(self.__check_cell(x - 1, y - 1))
        possible_steps.extend(self.__check_adjacent_cells(x, y))
        return possible_steps

    def __check_pawn_steps(self, x, y, last_step):
        possible_steps = []
        possible_steps.extend(self.__is_correct_pawn_step(x + 1, y))
        possible_steps.extend(self.__is_correct_pawn_step(x + 2, y))
        possible_steps.extend(self.__is_correct_pawn_step(x + 1, y + 1))
        possible_steps.extend(self.__is_correct_pawn_step(x + 1, y - 1))
        possible_steps.extend(self.__is_en_passant(x, y, last_step))
        return possible_steps

    def __check_queen_steps(self, x, y):
        possible_steps = []
        possible_steps.extend(self.__check_bishop_steps())
        possible_steps.extend(self.__check_adjacent_cells(x, y))
        return possible_steps

    def __check_bishop_steps_diagonally(self, x_incr_val, y_incr_val):
        possible_steps = []
        current_x = self.get_piece_x() + x_incr_val
        current_y = self.get_piece_y() + y_incr_val
        while current_x < 8 and current_y < 8:
            current_piece = self.board[current_x][current_y]
            if current_piece is None:
                possible_steps.append(current_piece)
            elif current_piece.get_direction() == self._direction:
                break
            else:
                possible_steps.append(current_piece)
                break
        current_x += x_incr_val
        current_y += y_incr_val
        return possible_steps

    def __is_correct_pawn_step(self, x, y):
        possible_steps = []
        if -1 < x < 8 and -1 < y < 8:
            current = self.board[x][y]
            if self.get_piece_y() != y:
                if current is not None and current.get_direction() != self.get_direction():
                    possible_steps.append(current)
            else:
                if current is None:
                    if y == self.get_piece_y() + 1 * self.get_direction():
                        possible_steps.append(current)
                    else:
                        if self.board[self.get_piece_x()+1][self.get_piece_y()] is None \
                                and self.get_is_first_step():
                            possible_steps.append(current)

        return possible_steps

    def __is_en_passant(self, x, y, last_step):
        possible_steps = []
        if last_step is not None:
            if last_step.get_direction() != self.get_direction():
                if last_step.get_piece_x() == x \
                        and last_step.get_piece_y() == (y + 1 or y - 1):
                    possible_steps.append(last_step)
        return possible_steps

    def __check_rook_steps_vertical(self, begin, end, step_distance):
        possible_steps = []
        for i in range(begin, end, step_distance):
            current_piece = self.board[i][self.get_piece_y()]
            if current_piece is None:
                possible_steps.append(current_piece)
            elif current_piece.get_direction() == self._direction:
                break
            else:
                possible_steps.append(current_piece)
                break
        return possible_steps

    def __check_rook_steps_horizontal(self, begin, end, step_distance):
        possible_steps = []
        for i in range(begin, end, step_distance):
            current_piece = self.board[self.get_piece_x()][i]
            if current_piece is None:
                possible_steps.append(current_piece)
            elif current_piece.get_direction() == self._direction:
                break
            else:
                possible_steps.append(current_piece)
                break
        return possible_steps

    def __check_adjacent_cells(self, x, y):
        possible_steps = []
        possible_steps.extend(self.__check_cell(x + 1, y))
        possible_steps.extend(self.__check_cell(x - 1, y))
        possible_steps.extend(self.__check_cell(x, y + 1))
        possible_steps.extend(self.__check_cell(x, y - 1))
        return possible_steps

    def __check_cell(self, x, y):
        steps = []
        if -1 < x < 8 and -1 < y < 8:
            current = self.board[x][y]
            if current is None or current.get_direction() != self.get_direction():
                steps.append(current)
        return steps
