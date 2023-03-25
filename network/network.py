import socket
import pickle


class Network:
    def __init__(self, ip):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ip
        self.port = 5555
        self.address = (self.server, self.port)

    def connect(self):
        try:
            self.client.connect(self.address)
            return pickle.loads(self.client.recv(4096))
        except:
            print("An error occurred in connection")