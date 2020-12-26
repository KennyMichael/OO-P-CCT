# defining global variables
# the board is a list with 10 spaces to allow for 1-9 as positions, 0 will not be playable
# empty board spaces are populated with a ' '
board = [' '] * 10


# intro function welcomes the player, and displays the playable positions on the board
def intro():
    print('Welcome to tic-tac-toe!')
    print('Here is the layout of the board:')
    print(' 1 ┃ 2 ┃ 3')
    print('━━━━━━━━━━━')
    print(' 4 ┃ 5 ┃ 6')
    print('━━━━━━━━━━━')
    print(' 7 ┃ 8 ┃ 9\n')


# function to print out current state of the board
def printBoard(board):
    print(' ' + board[1] + ' ┃ ' + board[2] + ' ┃ ' + board[3])
    print('━━━━━━━━━━━')
    print(' ' + board[4] + ' ┃ ' + board[5] + ' ┃ ' + board[6])
    print('━━━━━━━━━━━')
    print(' ' + board[7] + ' ┃ ' + board[8] + ' ┃ ' + board[9])


# function to place X or O in desired position
def placeMove(letter, place):
    board[place] = letter


# function to check if the chose position has been filled. Positions start with ' '
def checkFree(place):
    if board[place] == ' ':
        return True
    else:
        return False


def isBoardFull(board):  # checking if there is more than 1 black space in the list of entries
    if board.count(' ') > 1:
        return False
    else:
        return True


# function takes 2 inputs, the board and either an X or an O and checks if the board contains a completed row
# board[i] gives the current character in that position of the board, and checks if it is the same as the given letter X or O
def rowComplete(board, let):
    if ((board[7] == let and board[8] == let and board[9] == let) or (board[4] == let and board[5] == let and board[6] == let) or (board[1] == let and board[2] == let and board[3] == let) or (board[7] == let and board[4] == let and board[1] == let) or (
            board[8] == let and board[5] == let and board[2] == let) or (board[9] == let and board[6] == let and board[3] == let) or (board[7] == let and board[5] == let and board[3] == let) or (board[9] == let and board[5] == let and board[1] == let)):
        return True  # if there is a completed row function returns True

    else:
        return False  # if there is no completed row the function returns false


# this function takes the players move, checks if it is valid, and places it on the baord if it is
def playerMove():
    loop = True  # loop over conditions for player move until move is acceptable
    while loop:
        # move taken by user input, 1 - 9 for positions on board
        move = input('Please enter a move from 1 - 9: ')
        try:
            move = int(move)  # try block tests that players choice is an int
            if move in range(1, 10):
                if checkFree(move):  # calls check free function to see if that space is playable
                    loop = False     # if the space is free, and in the range of allowable moves, the loop will end
                    # placeMove function adds the players letter 'X' to the board
                    placeMove('X', move)
                else:
                    # if checkFree returns false, and loop returns to asking player for another move
                    print('This space is taken')
            else:
                # if the move is not in the requested range, the player is prompted to make another move
                print('Please enter a number from 1 - 9: ')
        except:
            # if the players move is not an int, the error message shows and loop restarts to request a new move
            print('Please enter an integer')


# AI function to make computers move
def compMove():
    availableMoves = []  # Create a list of possible moves
    for i in range(1, 10):
        if board[i] == ' ':  # if there is a space in the list 'board' with the value ' ' it is added to the list of available moves
            availableMoves.append(i)

    move = 0  # default move is 0, if none of the spaces are available the computers move will return as 0

    # Check for possible winning move first, and make that move if possible
    for i in availableMoves:
        # creates copy of the board with a slice, so as not to redefine the variable 'board'
        boardSlice = board[:]
        boardSlice[i] = 'O'
        if rowComplete(boardSlice, 'O'):  # if a complete row can be made, the AI makes that move
            move = i
            return move

    # next the AI checks if the player can win on the next move, using the same logic as above
    # if the player can win, the AI blocks that position
    for i in availableMoves:
        boardSlice = board[:]
        boardSlice[i] = 'X'
        if rowComplete(boardSlice, 'X'):
            move = i
            return move

    # If the AI cannot win, or block a win on the next move, it will try to take the center as it is the best strategic position
    if 5 in availableMoves:
        move = 5
        return move

    # If the AI cannot take the centre, next the AI will try and play a corner
    for i in availableMoves:
        if i in [1, 3, 7, 9]:  # list of corners on board
            move = i
            return move

    # Take any edge as the last option, as it is the least desirable position
    for i in availableMoves:
        if i in [2, 4, 6, 8]:  # list of all edges on board
            move = i
            return move

    return move  # if none of the above positions are available, the function returns the default move, 0


# main function to run program
def main():
    printBoard(board)  # first prints out state of the board

    while not (isBoardFull(board)):  # checks if the board is full
        if not (rowComplete(board, 'O')):  # checking if computer has won
            playerMove()  # player moves first
            printBoard(board)  # board is printed out after each move
        else:
            print('You loose, AI is undeniable')
            break

        if not (rowComplete(board, 'X')):  # checking if human has won
            move = compMove()
            if move == 0:  # computers move defaults to 0 if there is no available moves. If the move returns 0, there is a draw as we have already tested for a winner
                print('Draw')
            else:
                placeMove('O', move)  # 'O' is placed for AI's chosen move
                # tells the AI's chosen move and prints the board
                print('AI played position ', move)
                printBoard(board)
        else:
            print('You win!')  # Winning statement
            break

    if isBoardFull(board):  # if not winner and is full, the game is a draw
        print('Draw')


# calling introduction and main functions to explain and begin the game
intro()
main()

# replay option asks for yes/no input
replay = input('Play again? Y/N ')
replay = replay.upper()
while replay == 'Y':
    board = [' '] * 10  # reset the board for new game
    main()
    replay = input('Play again? Y/N ')
    replay = replay.upper()
