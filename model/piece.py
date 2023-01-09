class Piece:

    def __init__(self, x, y, p_type, direction):
        self._x = x
        self._y = y
        self._p_type = p_type
        self._direction = direction
        self._is_first_step = True
        self._captured_pieces = list()

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

    def get_direction(self):
        return self._direction

    def get_is_first_step(self):
        return self._is_first_step

    def change_to_not_first_step(self):
        self._is_first_step = False

    def add_to_captured_pieces(self, piece):
        self._captured_pieces.append(piece)

    def remove_from_captured_pieces(self, piece):
        self._captured_pieces.remove(piece)
