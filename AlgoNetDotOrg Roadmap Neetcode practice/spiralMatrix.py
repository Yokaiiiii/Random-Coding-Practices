"""
    Given an m x n matrix, return all elements of the matrix in spiral order.

    Example 1:
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4,5]

    Example 2:
    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 
"""
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


def solution(matrix):
    ls = 0  # Left start
    bs = 0  # Bottom start (top boundary)
    le = len(matrix[0]) - 1  # Right end
    be = len(matrix) - 1  # Bottom end (bottom boundary)
    number = len(matrix[0]) * len(matrix)  # Total number of elements
    solution = []
    count = 0

    while count < number:
        # Traverse from left to right along the top boundary
        for i in range(ls, le + 1):
            if count < number:
                solution.append(matrix[bs][i])
                count += 1
        bs += 1

        # Traverse from top to bottom along the right boundary
        for i in range(bs, be + 1):
            if count < number:
                solution.append(matrix[i][le])
                count += 1
        le -= 1

        # Traverse from right to left along the bottom boundary
        for i in reversed(range(ls, le + 1)):
            if count < number:
                solution.append(matrix[be][i])
                count += 1
        be -= 1

        # Traverse from bottom to top along the left boundary
        for i in reversed(range(bs, be + 1)):
            if count < number:
                solution.append(matrix[i][ls])
                count += 1
        ls += 1

    return solution


print(solution(matrix))
