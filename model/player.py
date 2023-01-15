class Player:
    def __init__(self, color, direction):
        self._color = color
        self._direction = direction
        self._captured_pieces = list()
        self._pieces_on_board = list()

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_direction(self):
        return self._direction

    def set_direction(self, direction):
        self._direction = direction

    def get_captured_pieces(self):
        return self._captured_pieces

    def add_to_captured_pieces(self, piece):
        self._captured_pieces.append(piece)

    def remove_from_captured_pieces(self, piece):
        self._captured_pieces.remove(piece)

    def get_pieces_on_board(self):
        return self._pieces_on_board

    def add_to_pieces_on_board(self, piece):
        self._pieces_on_board.append(piece)

    def remove_from_pieces_on_board(self, piece):
        self._pieces_on_board.remove(piece)
