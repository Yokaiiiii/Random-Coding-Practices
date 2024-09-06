"""
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.

    Example 1:

    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

    Example 2:

    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9
"""


def solution(nums):
    if not nums:
        return 0

    nums = sorted(set(nums))  # Remove duplicates and sort the list
    longest_consecutive_sequence = 1
    max_consecutive_length = 1

    for index in range(1, len(nums)):
        if nums[index] == nums[index - 1] + 1:
            longest_consecutive_sequence += 1
        else:
            max_consecutive_length = max(
                max_consecutive_length, longest_consecutive_sequence)
            longest_consecutive_sequence = 1

    return max(max_consecutive_length, longest_consecutive_sequence)


print(solution([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
