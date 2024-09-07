"""
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
    

    Example 1:

    Input: s = "()"

    Output: true

    Example 2:

    Input: s = "()[]{}"

    Output: true

    Example 3:

    Input: s = "(]"

    Output: false

    Example 4:

    Input: s = "([])"

    Output: true
"""


def solution(s):
    stack = []

    for parenthesis in s:
        if parenthesis == "{":
            stack.append("}")
        elif parenthesis == "[":
            stack.append("]")
        elif parenthesis == "(":
            stack.append(")")
        else:
            if stack and parenthesis == stack[-1]:
                stack.pop()
            else:
                return False
    if stack is []:
        return True

    return False


print(solution("]"))
