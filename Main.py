# Noughts and cross game where one instance chooses to act as the server and the other as the client.

isServer = input('Act as server? (Y/N):\n').upper() == "Y"

board = []

# Setup connections and wait for client to join
if isServer:
    pass

# attempt to join server
else:
    pass


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

board = [0,0,0,
         0,0,0,
         0,0,0]

#show board and ask for a row and a column to play in
showBoard()
line = input('Enter a row and column in which to play from 1-3\n Eg: 1,3')
row = line[0]
column = line[:-1]

if isValidMove(row,column):
    pass