import socket
from _thread import *
import pickle
from network.my_string import MyString
from gui.game_window import GameWindow


def start_server(ip):
    """
    A function to start hosting a local server

    :param ip: the ip of the server to host
    """

    ip = ip
    port = 9999

    ready_boxes = [False, False]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []

    in_game = [False]

    player_names = ["", ""]
    ready_to_play = ["no"]
    rolled_players = ["", ""]
    game_time = [None]
    steps = [[]]

    current_message_box = []
    index = [0]

    try:
        s.bind((ip, port))
    except socket.error as e:
        print(e)

    s.listen(2)

    def get_first_enemy_player_message_box(name):
        """
        Returns the current message box indicator string of the other player, if there is one

        :param name: the name of the player who will receive the message box indicator string
        :return: a list containing the message box indicator string, if none, an empty list
        """

        for i in current_message_box:
            if i[0] != name:
                current = i
                current_message_box.remove(i)
                if current[1] == "end_of_game":
                    return [current[1], current[2]]
                return [current[1]]
        return []

    def if_game_has_already_started(conn, data):
        """
        Manages requests in case the game has already started

        :param conn: the connection data of the current client
        :param data: the received data from the request
        """

        if type(data) == list and type(data[0]) == str and data[0] in player_names:

            if len(current_message_box) == 0:
                current_message_box.append(data)
            conn.send(pickle.dumps(MyString("OK")))

        elif type(data) == MyString and data.get_string() in player_names:
            conn.send(pickle.dumps(get_first_enemy_player_message_box(data.get_string())))

        elif type(data) == list:
            steps[0] = data
            conn.send(pickle.dumps(MyString("OK")))

        elif type(data) == MyString and data.get_string() == "get_steps":
            conn.send(pickle.dumps(steps[0]))

    def set_players(conn, data, ind):
        """
        Checks whether the given name is available and stores them in lists, and the turn order as well

        :param conn: the connection data of the current client
        :param data: the received data from the request
        :param ind: the index of the current connected player in the lobby
        """

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

    def manage_check_boxes(conn, data):
        """
        Manages checkbox states whether they are checked or not in the lobby

        :param conn: the connection data of the current client
        :param data: the received data from the request
        """
        if conn == connections[0]:
            ready_boxes[0] = data.get_string()
            conn.send(pickle.dumps(MyString(ready_boxes[1])))
        else:
            ready_boxes[1] = data.get_string()
            conn.send(pickle.dumps(MyString(ready_boxes[0])))

    def if_game_has_not_started(conn, data, ind):
        """
        Manages requests in case the game has not started yet

        :param conn: the connection data of the current client
        :param data: the received data from the request
        :param ind: the index of the current connected player in the lobby
        """

        if type(data) == MyString and data.get_string() in ["checked", "unchecked"]:
            manage_check_boxes(conn, data)

        elif type(data) == MyString and data.get_string().isdigit():
            game_time[0] = data.get_string()
            conn.send(pickle.dumps(MyString("OK")))

        elif type(data) == MyString and data.get_string() == "wait":
            conn.send(pickle.dumps(player_names))

        elif type(data) == MyString and data.get_string() == "get_time":
            conn.send(pickle.dumps(MyString(game_time[0])))

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
            set_players(conn, data, ind)

    def reset():
        """
        Resets the variables after a game ends
        """

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

    def threaded_client(conn, ind):
        """
        Handles the management of the given client

        :param conn: the connection data of the current client
        :param ind: the index of the current connected player in the lobby
        """

        conn.send(pickle.dumps(True))

        while True:
            try:
                data = pickle.loads(conn.recv(4096))
                if not data:
                    break
                elif in_game[0]:
                    if_game_has_already_started(conn, data)

                else:
                    if_game_has_not_started(conn, data, ind)

            except:
                break

        conn.close()
        connections.remove(conn)
        if len(connections) == 0:
            reset()

    while True:
        conn, addr = s.accept()
        connections.append(conn)

        start_new_thread(threaded_client, (conn, index[0]))
        index[0] += 1
