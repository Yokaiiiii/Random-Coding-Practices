"""
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    
    Example 1:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    Example 2:

    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
"""


arr = ["cir", "car"]


"""
"""


def solution(strs):
    min_length = len(strs[0])
    for s in strs:
        min_length = min(len(s), min_length)
    i = 0
    word = strs[0]
    for j in range(min_length):
        letter = word[j]
        print(f"letter = {letter}")
        for s in strs:
            print(f"S[j] = {s[j]}")
            if letter != s[j]:
                return word[:i]
        else:
            print("True")
            i += 1
    return word[:i]


print(solution(arr))
