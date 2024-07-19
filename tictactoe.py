import os

# Function to initialize the game board with empty spaces


def initializeBoard():
    return [[" " for _ in range(3)] for _ in range(3)]

# Function to display the game board


def display_board(board):
    os.system("cls||clear")  # Clear the console for a fresh display
    i = 0
    for row in board:
        i += 1
        # Join the row elements with ' | ' for better display
        print(" | ".join(row))
        if i != 3:
            print("-" * 10)  # Print a separator between rows
    print()

# Function to check if a move is valid


def isValidMove(moves, board):
    # Check for out-of-bound moves
    if (moves[0] > 2) or (moves[1] > 2):
        return False
    else:
        # Check if the selected cell is empty
        if (board[moves[0]][moves[1]] == " "):
            return True
        else:
            return False

# Function to handle player's move


def playerMove(board, player):
    isValid = False
    while not isValid:
        move = input(
            f"Player {player}, please enter your move (row and column separated by space): ")
        move = move.split(" ")  # Split the input into row and column
        move = [int(i) for i in move]  # Convert the input to integers
        if isValidMove(move, board):
            # If the move is valid, place the player's marker on the board
            board[move[0]][move[1]] = player
            isValid = True
        else:
            print(
                "Your input was out of bound or the cell is already occupied, please enter again")

# Function to check if the current player has won


def checkWinCondition(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # First row
        [board[1][0], board[1][1], board[1][2]],  # Second row
        [board[2][0], board[2][1], board[2][2]],  # Third row
        [board[0][0], board[1][0], board[2][0]],  # First column
        [board[0][1], board[1][1], board[2][1]],  # Second column
        [board[0][2], board[1][2], board[2][2]],  # Third column
        # Diagonal from top-left to bottom-right
        [board[0][0], board[1][1], board[2][2]],
        # Diagonal from bottom-left to top-right
        [board[2][0], board[1][1], board[0][2]],
    ]
    # Check if any win condition is met
    return [player, player, player] in win_conditions

# Function to check if the game is a draw


def checkDraw(board):
    for row in board:
        if " " in row:
            return False  # If there's any empty cell, it's not a draw
    return True  # If no empty cells, it's a draw

# Function to handle the main game loop


def playGame():
    board = initializeBoard()  # Initialize the game board
    currentPlayer = "X"  # Start with player 'X'
    while True:
        display_board(board)  # Display the current state of the board

        # Prompt the current player to make a move
        playerMove(board, currentPlayer)

        # Check if the current player has won
        if checkWinCondition(board, currentPlayer):
            display_board(board)
            print(f"Congratulations!!\nPlayer {
                  currentPlayer} has won the game!!")
            break

        elif checkDraw(board):  # Check if the game is a draw
            display_board(board)
            print("It's a draw!!")
            break

        currentPlayer = "O" if currentPlayer == "X" else "X"  # Switch to the other player


playGame()  # Start the game
