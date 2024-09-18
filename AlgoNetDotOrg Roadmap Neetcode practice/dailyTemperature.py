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
    n = len(temperatures)  # Get the number of temperatures
    stack = []  # Initialize an empty stack to keep track of indices
    answer = [0] * n  # Initialize the answer list with zeros

    for i in range(n):
        # While stack is not empty and the current temperature is higher than the temperature at the index stored at the top of the stack
        while stack and temperatures[stack[-1]] < temperatures[i]:
            idx = stack.pop()  # Pop the index from the stack
            answer[idx] = i - idx  # Calculate the number of days until a warmer temperature
        stack.append(i)  # Push the current index onto the stack
    
    return answer  # Return the list of days until a warmer temperature

# Example usage
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(solution(temperatures))  # Outputs: [1, 1, 4, 2, 1, 1, 0, 0]



print(solution([73, 74, 75, 71, 69, 72, 76, 73]))
