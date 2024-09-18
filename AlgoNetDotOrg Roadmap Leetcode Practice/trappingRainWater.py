"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""


def solution(height):
    # first lets make a list of maximum height to the left of the current index
    n = len(height)
    max_left = 0
    left_max_height = []
    for index in range(n):
        left_max_height.append(max_left)
        max_left = max(max_left, height[index])

    # similary, do for the max height to the right as well

    max_right = 0
    right_max_height = []
    for index in reversed(range(n)):
        right_max_height.append(max_right)
        max_right = max(max_right, height[index])

    right_max_height.reverse()

    # now we have both the left max height and right max height at each index
    # now to find the trapped water in each index we need to calculate the min(left_max_height, right_max_height) at each index and subtract it with the heigh of that index,
    # if the value if postive, thats the amount of water in that index, else its 0
    answer = 0
    for index in range(n):
        current_sum = min(
            left_max_height[index], right_max_height[index]) - height[index]
        if current_sum > 0:
            answer += current_sum

    return answer

    # return sum(((min(left_max_height[index], right_max_height[index]) - height[index]) for index in range(n) if (min(left_max_height[index], right_max_height[index]) - height[index]) > 0))


print(solution(height=[4, 2, 0, 3, 2, 5]))
