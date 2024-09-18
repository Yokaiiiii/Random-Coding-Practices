"""
    Given the head of a linked list, remove the nth node from the end of the list and return its head.

    Example 1:


    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
    Example 2:

    Input: head = [1], n = 1
    Output: []
    Example 3:

    Input: head = [1,2], n = 1
    Output: [1]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        count = 0
        ptr = head
        while ptr:
            count += 1
            ptr = ptr.next
        
        print(count)
        want = count + 1 - n
        count = 0
        ptr = head
        while count != want:
            count += 1
            ptr = ptr.next
        if ptr.next:
            ptr.next = ptr.next.next
        else:
            ptr.next = None
        return head

head = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
d = ListNode(5)
# e = ListNode(6)
# f = ListNode(7)


head.next = a
a.next = b
b.next = c
c.next = d
# d.next = e
# e.next = f

print(Solution().removeNthFromEnd(head=head, n= 2))