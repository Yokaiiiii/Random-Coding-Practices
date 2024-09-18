"""
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.



    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    Example 3:

    Input: nums = [3,3], target = 6
    Output: [0,1]
"""


"""
    Solution done using two pointer
        num_indices = {}
        for i, num in enumerate(nums):
            num_indices[num] = i

        # Sort the list
        nums_sorted = sorted(nums)

        # Initialize two pointers
        left = 0
        right = len(nums) - 1

        # Loop until the pointers meet
        while left < right:
            # Calculate the sum of the current pair
            current_sum = nums_sorted[left] + nums_sorted[right]

            # If the sum equals the target, return the indices
            if current_sum == target:
                return [num_indices[nums_sorted[left]], num_indices[nums_sorted[right]]]

            # If the sum is less than the target, move the left pointer to the right
            elif current_sum < target:
                left += 1

            # If the sum is greater than the target, move the right pointer to the left
            else:
                right -= 1
"""


def solution(nums=[3, 2, 4], target=6):
    dictionary = {}

    for index, num in enumerate(nums):
        compliment = target - num
        if compliment in dictionary:
            return [dictionary[compliment], index]

        dictionary[num] = index

    return []


print(solution())
