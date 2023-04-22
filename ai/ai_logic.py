import copy
from copy import deepcopy
from ai.piece_values import PieceValues
from model.piece_type import PieceType
from model.board import Board
from model.player import Player
from model.colors import Color
from model.game import Game


class AiLogic:

    ai_player_color: Color
    enemy_color: Color

    @staticmethod
    def set_ai_player(color):
        AiLogic.ai_player_color = color
        AiLogic.enemy_color = color.WHITE if color == color.BLACK else color.WHITE

    @staticmethod
    def minimax(board, depth, color, game):

        if depth == 0 \
                or not game.is_king_alive(AiLogic.enemy_color) \
                or not game.is_king_alive(AiLogic.ai_player_color) \
                or game.is_stalemate():
            return AiLogic.evaluate_board(board), board

        if color == AiLogic.ai_player_color:

            enemy_color = color.WHITE if color == color.BLACK else color.BLACK
            max_eval = float('-inf')
            best_move = None

            for move in AiLogic.get_all_moves(AiLogic.ai_player_color, game):
                value = AiLogic.minimax(move[0].get_board(), depth - 1, enemy_color, move[0])[0]
                max_eval = max(max_eval, value)
                if max_eval == value:
                    best_move = move

            return max_eval, best_move[1], best_move[2]

        else:

            enemy_color = color.WHITE if color == color.BLACK else color.BLACK
            min_eval = float('inf')
            best_move = None

            for move in AiLogic.get_all_moves(color, game):
                value = AiLogic.minimax(move[0].get_board(), depth - 1, enemy_color, move[0])[0]
                min_eval = min(min_eval, value)
                if min_eval == value:
                    best_move = move

            return min_eval, best_move[1], best_move[2]

    @staticmethod
    def get_all_moves(color, game):
        moves = []

        player = game.get_white_player() if color == Color.WHITE \
            else game.get_black_player()

        targeted = game.is_king_targeted(player)
        piece_list = player.get_pieces_on_board()

        if targeted:
            piece_list = AiLogic.get_pieces_if_targeted(game)

        for piece in piece_list:

            piece_x = piece.get_piece_x()
            piece_y = piece.get_piece_y()

            move_list = game.filter_wrong_moves(piece_x, piece_y)

            if targeted:
                move_list = AiLogic.steps_of_piece_if_king_is_targeted(game, piece)

            for cell in move_list:

                target_x = cell.get_piece().get_piece_x()
                target_y = cell.get_piece().get_piece_y()

                test_game = copy.deepcopy(game)

                piece_to_move = test_game.get_board_table()[piece_x][piece_y]
                target_piece = test_game.get_board_table()[target_x][target_y]

                test_game.move(piece_to_move, target_piece)

                moves.append((test_game, (piece_x, piece_y), (target_x, target_y)))

        return moves

    @staticmethod
    def get_pieces_if_targeted(game):
        lst = []

        for i in game.steps_if_king_is_targeted():
            lst.append(i[0].get_piece())
        return lst

    @staticmethod
    def steps_of_piece_if_king_is_targeted(game, piece):
        for i in game.steps_if_king_is_targeted():
            if i[0].get_piece() == piece:
                return i[1]
        return None

    @staticmethod
    def evaluate_board(board):

        white_value = 0
        black_value = 0
        table = board.get_board()

        for i in range(0, 8):
            for j in range(0, 8):
                piece = table[i][j].get_piece()

                if piece.get_piece_type() != PieceType.NO_TYPE:

                    p_type = piece.get_piece_type()
                    enemy_border = 0 if piece.get_direction() == 1 else 7

                    if p_type == PieceType.PAWN and \
                            piece.get_piece_x() == enemy_border:
                        piece = deepcopy(piece)
                        piece.set_piece_type(PieceType.QUEEN)

                    if piece.get_direction() == 1:

                        white_value += PieceValues.piece_strengths[p_type]
                        white_value += PieceValues.piece_values_based_on_position[p_type]\
                            [piece.get_piece_x()][piece.get_piece_y()]
                    else:
                        black_value += PieceValues.piece_strengths[p_type]
                        black_value += PieceValues.piece_values_based_on_position[p_type]\
                            [7 - piece.get_piece_x()][piece.get_piece_y()]

        value = (white_value - black_value) if AiLogic.ai_player_color == Color.WHITE else (black_value - white_value)

        return value

