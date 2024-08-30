"""
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.

    Example 1:

    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
    Example 2:

    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

"""


arr = [1, 2, 3, 4]


def brute_force_solution(nums):
    # brute force approach
    solution = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(len(nums)):
            solution[i] *= nums[j] if i != j else 1

    return solution


def left_product(nums):
    left = [1] * len(nums)
    for i in range(1, len(nums)):
        left[i] = left[i - 1] * nums[i - 1]

    return left


def right_product(nums):
    right = [1] * len(nums)
    for i in reversed(range(0, len(nums) - 1)):
        right[i] = right[i + 1] * nums[i + 1]

    return right


def solution(nums):
    # left product
    left = [1] * len(nums)
    for i in range(1, len(nums)):
        left[i] = left[i - 1] * nums[i - 1]

    # right product
    right = [1] * len(nums)
    for i in reversed(range(0, len(nums) - 1)):
        right[i] = right[i + 1] * nums[i + 1]

    # solution
    for i in range(len(nums)):
        nums[i] = left[i] * right[i]

    return nums


print(left_product(arr))
print(right_product(arr))
print(solution(arr))
