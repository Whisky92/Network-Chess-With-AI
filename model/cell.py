class Cell:
    """
    A class to represent a cell on the board
    """

    def __init__(self, piece):
        self._piece = piece

    def get_piece(self):
        return self._piece

    def set_piece(self, piece):
        self._piece = piece
