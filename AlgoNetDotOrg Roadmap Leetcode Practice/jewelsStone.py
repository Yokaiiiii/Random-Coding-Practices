"""
    You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

    Letters are case sensitive, so "a" is considered a different type of stone from "A".

    Example 1:

    Input: jewels = "aA", stones = "aAAbbbb"
    Output: 3

    Example 2:

    Input: jewels = "z", stones = "ZZ"
    Output: 0
"""

# So tehinically i need to find the occurance of every letters in the string, and then find the value of that letter
# so lets make a dictionary with key as letter and value as the number of occurance of it in the string, then we can print the added value of the letter
# we need


def solution(jewels, stones):
    counter = {}
    is_there = False
    for stone in stones:
        if stone in jewels:
            is_there = True
        if stone not in counter:
            counter[stone] = 1
        else:
            counter[stone] += 1
    # we just made a dictionary with the letters in it

    count = 0
    if is_there:
        for jewel in jewels:
            if jewel in counter:
                count += counter[jewel]

    return count


jewels = "aA"
stones = "aAABBbb"

print(solution(jewels, stones))
