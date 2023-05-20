from typing import List
from typing import Optional
from operator import attrgetter
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # def __repr__(self):
    #     if self:
    #         return "{} -> {}".format(self.val, self.next)


class Solution:
    # @param a list of ListNode
    # @return a ListNode
    # Time: O(nlogn) Space: O(1)
    def mergeKLists(self, lists):
        if not lists:
            return None

        return self.merge_range_lists(lists, 0, len(lists) - 1)

    def merge_range_lists(self, lists, start, end):
        if start == end:
            return lists[start]

        mid = (start + end) // 2
        left = self.merge_range_lists(lists, start, mid)
        right = self.merge_range_lists(lists, mid + 1, end)
        return self.merge_two_lists(left, right)

    def merge_two_lists(self, head1, head2):
        tail = dummy = ListNode(0)
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        if head1:
            tail.next = head1
        if head2:
            tail.next = head2

        return dummy.next

    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sorted_list = []
        for head in lists:
            curr = head
            while curr is not None:
                sorted_list.append(curr)
                curr = curr.next

        sorted_list = sorted(sorted_list, key=attrgetter('val'))
        for i, node in enumerate(sorted_list):
            try:
                node.next = sorted_list[i + 1]
            except:
                node.next = None

        if sorted_list:
            return sorted_list[0]
        else:
            return None

    # Building the new list with just the values from the old ones,
    # leaving the old lists intact
    def mergeKLists2(self, lists):
        def vals(node):
            while node:
                yield node.val
                node = node.next
        dummy = last = ListNode(None)
        for val in heapq.merge(*map(vals, lists)):
            last.next = last = ListNode(val)
        return dummy.next

    # Building the new list with the nodes from the old ones
    def mergeKLists3(self, lists):
        def gen(node):
            while node:
                yield node.val, node
                node = node.next
        dummy = last = ListNode(None)
        for _, last.next in heapq.merge(*map(gen, lists)):
            last = last.next
        return dummy.next

    # def mergeKLists_heap(self, lists: List[ListNode]) -> ListNode:
    """
    1, Take the first node of each of the linked lists
    and add it into a heap. When you add it to the heap
    add (node.val, i) where i is the ith list.

    2, Create a dummy node head.

    3, Pop the first node from the heap and make it the
    next node in the dummy-list. Remember to add the
    first node from the ith linked list into the heap
    since we just removed a node from this list from the heap.

    4, Repeat until the heap is empty.
    Time Complexity: O(n·log(m)) where n is the total number of elements and m is the number of lists
    Space Complexity: O(n)
    """

    def mergeKLists_heap(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = ListNode(None)
        curr = head
        h = []
        for i in range(len(lists)):
            # print('list[%d] is %s' % (i, lists[i].val))
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next

        while h:
            val, i = heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next

        return head.next

    def mergeKLists_Python3(self, lists):
        ListNode.__eq__ = lambda self, other: self.val == other.val
        ListNode.__lt__ = lambda self, other: self.val < other.val
        h = []
        head = tail = ListNode(0)
        for i in lists:
            if i:
                heapq.heappush(h, (i.val, i))

        while h:
            node = heapq.heappop(h)[1]
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(h, (node.next.val, node.next))

        return head.next

    def mergeKLists_heapq1(self, lists):
        h = []
        head = tail = ListNode(0)
        for i in range(len(lists)):
            heapq.heappush(h, (lists[i].val, i, lists[i]))

        while h:
            node = heapq.heappop(h)
            node = node[2]
            tail.next = node
            tail = tail.next
            if node.next:
                i += 1
                heapq.heappush(h, (node.next.val, i, node.next))

        return head.next


if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(4)
    list1.next.next = ListNode(5)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    list3 = ListNode(2)
    list3.next = ListNode(6)
    # print(Solution().mergeKLists1([list1, list2, list3]))
    print(Solution().mergeKLists_heapq1([list1, list2, list3]))
