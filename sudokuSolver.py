
# grid = [
#     [0, 8, 0, 2, 9, 0, 0, 7, 0],
#     [0, 0, 0, 0, 3, 0, 0, 0, 0],
#     [0, 0, 2, 0, 0, 0, 0, 0, 6],
#     [8, 0, 0, 0, 0, 0, 0, 0, 9],
#     [5, 0, 0, 0, 0, 0, 7, 8, 1],
#     [0, 0, 0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 9, 0, 0, 0, 0, 0],
#     [0, 0, 4, 0, 0, 6, 8, 0, 0],
#     [0, 0, 3, 0, 1, 5, 6, 0, 0],
# ]


# def is_valid_move(grid, row, col, number):
#     """
#     Checks if placing a number at a specific cell is valid.
#     """
#     # Check the row for duplicate numbers
#     for i in range(9):
#         if number == grid[row][i]:
#             return False

#     # Check the column for duplicate numbers
#     for i in range(9):
#         if number == grid[i][col]:
#             return False

#     # Check the 3x3 subgrid for duplicate numbers
#     corner_row = row - row % 3  # Determine the starting row of the 3x3 subgrid
#     corner_col = col - col % 3  # Determine the starting column of the 3x3 subgrid

#     # Iterate through the 3x3 subgrid
#     for i in range(3):
#         for j in range(3):
#             if grid[corner_row + i][corner_col + j] == number:
#                 return False

#     # If no duplicates are found, the move is valid
#     return True


# def solver(grid, row, col):
#     """
#     Solves the Sudoku puzzle using backtracking.
#     """
#     # Base condition: If we reach the end of a row, move to the next row
#     if col == 9:
#         if row == 8:  # If we reach the last cell
#             return True
#         row += 1
#         col = 0  # Start from the first column of the next row

#     # If the current cell is already filled, move to the next cell
#     if grid[row][col] > 0:
#         return solver(grid, row, col + 1)

#     # Try placing digits from 1 to 9 in the current cell
#     for num in range(1, 10):
#         if is_valid_move(grid, row, col, num):
#             grid[row][col] = num  # Place the number in the cell

#             # Recursively solve the rest of the grid
#             if solver(grid, row, col + 1):
#                 return True

#             # If placing the number did not lead to a solution, backtrack
#             grid[row][col] = 0

#     # If no number can be placed, return False to indicate failure
#     return False


# # Attempt to solve the problem grid and print the result
# if solver(grid, 0, 0):
#     print("Solved Sudoku Grid:")
#     # Print the solved grid
#     for row in grid:
#         print(" ".join(map(str, row)))

# else:
#     print("No solution exists.")


# solver.py
def solve(bo):
    """
    Solves a sudoku board using backtracking
    :param bo: 2d list of ints
    :return: solution
    """
    find = find_empty(bo)
    if find:
        row, col = find
    else:
        return True

    for i in range(1, 10):
        if valid(bo, (row, col), i):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, pos, num):
    """
    Returns if the attempted move is valid
    :param bo: 2d list of ints
    :param pos: (row, col)
    :param num: int
    :return: bool
    """

    # Check row
    for i in range(0, len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Col
    for i in range(0, len(bo)):
        if bo[i][pos[1]] == num and pos[1] != i:
            return False

    # Check box

    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def find_empty(bo):
    """
    finds an empty space in the board
    :param bo: partially complete board
    :return: (int, int) row col
    """

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None


def print_board(bo):
    """
    prints the board
    :param bo: 2d List of ints
    :return: None
    """
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j], end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")
