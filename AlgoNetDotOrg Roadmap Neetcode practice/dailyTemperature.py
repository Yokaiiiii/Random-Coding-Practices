"""
    Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

    

    Example 1:

    Input: temperatures = [73,74,75,71,69,72,76,73]
    Output: [1,1,4,2,1,1,0,0]
    Example 2:

    Input: temperatures = [30,40,50,60]
    Output: [1,1,1,0]
    Example 3:

    Input: temperatures = [30,60,90]
    Output: [1,1,0]
 
"""


def solution(temperatures):
    n = len(temperatures)
    stack = []
    answer = [0] * n

    for i in range(n):
        print(stack)
        print(answer)
        if stack == []:
            stack.append((temperatures[i], i))
        elif stack[-1][0] > temperatures[i]:
            stack.append((temperatures[i], i))
        else:
            while stack != []:
                if stack[-1][0] < temperatures[i]:
                    answer[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                else:
                    stack.append((temperatures[i], i))
                    break
            else:
                stack.append((temperatures[i], i))
    return answer


print(solution([73, 74, 75, 71, 69, 72, 76, 73]))
