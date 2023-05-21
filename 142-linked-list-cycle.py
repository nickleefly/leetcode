# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Initialize two pointers: slow and fast
        slow = head
        fast = head

        # Iterate through the linked list while both pointers are not None and the fast pointer can move two steps at a time
        while fast and fast.next:
            # Move the slow pointer one step forward
            slow = slow.next

            # Move the fast pointer two steps forward
            fast = fast.next.next

            # If the two pointers meet at some point, then there is a cycle in the linked list
            if slow == fast:
                return True

        # If the fast pointer reaches the end of the linked list, then there is no cycle
        return False
