"""
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true

    Example 2:

    Input: s = "rat", t = "car"
    Output: false
"""


def solution(s, t):
    """
    So what we can do is, lets first compare the length of both the things, if they are equal then only we will move forward
    Then we will make a dictionry with the count of both the things, if both are equal, then we return True else false

    """

    if len(s) != len(t):
        return False

    counter_s = dict()
    counter_t = dict()

    for letter in s:
        counter_s[letter] = counter_s.get(letter, 0) + 1

    for letter in t:
        counter_t[letter] = counter_t.get(letter, 0) + 1

    if counter_t == counter_s:
        return True

    return False


s = "aacc"
t = "ccac"

print(solution(s, t))
