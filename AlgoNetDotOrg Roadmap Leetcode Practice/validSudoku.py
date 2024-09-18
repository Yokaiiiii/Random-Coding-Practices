"""
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
"""

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


def solution(board):
    # lets check for the row
    for row in range(9):
        s = set()
        for col in range(9):
            item = board[row][col]
            if item in s:
                return False
            elif item != ".":
                s.add(item)

    # lets check for the col now

    for col in range(9):
        s = set()
        for row in range(9):
            item = board[row][col]
            if item in s:
                return False
            elif item != ".":
                s.add(item)

    # now checking for the square box
    boxes = [
        (0, 0), (0, 3), (0, 6),
        (3, 0), (3, 3), (3, 6),
        (6, 0), (6, 3), (6, 6),
    ]

    for rows, cols in boxes:
        s = set()
        for row in range(rows, rows + 3):
            for col in range(cols, cols + 3):
                item = board[row][col]
                if item in s:
                    return False
                elif item != ".":
                    s.add(item)
    return True


print(solution(board))
