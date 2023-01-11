class Player:
    def __init__(self, color):
        self._color = color
        self._direction = None

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_direction(self):
        return self._direction

    def set_direction(self, direction):
        self._direction = direction
