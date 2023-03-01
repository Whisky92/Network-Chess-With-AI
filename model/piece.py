from model.piece_type import PieceType
from model.king_step_checker import KingStepChecker


class Piece:
    def __init__(self, x, y, p_type, direction):
        self._x = x
        self._y = y
        self._p_type = p_type
        self._direction = direction
        self._is_first_step = True
        self._en_passant_step = None
        self._is_able_to_evolve = False

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

    def get_en_passant_step(self):
        return self._en_passant_step

    def delete_last_en_passant_step(self):
        self._en_passant_step = None

    def change_to_not_first_step(self):
        self._is_first_step = False

    def get_is_able_to_evolve(self):
        return self._is_able_to_evolve

    def change_to_able_to_evolve(self):
        if self._direction == 1:
            enemy_border = 7
        else:
            enemy_border = 0
        if self._p_type == PieceType.PAWN and self._x == enemy_border:
            self._is_able_to_evolve = True

    def set_to_not_able_to_evolve(self):
        self._is_able_to_evolve = False

    def get_possible_steps(self, board, last_step, white_player, black_player, castling_step, castling_rook,
                           rook_target):
        possible_cells = []
        x = self._x
        y = self._y
        p_type = self.get_piece_type()
        if p_type == PieceType.KNIGHT:
            possible_cells.extend(self.__check_knight_steps(board, x, y))
        elif p_type == PieceType.KING:
            possible_cells.extend(KingStepChecker.check_king_steps(board, x, y, white_player, black_player, last_step,
                                                                   castling_step, castling_rook, rook_target))
        elif p_type == PieceType.ROOK:
            possible_cells.extend(self.__check_rook_steps(board, x, y))
        elif p_type == PieceType.PAWN:
            possible_cells.extend(self.__check_pawn_steps(board, x, y, last_step))
        elif p_type == PieceType.BISHOP:
            possible_cells.extend(self.__check_bishop_steps(board))
        elif p_type == PieceType.QUEEN:
            possible_cells.extend(self.__check_queen_steps(board, x, y))
        return possible_cells

    def __check_bishop_steps(self, board):
        possible_steps = []
        possible_steps.extend(self.__check_bishop_steps_diagonally(board, 1, 1))
        possible_steps.extend(self.__check_bishop_steps_diagonally(board, 1, -1))
        possible_steps.extend(self.__check_bishop_steps_diagonally(board, -1, 1))
        possible_steps.extend(self.__check_bishop_steps_diagonally(board, -1, -1))
        return possible_steps

    def __check_rook_steps(self, board, x, y):
        possible_steps = []
        possible_steps.extend(self.__check_rook_steps_vertical(board, x+1, 8, 1))
        possible_steps.extend(self.__check_rook_steps_vertical(board, x-1, -1, -1))
        possible_steps.extend(self.__check_rook_steps_horizontal(board, y+1, 8, 1))
        possible_steps.extend(self.__check_rook_steps_horizontal(board, y-1, -1, -1))
        return possible_steps

    def __check_knight_steps(self, board, x, y):
        possible_steps = []
        cell = board[x][y]
        possible_steps.extend(KingStepChecker.check_cell(board, cell, x - 2, y + 1))
        possible_steps.extend(KingStepChecker.check_cell(board, cell, x - 2, y - 1))
        possible_steps.extend(KingStepChecker.check_cell(board, cell, x + 2, y + 1))
        possible_steps.extend(KingStepChecker.check_cell(board, cell, x + 2, y - 1))
        possible_steps.extend(KingStepChecker.check_cell(board, cell, x + 1, y + 2))
        possible_steps.extend(KingStepChecker.check_cell(board, cell, x + 1, y - 2))
        possible_steps.extend(KingStepChecker.check_cell(board, cell, x - 1, y + 2))
        possible_steps.extend(KingStepChecker.check_cell(board, cell, x - 1, y - 2))
        return possible_steps

    def __check_pawn_steps(self, board, x, y, last_step):
        possible_steps = []
        possible_steps.extend(self.__is_correct_pawn_step(board, x - 1 * self.get_direction(), y))
        possible_steps.extend(self.__is_correct_pawn_step(board, x - 2 * self.get_direction(), y))
        possible_steps.extend(self.__is_correct_pawn_step(board, x - 1 * self.get_direction(), y + 1))
        possible_steps.extend(self.__is_correct_pawn_step(board, x - 1 * self.get_direction(), y - 1))
        possible_steps.extend(self.__is_en_passant(board, x, y, last_step))
        return possible_steps

    def __check_queen_steps(self, board, x, y):
        cell = board[x][y]
        possible_steps = []
        possible_steps.extend(self.__check_bishop_steps(board))
        possible_steps.extend(KingStepChecker.check_adjacent_cells(board, cell, x, y))
        return possible_steps

    def __check_bishop_steps_diagonally(self, board, x_incr_val, y_incr_val):
        possible_steps = []
        current_x = self.get_piece_x() + x_incr_val
        current_y = self.get_piece_y() + y_incr_val
        while -1 < current_x < 8 and -1 < current_y < 8:
            current = board[current_x][current_y]
            current_piece = current.get_piece()
            if current_piece.get_direction() == 0:
                possible_steps.append(current)
            elif current_piece.get_direction() != self.get_direction():
                possible_steps.append(current)
                break
            else:
                break
            current_x += x_incr_val
            current_y += y_incr_val
        return possible_steps

    def __is_correct_pawn_step(self, board, x, y):
        possible_steps = []
        if -1 < x < 8 and -1 < y < 8:
            current = board[x][y]
            current_piece = current.get_piece()
            if self.get_piece_y() != y:
                if current_piece.get_direction() != 0 and current_piece.get_direction() != self.get_direction():
                    possible_steps.append(current)
            else:
                if current_piece.get_direction() == 0:
                    if x == self.get_piece_x() - 1 * self.get_direction():
                        possible_steps.append(current)
                    else:
                        if board[self.get_piece_x() - 1 * self.get_direction()][self.get_piece_y()]\
                                .get_piece().get_direction() == 0 \
                                and self.get_is_first_step():
                            possible_steps.append(current)

        return possible_steps

    def __is_en_passant(self, board, x, y, last_step_cell):

        possible_steps = []
        if last_step_cell is not None:
            last_step = last_step_cell.get_piece()
            if last_step.get_direction() != self.get_direction():
                if last_step.get_piece_x() == x \
                        and (last_step.get_piece_y() == y + 1 or
                             last_step.get_piece_y() == y - 1):
                    step_x = last_step.get_piece_x() - 1 * self.get_direction()
                    step_y = last_step.get_piece_y()
                    step = board[step_x][step_y]
                    possible_steps.append(step)
                    self._en_passant_step = step
        return possible_steps

    def __check_rook_steps_vertical(self, board, begin, end, step_distance):
        possible_steps = []
        for i in range(begin, end, step_distance):
            current = board[i][self.get_piece_y()]
            current_piece = current.get_piece()
            if current_piece.get_direction() == 0:
                possible_steps.append(current)
            elif current_piece.get_direction() != self.get_direction():
                possible_steps.append(current)
                break
            else:
                break
        return possible_steps

    def __check_rook_steps_horizontal(self, board, begin, end, step_distance):
        possible_steps = []
        for i in range(begin, end, step_distance):
            current = board[self.get_piece_x()][i]
            current_piece = current.get_piece()
            if current_piece.get_direction() == 0:
                possible_steps.append(current)
            elif current_piece.get_direction() != self.get_direction():
                possible_steps.append(current)
                break
            else:
                break
        return possible_steps
