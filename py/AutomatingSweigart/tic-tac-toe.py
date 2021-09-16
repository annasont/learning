""" Tic-tac-toe game"""

board = ['top-L', 'top-M', 'top-R', 'mid-L', 'mid-M', 'mid-R', 'low-L', 'low-M', 'low-R']

myBoard = {}

for position in board:
    myBoard.setdefault(position, '  ')

def showBoard():
    print(myBoard['top-L'] + '|' + myBoard['top-M'] + '|' + myBoard['top-R'] + '\n -+-+- \n' +
        myBoard['mid-L'] + '|' + myBoard['mid-M'] + '|' + myBoard['mid-R'] + '\n -+-+- \n' +
        myBoard['low-L'] + '|' + myBoard['low-M'] + '|' + myBoard['low-R'])



player = 1
for i in range(9):
    print('Where do you want to place your mark?')
    turn = input()
    if player == 1:
        myBoard[turn] = 'X'
        player = 2
    elif player == 2:
        myBoard[turn] = 'O'
        player = 1  
    
    print(showBoard())
 

