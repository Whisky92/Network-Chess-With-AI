class Player:
    """
    A class to represent a player in the game
    """

    def __init__(self, color, direction):
        self._color = color
        self._direction = direction
        self._pieces_on_board = list()
        self._can_stalemate = False

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_direction(self):
        return self._direction

    def set_direction(self, direction):
        self._direction = direction

    def set_can_stalemate(self, value):
        self._can_stalemate = value

    def get_pieces_on_board(self):
        return self._pieces_on_board

    def add_to_pieces_on_board(self, piece):
        """
        Adds a piece to the list that stores the owned pieces

        :param piece: the piece to add
        """
        self._pieces_on_board.append(piece)

    def remove_from_pieces_on_board(self, piece):
        """
        Removes a piece from the list that stores the owned pieces

        :param piece: the piece to remove
        """
        self._pieces_on_board.remove(piece)
