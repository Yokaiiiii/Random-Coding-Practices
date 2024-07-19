import os


def display_board(board):
    i = 0
    for row in board:
        i += 1
        print(" | ".join(row))
        if i != 3:
            print("-" * 10)
    print()


def initializeBoard():
    return [[" " for _ in range(3)] for _ in range(3)]


# board = initializeBoard()
# display_board(board)


def isValidMove(moves, board):
    # check for out of bound
    if (moves[0] > 2) or (moves[1] > 2):
        return False
    else:
        if (board[moves[0]][moves[1]] == " "):
            return True
        else:
            return False


def playerMove(board, player):
    isValid = False
    while not isValid:
        move = input(f"Player {player}. please enter your move : ")
        move = move.split(" ")
        move = [int(i) for i in move]
        if isValidMove(move, board):
            # print('In the range')
            board[move[0]][move[1]] = player
            isValid = True
        else:
            print("Your input was out of bound, please enter again")


# board = [[" ", " ", " "], [" ", "X", " "], [" ", " ", " "]]
def playGame():
    board = initializeBoard()
    currentPlayer = "X"
    i = 0
    while i < 5:
        os.system('cls||clear')
        display_board(board)

        playerMove(board, currentPlayer)

        currentPlayer = "0" if currentPlayer == "X" else "X"
        i += 1


playGame()
