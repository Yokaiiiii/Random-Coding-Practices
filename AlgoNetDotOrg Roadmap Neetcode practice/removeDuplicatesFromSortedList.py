"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:

Input: head = [1,1,2]
Output: [1,2]

Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution(head):
    ptr = head
    while ptr and ptr.next:
        if ptr.val == ptr.next.val:
            ptr.next = ptr.next.next
        else:
            ptr = ptr.next

    ptr = head
    while ptr != None:
        print(ptr.val)
        ptr = ptr.next


head = ListNode(1)
a = ListNode(1)
b = ListNode(2)
# c = ListNode(30)
# d = ListNode(50)
# e = ListNode(70)
# f = ListNode(70)

head.next = a
a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f

solution(head)
