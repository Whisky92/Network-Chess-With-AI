import socket
from _thread import *
import pickle


def start_server():

    server = "localhost"
    port = 5555

    names = ["", ""]
    index = 0

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((server, port))
    except socket.error as e:
        print(e)

    s.listen(2)

    def threaded_client(conn, index):

        conn.send(pickle.dumps(True))

    while True:
        conn, addr = s.accept()

        start_new_thread(threaded_client, (conn, index))
        index += 1


