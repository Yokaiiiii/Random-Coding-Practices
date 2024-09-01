"""
    Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.

    Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false

    Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false

    Example 3:
    Input: ransomNote = "aa", magazine = "aab"
    Output: true
"""
# again, lets make a dictionry with all the letter in magazine and its count, then compare it with ransomnote, and subtract the count, if its value is 0 or not available then we return false, else return True


def solution(ransomNote, magazine):
    counter = dict()
    for letter in magazine:
        counter[letter] = counter.get(letter, 0) + 1

    for letter in ransomNote:
        if letter in counter and counter[letter] > 0:
            counter[letter] -= 1
        else:
            return False

    return True


ransomNote = "a"
magazine = "ab"

print(solution(ransomNote, magazine))
