"""
    Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

    Since the result may be very large, so you need to return a string instead of an integer.

    

    Example 1:

    Input: nums = 
    Output: "210"
    Example 2:

    Input: nums = [3,30,34,5,9]
    Output: "9534330"
 
"""


def solution(nums):
    nums = list(map(str, nums))
    print(nums)

    nums.sort(key=lambda x : x * 10, reverse= True)
    print(nums)

    if nums[0] == "0":
        return "0"

    return "".join(nums)
    



nums = [0,00,00000,0]
print(solution(nums))
