class Piece:

    def __init__(self, p_type, direction):
        self._p_type = p_type
        self.direction = direction
        self.is_first_step = True
        self.captured_pieces = list()

    def get_piece_type(self):
        return self._p_type

    def get_is_first_step(self):
        return self.is_first_step

    def change_to_not_first_step(self):
        self.is_first_step = False

    def add_to_captured_pieces(self, piece):
        self.captured_pieces.append(piece)

    def remove_from_captured_pieces(self, piece):
        self.captured_pieces.remove(piece)
