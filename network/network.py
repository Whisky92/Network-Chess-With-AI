import socket
import pickle
import sys


class Network:
    """
    A class for initating connection to a server, for sending and receiving data
    """

    def __init__(self, ip):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(2)
        self.server = ip
        self.port = 9999
        self.address = (self.server, self.port)

    def connect(self):
        """
        Tries to connect to the provided ip address and port
        """

        try:
            self.client.connect(self.address)
            return pickle.loads(self.client.recv(4096))
        except socket.timeout:
            print("Timeout error")
        except Exception as e:
            print(e)
            print("An error occurred in connection")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    def send_board(self, board):
        """
        Sends a board object through network

        :param board: the board to send
        :return: the response from the server
        """

        try:
            self.client.send(pickle.dumps(board))
            return pickle.loads(self.client.recv(4096*2))
        except socket.error as e:
            print(e)

    def send_object(self, obj):
        """
        Sends an object through network

        :param obj: the object to send
        :return: the response from the server
        """

        try:
            self.client.send(pickle.dumps(obj))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)
