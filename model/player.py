class Player:
    def __init__(self, color):
        self._color = color
        self._direction = None
        self._captured_pieces = list()

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_direction(self):
        return self._direction

    def set_direction(self, direction):
        self._direction = direction

    def add_to_captured_pieces(self, piece):
        self._captured_pieces.append(piece)

    def remove_from_captured_pieces(self, piece):
        self._captured_pieces.remove(piece)
