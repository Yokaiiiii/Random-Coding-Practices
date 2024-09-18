# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        ptr = head  # Initialize the pointer to the head of the list
        prev = None  # Initialize the previous node as None

        while ptr:
            next_ptr = ptr.next  # Store the next node
            ptr.next = prev  # Reverse the current node's pointer
            prev = ptr  # Move the previous node to the current node
            ptr = next_ptr  # Move to the next node

        return prev  # Return the new head of the reversed list
