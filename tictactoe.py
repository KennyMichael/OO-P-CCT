board = [' '] * 10


def intro():
    print('Welcome to tic-tac-toe!')
    print('Here is the layout of the board:')
    print(' 1 ┃ 2 ┃ 3')
    print('━━━━━━━━━━━')
    print(' 4 ┃ 5 ┃ 6')
    print('━━━━━━━━━━━')
    print(' 7 ┃ 8 ┃ 9\n')


def printBoard(board):
    print(' ' + board[1] + ' ┃ ' + board[2] + ' ┃ ' + board[3])
    print('━━━━━━━━━━━')
    print(' ' + board[4] + ' ┃ ' + board[5] + ' ┃ ' + board[6])
    print('━━━━━━━━━━━')
    print(' ' + board[7] + ' ┃ ' + board[8] + ' ┃ ' + board[9])


def placeMove(letter, place):
    board[place] = letter


def checkFree(place):
    if board[place] == ' ':
        return True
    else:
        return False


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def rowComplete(board, let):
    if ((board[7] == let and board[8] == let and board[9] == let) or (board[4] == let and board[5] == let and board[6] == let) or (board[1] == let and board[2] == let and board[3] == let) or (board[7] == let and board[4] == let and board[1] == let) or (
            board[8] == let and board[5] == let and board[2] == let) or (board[9] == let and board[6] == let and board[3] == let) or (board[7] == let and board[5] == let and board[3] == let) or (board[9] == let and board[5] == let and board[1] == let)):
        return True

    else:
        return False


def playerMove():
    loop = True
    while loop:
        move = input('Please enter a move from 1 - 9: ')
        try:
            move = int(move)
            if move in range(1, 10):
                if checkFree(move):
                    loop = False
                    placeMove('X', move)
                else:
                    print('This space is taken')
            else:
                print('Please enter a number from 1 - 9: ')
        except:
            print('Please enter an integer')


def compMove():
    availableMoves = []
    for i in range(1, 10):
        if board[i] == ' ':
            availableMoves.append(i)

    move = 0

    for i in availableMoves:
        boardSlice = board[:]
        boardSlice[i] = 'O'
        if rowComplete(boardSlice, 'O'):
            move = i
            return move

    for i in availableMoves:
        boardSlice = board[:]
        boardSlice[i] = 'X'
        if rowComplete(boardSlice, 'X'):
            move = i
            return move

    if 5 in availableMoves:
        move = 5
        return move

    for i in availableMoves:
        if i in [1, 3, 7, 9]:
            move = i
            return move

    for i in availableMoves:
        if i in [2, 4, 6, 8]:
            move = i
            return move

    return move


def main():
    printBoard(board)

    while not (isBoardFull(board)):
        if not (rowComplete(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('You loose, AI is undeniable')
            break

        if not (rowComplete(board, 'X')):
            move = compMove()
            if move == 0:
                print('Draw')
            else:
                placeMove('O', move)
                print('AI played position ', move)
                printBoard(board)
        else:
            print('You win!')
            break

    if isBoardFull(board):
        print('Draw')


intro()
main()
