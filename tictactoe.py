import os


def initializeBoard():
    return [[" " for _ in range(3)] for _ in range(3)]


def display_board(board):
    os.system("cls||clear")
    i = 0
    for row in board:
        i += 1
        print(" | ".join(row))
        if i != 3:
            print("-" * 10)
    print()


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


def checkWinCondition(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions


def checkDraw(board):
    for row in board:
        if " " in row:
            return False
    return True


def playGame():
    board = initializeBoard()
    currentPlayer = "X"
    while True:
        display_board(board)

        playerMove(board, currentPlayer)

        if checkWinCondition(board, currentPlayer):
            display_board(board)
            print(f"Congratulation!!\nPlayer {
                  currentPlayer} have won the game!!")
            break

        elif checkDraw(board):
            display_board(board)
            print("Its a draw!!")
            break

        currentPlayer = "0" if currentPlayer == "X" else "X"


playGame()
