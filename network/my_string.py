class MyString:
    """
    A class to wrap string variables to send it through network
    """

    def __init__(self, string):
        self.string = string

    def get_string(self):
        return self.string

    def set_string(self, string):
        self.string = string
