"""
    The question goes like
    You are given a list of numbers and you need to find the number which does not repeat.
    eg:
        lst = [1,2,3,7,3,1,2]
        ans = 7
"""


def anotherListMethod():
    def findTheSingleElement(lst):
        temp = []
        for i in lst:
            if i not in temp:
                temp.append(i)
            else:
                temp.remove(i)
        return temp.pop()

    lst = [1, 2, 3, 7, 3, 1, 2]

    ans = findTheSingleElement(lst)

    print(ans)


def findTheSingleElement(values):
    while True:
        temp = values.pop()
        if temp in values:
            pass
        else:
            return temp


lst = [1, 2, 3, 7, 3, 1, 2]

ans = findTheSingleElement(lst)
print(ans)
