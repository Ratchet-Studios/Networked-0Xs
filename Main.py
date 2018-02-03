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
    server_socket.bind((socket.gethostname(), 4444))
    # become a server socket
    server_socket.listen(1)
    
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
    client_socket.connect((address, 4444))

def makeMove(position):
    board[position] = my_player_number
    client_socket.send(position)

def receiveMove():
    receivedMove = client_socket.recv()
    board[receivedMove] = opponent_player_number
    
    
# Luc Game

def showBoard():
    print('\t|\t|\t\n'*3)


board = []
