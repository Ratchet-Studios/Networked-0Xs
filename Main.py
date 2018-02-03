import socket

# Noughts and cross game where one instance chooses to act as the server and the other as the client.

isServer = input('Act as server? (Y/N):\n').upper() == "Y"

if isServer:
    my_player_number = 1
    opponent_player_number = 2
else:
    my_player_number = 2
    opponent_player_number = 2

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
    
    print("Another player connected")

# attempt to join server
else:
    
    address = input("Enter server address: ")
    
    # create an INET, STREAMing socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # now connect to the web server on port 80 - the normal http port
    print("Connecting to server")
    client_socket.connect(('localhost', 4444))

def makeMove(position):
    board[position] = my_player_number
    client_socket.send(position)

def receiveMove():
    receivedMove = client_socket.recv()
    board[receivedMove] = opponent_player_number
    
    
# Luc Game
# Board Layout:
#    0 1 2
# 0  0|1|2
# 1  3|4|5
# 2  6|7|8

def showBoard():
    print('x|o|x')
    print('o|x|o')
    print('x|o|x')

def isValidMove(position):
    return board[position]==0

def convertPosition(row,column):
    return row*3+column

#board above


#show board and ask for a row and a column to play in
showBoard()
line = input('Enter a row and column in which to play from 1-3\n Eg: 1,3')
row = line[0]
column = line[:-1]

if isValidMove(row,column):
    pass