from enum import Enum


class PieceType(Enum):
    """
    An enum class to store the possible piece types in chess (and the no-type for empty cells)
    """

    NO_TYPE = 0
    PAWN = 1
    ROOK = 2
    KNIGHT = 3
    BISHOP = 4
    QUEEN = 5
    KING = 6
