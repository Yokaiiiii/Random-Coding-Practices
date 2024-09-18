"""
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

    

    Example 1:

    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
    Example 2:

    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

arr = [[1, 4], [0, 0]]


def solution(intervals):
    # Sort intervals by starting value
    intervals.sort()

    # Initialize left and right bounds with the first interval
    left, right = intervals[0]
    solution = []

    # Iterate over the rest of the intervals
    for i in range(1, len(intervals)):
        current_left, current_right = intervals[i]

        # If there's no overlap, save the current interval and reset bounds
        if current_left > right:
            solution.append([left, right])
            left, right = current_left, current_right
        else:
            # Merge intervals by updating the right bound
            right = max(right, current_right)

    # Append the last merged interval
    solution.append([left, right])

    return solution


print(solution(arr))
