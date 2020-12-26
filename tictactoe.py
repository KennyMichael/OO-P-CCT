# # board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# board = [' ', 'O', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' ', ]


# def printBoard(board):
#     print(' ' + board[1] + ' ┃ ' + board[2] + ' ┃ ' + board[3])
#     print('━━━━━━━━━━━')
#     print(' ' + board[4] + ' ┃ ' + board[5] + ' ┃ ' + board[6])
#     print('━━━━━━━━━━━')
#     print(' ' + board[7] + ' ┃ ' + board[8] + ' ┃ ' + board[9])


# def isWinner(bo, le):
#     if ((bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[7] == le and bo[4] == le and bo[1] == le) or (bo[8] == le and bo[5] == le and bo[2] == le) or (bo[9] == le and bo[6] == le and bo[3] == le) or (bo[7] == le and bo[5] == le and bo[3] == le) or (bo[9] == le and bo[5] == le and bo[1] == le)):
#         print('Row completed, winner')
#     else:
#         print('No completed row')


# printBoard(board)
# isWinner(board, 'X')

def placeMove(letter, place):
    board[place] = letter


def playerMove():
    loop = True
    while loop:
        move = input('Please enter a move from 1 - 9: ')
        move = int(move)
        if move in range(1, 10):
            loop = False    # loop to prompt again if the user input is not in desired range
            placeMove('X', move)
