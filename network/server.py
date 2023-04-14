import socket
from _thread import *
from network.network_messages import NetworkMessages
from model.board import Board
import pickle
from network.my_string import MyString
from gui.game_window import GameWindow
from gui.my_message_box import *

def start_server():

    ip = str(socket.gethostbyname(socket.gethostname()))
    print(ip)
    port = 9999

    ready_boxes = [False, False]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []

    in_game = [False]

    player_names = ["", ""]
    ready_to_play = ["no"]
    rolled_players = ["", ""]
    steps = [[]]

    current_message_box = []

    index = [0]

    try:
        s.bind((ip, port))
    except socket.error as e:
        print(e)

    s.listen(2)

    def get_first_enemy_player_message_box(name):
        for i in current_message_box:
            if i[0] != name:
                current = i
                current_message_box.remove(i)
                if current[1] == "end_of_game":
                    return [current[1], current[2]]
                return [current[1]]
        return []

    def threaded_client(conn, ind):
        conn.send(pickle.dumps(True))
        while True:
            try:
                data = pickle.loads(conn.recv(4096))
                print(data, " ez ez itt")
                if not data:
                    break
                elif in_game[0]:
                    print(type(data), "adatttt")
                    if type(data) == list and type(data[0]) == str and data[0] in player_names:
                        print(data[0], data[1])
                        if len(current_message_box) == 0:
                            current_message_box.append(data)
                        print("nééééééééééééééééééééézzzz ideeeeeeeeee")
                        conn.send(pickle.dumps(MyString("OK")))
                    elif type(data) == MyString and data.get_string() in player_names:
                        print("helloka")
                        conn.send(pickle.dumps(get_first_enemy_player_message_box(data.get_string())))
                    elif type(data) == list:
                        print("ez az adat jött be na ez itt naaaajóóóó: ", data)
                        steps[0] = data
                        conn.send(pickle.dumps(MyString("OK")))
                    elif type(data) == MyString and data.get_string() == "get_steps":
                        print("ez az adat jött be: ", data)
                        print("ELKÜLDVE: ", steps[0])
                        conn.send(pickle.dumps(steps[0]))
                else:
                    if type(data) == MyString and data.get_string() in ["checked", "unchecked"]:
                        if conn == connections[0]:
                            ready_boxes[0] = data.get_string()
                            conn.send(pickle.dumps(MyString(ready_boxes[1])))
                        else:
                            ready_boxes[1] = data.get_string()
                            conn.send(pickle.dumps(MyString(ready_boxes[0])))
                    elif type(data) == MyString and data.get_string() == "wait":
                        conn.send(pickle.dumps(player_names))
                    elif type(data) == MyString and data.get_string() == "start_game":
                        if ready_to_play[0] == "yes":
                            in_game[0] = True
                        conn.send(pickle.dumps(MyString(ready_to_play[0])))
                    elif type(data) == MyString and data.get_string() == "get_rolls":
                        conn.send(pickle.dumps(rolled_players))
                    elif type(data) == MyString and data.get_string() == "ready":
                        ready_to_play[0] = "yes"
                        conn.send(pickle.dumps(MyString("OK")))
                    elif type(data) == MyString:
                        index_to_check = 0 if ind == 1 else 1
                        other_player_name = player_names[index_to_check]

                        correct = other_player_name != data.get_string()

                        if correct:
                            player_names[ind] = data.get_string()

                        if ind == 1:

                            first = GameWindow.get_first_player(player_names[0], player_names[1])
                            second = player_names[0] if first != player_names[0] else player_names[1]

                            rolled_players[0] = first
                            rolled_players[1] = second

                        conn.send(pickle.dumps(player_names))
            except:
                break

        conn.close()
        connections.remove(conn)
        if len(connections) == 0:
            ready_boxes[0] = False
            ready_boxes[1] = False
            in_game[0] = False
            player_names[0] = ""
            player_names[1] = ""
            ready_to_play[0] = "no"
            rolled_players[0] = ""
            rolled_players[1] = ""
            steps[0] = []
            index[0] = 0

    while True:
        conn, addr = s.accept()
        connections.append(conn)

        start_new_thread(threaded_client, (conn, index[0]))
        index[0] += 1