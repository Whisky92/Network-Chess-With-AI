import copy
from copy import deepcopy
from ai.piece_values import PieceValues
from model.piece_type import PieceType
from model.board import Board
from model.player import Player
from model.colors import Color
from model.game import Game


class AiLogic:
    """
    A class to store the logic of the Artificial Intelligence
    """

    ai_player_color: Color
    enemy_color: Color

    @staticmethod
    def set_ai_player(color):
        """
        A setter method for ai_player_color

        :param color: the color to set
        """
        AiLogic.ai_player_color = color
        AiLogic.enemy_color = color.WHITE if color == color.BLACK else color.WHITE

    @staticmethod
    def minimax(board, depth, color, game):
        """
        MiniMax algorithm to decide the most beneficial step for the AI

        :param board: the current game board
        :param depth: the number of rounds to examine all possible step combinations
        :param color: the color of the player to be checked
        :param game: the current game
        :return: the value and the start and target coordinates of the best step
        """

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
        """
        Returns all possible moves of the player indicated by the given color

        :param color: the color the player
        :param game: the current game
        :return: the list of possible moves
        """

        moves = []

        player = game.get_white_player() if color == Color.WHITE \
            else game.get_black_player()

        targeted = game.is_king_targeted(player)
        piece_list = player.get_pieces_on_board()

        if targeted:
            piece_list = AiLogic.get_pieces_if_targeted(game, player)

        for piece in piece_list:

            piece_x = piece.get_piece_x()
            piece_y = piece.get_piece_y()

            move_list = game.filter_wrong_moves(piece_x, piece_y)

            if targeted:
                move_list = AiLogic.steps_of_piece_if_king_is_targeted(game, player, piece)

            for cell in move_list:

                test_game, target_x, target_y = Game.move_in_test_game(piece_x, piece_y, cell, game)

                moves.append((test_game, (piece_x, piece_y), (target_x, target_y)))

        return moves

    @staticmethod
    def get_pieces_if_targeted(game, player):
        """
        Returns the possible movable pieces in case the king is targeted

        :param game: the current game
        :param player: the player whose king is about to be checked

        :return: list of possible moves
        """
        lst = []

        for i in game.steps_if_king_is_targeted(player):
            lst.append(i[0].get_piece())
        return lst

    @staticmethod
    def steps_of_piece_if_king_is_targeted(game, player, piece):
        """
        Returns the possible targets of the given piece in case the king is targeted

        :param game: the current game
        :param player: the player whose king is about to be checked
        :param piece: the current piece

        :return: the list of possible targets
        """
        for i in game.steps_if_king_is_targeted(player):
            if i[0].get_piece() == piece:
                return i[1]
        return None

    @staticmethod
    def evaluate_board(board):
        """
        Evaluates the game board based on the piece values and positions

        :param board: the current game board

        :return: the value of the board
        """

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

