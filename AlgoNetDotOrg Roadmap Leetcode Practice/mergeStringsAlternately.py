"""
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

    Return the merged string.
"""

word1 = "hello"
word2 = "world"

# hweolrllod234


def merge_words(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    result = []

    min_len = min(len1, len2)
    for i in range(min_len):
        result.append(word1[i])
        result.append(word2[i])

    if len1 > len2:
        result.extend(word1[min_len:])
    else:
        result.extend(word2[min_len:])

    return ''.join(result)


print(merge_words(word1, word2))
