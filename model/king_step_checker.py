from model.piece_type import PieceType


class KingStepChecker:

    @staticmethod
    def check_king_steps(board, x, y, white_player, black_player, last_step, castling_step, castling_rook, rook_target):
        possible_cells = []
        cell = board[x][y]
        player = KingStepChecker.__get_player_by_direction(cell.get_piece().get_direction(), white_player, black_player)
        possible_cells.extend(KingStepChecker.is_king_cells_targeted(board, player, white_player, black_player,
                                                                     last_step, castling_step, castling_rook,
                                                                     rook_target))

        direction = cell.get_piece().get_direction()
        king_x = 0 if direction == -1 else 7
        king_y = 4

        cell_x = cell.get_piece().get_piece_x()

        if board[cell_x][7].get_piece().get_piece_type() == PieceType.ROOK \
            and board[cell_x][7].get_piece().get_direction() \
                == direction and x == king_x and y == king_y:

            possible_cells.extend(KingStepChecker.add_castling_steps_to_possible_steps(board, cell,
                                                                                       cell_x,
                                                                                       cell.get_piece().get_piece_y() + 2,
                                                                                       castling_step, castling_rook,
                                                                                       rook_target, white_player,
                                                                                       black_player, last_step))
        if board[cell_x][0].get_piece().get_piece_type() == PieceType.ROOK \
            and board[cell_x][0].get_piece().get_direction() \
                == direction:

            possible_cells.extend(KingStepChecker.add_castling_steps_to_possible_steps(board, cell,
                                                                                       cell_x,
                                                                                       cell.get_piece().get_piece_y() - 2,
                                                                                       castling_step, castling_rook,
                                                                                       rook_target, white_player,
                                                                                       black_player, last_step))
        return possible_cells

    @staticmethod
    def __check_king_steps(board, cell, x, y):
        possible_steps = []
        possible_steps.extend(KingStepChecker.check_cell(board, cell, x + 1, y + 1))
        possible_steps.extend(KingStepChecker.check_cell(board, cell, x + 1, y - 1))
        possible_steps.extend(KingStepChecker.check_cell(board, cell, x - 1, y + 1))
        possible_steps.extend(KingStepChecker.check_cell(board, cell, x - 1, y - 1))
        possible_steps.extend(KingStepChecker.check_adjacent_cells(board, cell, x, y))
        return possible_steps

    @staticmethod
    def get_king_cell(board, player):
        for i in player.get_pieces_on_board():
            if i.get_piece_type() == PieceType.KING:
                return board[i.get_piece_x()][i.get_piece_y()]

    @staticmethod
    def check_cell(board, cell, x, y):
        steps = []
        if -1 < x < 8 and -1 < y < 8:
            current = board[x][y]
            if current.get_piece().get_direction() != cell.get_piece().get_direction():
                steps.append(current)
        return steps

    @staticmethod
    def is_king_cells_targeted(board, player, white_player, black_player, last_step, castling_step, castling_rook,
                               rook_target):
        king_cell = KingStepChecker.get_king_cell(board, player)
        non_targeted_cells = []
        enemy_player = black_player if player == white_player else white_player
        for i in KingStepChecker.__check_king_steps(board, king_cell, king_cell.get_piece().get_piece_x(),
                                                    king_cell.get_piece().get_piece_y()):
            if not KingStepChecker.is_cell_targeted(board, i, enemy_player, white_player, black_player, last_step,
                                                    castling_step, castling_rook, rook_target):
                non_targeted_cells.append(i)
        return non_targeted_cells

    @staticmethod
    def check_adjacent_cells(board, cell, x, y):
        possible_steps = []
        possible_steps.extend(KingStepChecker.check_cell(board, cell, x + 1, y))
        possible_steps.extend(KingStepChecker.check_cell(board, cell, x - 1, y))
        possible_steps.extend(KingStepChecker.check_cell(board, cell, x, y + 1))
        possible_steps.extend(KingStepChecker.check_cell(board, cell, x, y - 1))
        return possible_steps

    @staticmethod
    def add_castling_steps_to_possible_steps(board, cell, x, y, castling_step, castling_rook, rook_target, white_player,
                                             black_player, last_step):
        possible_steps = []
        target_piece = board[x][y]
        if 7 - y < y - 0:
            castling = KingStepChecker.__check_castling_on_one_side(board, cell, target_piece, 7, white_player,
                                                                    black_player, last_step, castling_step,
                                                                    castling_rook, rook_target)
            if len(castling) != 0:
                if board[x][5] not in rook_target:
                    rook_target.append(board[x][5])
                possible_steps.extend(castling)
        else:
            castling = KingStepChecker.__check_castling_on_one_side(board, cell, target_piece, 0, white_player,
                                                                    black_player, last_step, castling_step,
                                                                    castling_rook, rook_target)
            if len(castling) != 0:
                if board[x][3] not in rook_target:
                    rook_target.append(board[x][3])
                possible_steps.extend(castling)
        return possible_steps

    @staticmethod
    def is_cell_targeted(board, cell, enemy_player, white_player, black_player, last_step, castling_step, castling_rook, rook_target):
        player = black_player if enemy_player == white_player else white_player
        changed = False
        changed_to_zero = False
        for i in enemy_player.get_pieces_on_board():
            dir = i.get_direction()
            if i == cell.get_piece() or i.get_piece_type() == PieceType.KING:
              continue
            elif i.get_piece_type() == PieceType.PAWN and cell.get_piece().get_direction() == 0:
                changed = True
                cell.get_piece().set_direction(player.get_direction())
            elif cell.get_piece().get_direction() == dir:
                changed_to_zero = True
                cell.get_piece().set_direction(0)
            result = cell in i.get_possible_steps(board, last_step, white_player, black_player, castling_step,
                                                  castling_rook, rook_target)
            if changed:
                cell.get_piece().set_direction(0)
                changed = False
            if changed_to_zero:
                cell.get_piece().set_direction(dir)
                changed_to_zero = False
            if result:
                return True
        return False

    @staticmethod
    def __check_castling_on_one_side(board, cell, target_piece, rook_y, white_player, black_player, last_step,
                                     castling_step, castling_rook, rook_target):
        possible_steps = []
        cell_y = cell.get_piece().get_piece_y()
        target_x = target_piece.get_piece().get_piece_x()
        target_y = target_piece.get_piece().get_piece_y()
        rook_cell = board[target_x][rook_y]
        if cell_y > target_y:
            min_y = target_y
            max_y = cell_y
        else:
            min_y = cell_y
            max_y = target_y
        if rook_cell.get_piece().get_is_first_step() and cell.get_piece().get_is_first_step():
            enemy_player = black_player if cell.get_piece().get_direction() == \
                                                 white_player.get_direction() else white_player
            for i in range(min_y + 1, max_y):
                current_cell = board[target_x][i]
                if current_cell.get_piece().get_piece_type() != PieceType.NO_TYPE:
                    return possible_steps
            for i in range(min_y, max_y + 1):
                current_cell = board[target_x][i]
                if KingStepChecker.is_cell_targeted(board, current_cell, enemy_player, white_player, black_player,
                                                    last_step, castling_step, castling_rook, rook_target):
                    return possible_steps
            if target_piece not in castling_step:
                castling_rook.append(rook_cell)
                castling_step.append(target_piece)
            possible_steps.append(target_piece)
        return possible_steps

    @staticmethod
    def __get_player_by_direction(direction, white_player, black_player):
        if white_player.get_direction() == direction:
            return white_player
        return black_player
