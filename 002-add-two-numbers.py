from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLinkedList(lst):
    head = None
    for val in reversed(lst):
        head = ListNode(val, head)
    return head


def toList(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst


l1 = createLinkedList([2, 4, 3])
l2 = createLinkedList([5, 6, 4])


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = cur = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, cur.next = divmod(carry, 10)
            cur.next = cur = ListNode(cur.next)
        return res.next


if __name__ == '__main__':
    s = Solution()
    print(toList(s.addTwoNumbers(l1, l2)))
