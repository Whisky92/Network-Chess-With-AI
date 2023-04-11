import socket
import pickle


class Network:
    def __init__(self, ip):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.client.settimeout(2)
        self.server = ip
        self.port = 9999
        self.address = (self.server, self.port)

    def connect(self):
        try:
            self.client.connect(self.address)
            return pickle.loads(self.client.recv(4096))
        except socket.timeout:
            print("Timeout error")
        except:
            print("An error occurred in connection")

    def send_board(self, board):
        try:
            self.client.send(pickle.dumps(board))
            return pickle.loads(self.client.recv(4096*2))
        except socket.error as e:
            print(e)

    def send_object(self, obj):
        try:
            self.client.send(pickle.dumps(obj))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)
