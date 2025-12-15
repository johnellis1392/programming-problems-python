from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val
        q = []
        def push(x): return x != None and heapq.heappush(q, x)
        def pop(): return heapq.heappop(q)

        for n in lists:
            push(n)
        if len(q) == 0:
            return None

        head = pop()
        prev = head
        push(head.next)
        while len(q) > 0:
            node = pop()
            prev.next = node
            if node == None:
                continue
            if node.next != None:
                push(node.next)
            prev = node
        prev.next = None
        ListNode.__lt__ = None
        return head


def make_list(values: List[int]) -> Optional[ListNode]:
    if len(values) == 0:
        return None
    head = ListNode(values[0])
    node = head
    for v in values[1:]:
        node.next = ListNode(v)
        node = node.next
    return head


def unmake_list(head: ListNode) -> List[int]:
    node = head
    res = []
    while node != None:
        res.append(node.val)
        node = node.next
    return res


def test_merge_k_lists():
    inputs = list(map(make_list, [[1, 4, 5], [1, 3, 4], [2, 6]]))
    exp = [1, 1, 2, 3, 4, 4, 5, 6]
    s = Solution()
    actual = s.mergeKLists(inputs)
    actual = unmake_list(actual)
    assert actual == exp

    assert unmake_list(s.mergeKLists([make_list([1])])) == [1]
