import socket

# Noughts and cross game where one instance chooses to act as the server and the other as the client.

isServer = input('Act as server? (Y/N):\n').upper() == "Y"

if isServer:
    my_player_number = 1
    opponent_player_number = 2
    mark = "x"
else:
    my_player_number = 2
    opponent_player_number = 2
    mark = "o"

board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]

# Setup connections and wait for client to join
if isServer:
    
    # create an INET, STREAMing socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to a public host, and a well-known port
    server_socket.bind(('', 4444))
    # become a server socket
    server_socket.listen()

    print("Waiting for connection")
    (client_socket, address) = server_socket.accept()
    
    server_socket.close()
    
    print("Another player connected")
    

# attempt to join server
else:
    
    address = input("Enter server address: ")
    
    # create an INET, STREAMing socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # now connect to the web server on port 80 - the normal http port
    print("Connecting to server")
    client_socket.connect(('localhost', 4444))
    
    



def make_move(position):
    board[position] = my_player_number
    client_socket.send(position)


def receive_move():
    receivedMove = client_socket.recv()
    board[receivedMove] = opponent_player_number
    
    
# Luc Game
# Board Layout:
#    0 1 2
# 0  0|1|2
# 1  3|4|5
# 2  6|7|8

def show_board():
    print('{}|{}|{}\n'
          '{}|{}|{}\n'
          '{}|{}|{}'.format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8]))


def is_valid_move(position):
    return board[position] == 0


def convert_position(row, column):
    return row * 3 + column

def is_game_over():
    #TODO implement win conditions


# board above


# show board and ask for a row and a column to play in
game_over = False

while not game_over:
    show_board()
    line = input('Enter a row and column in which to play from 1-3\n Eg: 1,3')
    row = line[0]
    column = line[:-1]
    position = convert_position(row, column)

    if is_valid_move(position):
        board[position] = mark
    make_move(position)
    print("Waiting for opponent move...")
    receive_move()
    game_over = is_game_over()

if victory:
    print("VICTORY")
else:
    print("You Lose...")
