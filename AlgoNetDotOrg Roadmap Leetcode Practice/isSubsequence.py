"""
    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

    Meaning it has to go in order as well.
"""


s = "abc"
t = "ahbgdc"


def isSubsequence(s, t):
    t = list(t)
    s = list(s)

    i = 0
    j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            print(f"Letter {s[i]} match at i = {i} and j = {j}")
            i += 1
            j += 1
        else:
            print(f"Letter {s[i]} not found at j = {j}")
            j += 1
    if i < len(s):
        return False
    return True


print(isSubsequence(s, t))
