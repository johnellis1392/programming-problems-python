
from typing import List, Optional

from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def reorderList(self, head: Optional[ListNode]) -> None:
    #     node = head
    #     nodes = []
    #     while node != None:
    #         nodes.append(node)
    #         node = node.next
    #     n = len(nodes)
    #     for i in range(n//2):
    #         temp = nodes[i].next
    #         nodes[i].next = nodes[n-i-1]
    #         nodes[n-i-1].next = temp
    #     nodes[n//2].next = None

    def reorderList(self, head: Optional[ListNode]) -> None:
        q = deque()
        node = head
        while node != None:
            q.append(node)
            node = node.next
        even = True
        node = None
        while len(q) > 0:
            if even:
                next = q.popleft()
            else:
                next = q.pop()
            even = not even
            if node != None:
                node.next = next
            node = next
        if node != None:
            node.next = None


def make_list(values: List[int]) -> Optional[ListNode]:
    if len(values) == 0:
        return None
    head = ListNode(values[0])
    node = head
    for v in values[1:]:
        node.next = ListNode(v)
        node = node.next
    return head


def from_list(node: Optional[ListNode]) -> List[int]:
    values = []
    while node != None:
        values.append(node.val)
        node = node.next
    return values


def test_reorder_list():
    s = Solution()
    l = make_list([1, 2, 3, 4, 5])
    s.reorderList(l)
    o = from_list(l)
    exp = [1, 5, 2, 4, 3]
    assert exp == o


def test_reorder_list2():
    s = Solution()
    l = make_list([1, 2, 3, 4])
    s.reorderList(l)
    o = from_list(l)
    exp = [1, 4, 2, 3]
    assert exp == o
