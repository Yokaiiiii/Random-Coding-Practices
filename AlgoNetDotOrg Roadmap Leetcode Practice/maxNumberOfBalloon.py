"""
    Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

    You can use each character in text at most once. Return the maximum number of instances that can be formed.

    Example 1:

    Input: text = "nlaebolko"
    Output: 1

    Example 2:

    Input: text = "loonbalxballpoon"
    Output: 2

    Example 3:

    Input: text = "leetcode"
    Output: 0
"""


def solution(text):
    counter = dict()
    count = 0
    min_count = (len(text)) // len("balloon")
    print(len(text) + 1)
    print(min_count)

    for letter in text:
        counter[letter] = counter.get(letter, 0) + 1

    # print(counter)
    for _ in range(min_count):
        for letter in "balloon":
            if letter in counter and counter[letter] > 0:
                counter[letter] -= 1
                # print(counter)
            else:
                return count
        count += 1
        # print(count)
    return count


text = "krhizmmgmcrecekgyljqkldocicziihtgpqwbticmvuyznragqoyrukzopfmjhjjxemsxmrsxuqmnkrzhgvtgdgtykhcglurvppvcwhrhrjoislonvvglhdciilduvuiebmffaagxerjeewmtcwmhmtwlxtvlbocczlrppmpjbpnifqtlninyzjtmazxdbzwxthpvrfulvrspycqcghuopjirzoeuqhetnbrcdakilzmklxwudxxhwilasbjjhhfgghogqoofsufysmcqeilaivtmfziumjloewbkjvaahsaaggteppqyuoylgpbdwqubaalfwcqrjeycjbbpifjbpigjdnnswocusuprydgrtxuaojeriigwumlovafxnpibjopjfqzrwemoinmptxddgcszmfprdrichjeqcvikynzigleaajcysusqasqadjemgnyvmzmbcfrttrzonwafrnedglhpudovigwvpimttiketopkvqw"

print(solution(text))


def copiedSolution(text):
    d = {}
    for c in text:
        if c in 'ban':
            d[c] = d.get(c, 0) + 2
        elif c in 'lo':
            d[c] = d.get(c, 0) + 1

    if len(d.values()) >= 5:
        return min(d.values()) // 2
    return 0
