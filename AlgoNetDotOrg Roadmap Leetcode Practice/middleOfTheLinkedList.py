"""
    Given the head of a singly linked list, return the middle node of the linked list.

    If there are two middle nodes, return the second middle node.

    

    Example 1:


    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.
    Example 2:

    Input: head = [1,2,3,4,5,6]
    Output: [4,5,6]
    Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""

# Definition for singly-linked list.
import math
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        ptr = head
        count = 0
        while ptr:
            count += 1
            print(count, ptr.val)
            ptr = ptr.next
        
        middle =  int(math.ceil(count/2)) if count % 2 != 0 else count//2 + 1
        print(middle)
        count = 0
        ptr = head
        while ptr:
            count += 1
            print(count, ptr.val)
            if count == middle:
                return ptr
            ptr = ptr.next
    
    def solution(self, head):
        h = t = head
        while h and h.next:
            if h.next.next:
                h = h.next.next
            else:
                h = h.next
            t = t.next
        return t.val


head = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
d = ListNode(5)
e = ListNode(6)
f = ListNode(7)


head.next = a
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

print(Solution().solution(head=head))