import socket

# Noughts and cross game where one instance chooses to act as the server and the other as the client.

CONST_EMPTY_SPACE_CHARACTER = "_"

isServer = input('Act as server? (Y/N):\n').upper() == "Y"

if isServer:
	my_player_number = "x"
	opponent_player_number = "o"
	mark = "x"
else:
	my_player_number = "o"
	opponent_player_number = "x"
	mark = "o"

board = []

for i in range(0, 9):
	board.append(CONST_EMPTY_SPACE_CHARACTER)

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
	client_socket.connect((address, 4444))


def make_move(position):
	board[position] = my_player_number
	client_socket.send(str(position).encode('ascii'))


def receive_move():
	received_move = int(client_socket.recv(4096).decode('ascii'))
	board[received_move] = opponent_player_number


# Luc Game
# Board Layout:
#    0 1 2
# 0  0|1|2
# 1  3|4|5
# 2  6|7|8

def show_board():
	# print('{}|{}|{}\n'
	#       '- - -\n'
	#       '{}|{}|{}\n'
	#       '- - -\n'
	#       '{}|{}|{}'.format(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))
	print('{} {} {}\n'
	      '{} {} {}\n'
	      '{} {} {}'
	      .format(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))


def is_valid_move(position):
	return board[position] == CONST_EMPTY_SPACE_CHARACTER


def convert_position(row, column):
	return row * 3 + column


def is_game_over():
	global victory
	if (board[0] == board[1] == board[2] != CONST_EMPTY_SPACE_CHARACTER) or (
				board[0] == board[3] == board[6] != CONST_EMPTY_SPACE_CHARACTER) or (
				board[0] == board[4] == board[8] != CONST_EMPTY_SPACE_CHARACTER):
		if board[0] == mark:
			victory = True
		return True
	elif (board[3] == board[4] == board[5] != CONST_EMPTY_SPACE_CHARACTER) or (
				board[1] == board[4] == board[7] != CONST_EMPTY_SPACE_CHARACTER) or (
				board[2] == board[4] == board[6] != CONST_EMPTY_SPACE_CHARACTER):
		if board[4] == mark:
			victory = True
		return True
	elif (board[6] == board[7] == board[8] != CONST_EMPTY_SPACE_CHARACTER) or (
				board[2] == board[5] == board[8] != CONST_EMPTY_SPACE_CHARACTER):
		if board[8] == mark:
			victory = True
		return True
	elif CONST_EMPTY_SPACE_CHARACTER not in board:
		victory = 'draw'
		return True
	else:
		return False


# show board and ask for a row and a column to play in
game_over = False
victory = False

if my_player_number == "o":
	print("Waiting for opponent move...")
	receive_move()
	
show_board()

while not game_over:
	
	valid = False
	while not valid:
		line = input('Enter a row and column in which to play from 1-3 (Eg: 1,3)\n')
		row = int(line[0])
		column = int(line[-1:])
		position = convert_position(row, column)
		
		if is_valid_move(position):
			board[position] = mark
			make_move(position)
			game_over = is_game_over()
			if game_over:
				show_board()
				if victory == 'draw':
					print("You Drew!!!")
				elif victory:
					print('VICTORY')
				else:
					print('You Lose...')
			
				exit(0)
			valid = True
		elif not CONST_EMPTY_SPACE_CHARACTER in board:
			victory = 'draw'
			break
		else:
			print('Invalid move, try again (x,y)')
	show_board()
	print('Waiting for opponent move...')
	receive_move()
	game_over = is_game_over()
	show_board()

if victory == 'draw':
	print("You Drew!!!")
elif victory:
	print('VICTORY')
else:
	print('You Lose...')
