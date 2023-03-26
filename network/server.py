import socket
from _thread import *
from network.network_messages import NetworkMessages
import pickle
from network.my_string import MyString

def start_server():

    hostname = socket.gethostname()
    print(hostname)

    ip = "0.0.0.0"
    port = 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []

    player_names = ["", ""]
    index = 0

    try:
        s.bind((ip, port))
    except socket.error as e:
        print(e)

    s.listen(2)

    def threaded_client(conn, index):

        conn.send(pickle.dumps(True))
        while True:
            try:
                data = pickle.loads(conn.recv(4096))
                print(data)
                if not data:
                    continue
                elif type(data) == MyString and data.get_string() == "wait":
                    print("ez ilyen")
                    conn.send(pickle.dumps(player_names))
                elif type(data) == MyString:
                    index_to_check = 0 if index == 1 else 1
                    other_player_name = player_names[index_to_check]

                    correct = other_player_name != data.get_string()

                    if correct:
                        player_names[index] = data.get_string()

                    print(player_names)
                    conn.send(pickle.dumps(player_names))
            except:
                break
        conn.close()

    while True:
        conn, addr = s.accept()
        connections.append(conn)

        start_new_thread(threaded_client, (conn, index))
        index += 1


