"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
"""


from typing import List, Optional
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def to_bytes(self, node: Optional[TreeNode]) -> bytearray:
        if node == None:
            return bytearray()  # Tag is not defined
        res = bytearray()
        tag = 0b001  # Tag is defined
        if node.left != None:
            tag |= 0b100  # Left branch is defined
        if node.right != None:
            tag |= 0b010  # Right branch is defined

        res.append(tag)
        res.extend(node.val.to_bytes(2, 'big', signed=True))
        res.extend(self.to_bytes(node.left))
        res.extend(self.to_bytes(node.right))

        return res

    def from_bytes(self, buf: bytearray) -> Optional[TreeNode]:
        if len(buf) == 0 or buf[0] == 0b000:
            # Null
            return None

        tag = buf.pop(0)
        val = int.from_bytes([buf.pop(0), buf.pop(0)], 'big', signed=True)
        node = TreeNode(val)

        if tag & 0b100 == 0b100:
            # Has Left Branch
            node.left = self.from_bytes(buf)

        if tag & 0b10 == 0b10:
            # Has Right Branch
            node.right = self.from_bytes(buf)

        return node

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.to_bytes(root).hex()

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self.from_bytes(bytearray.fromhex(data))


def make_tree(values: List[int]) -> TreeNode:
    '''
    Trees are defined in a heap-style format, for the child nodes
    of some node at index i are found at 2*i and 2*i+1.
    '''
    if len(values) == 0:
        return None
    tree = TreeNode(values[0])
    nodes = deque()
    nodes.append(tree)
    i = 1
    while len(nodes) > 0 and i < len(values):
        node = nodes.popleft()

        # Create Left Node
        v = values[i]
        if v == None:
            node.left = None
        else:
            node.left = TreeNode(v)
            nodes.append(node.left)
        i += 1

        # Check that we reached the end early
        if i >= len(values):
            continue

        # Create Right Node
        v = values[i]
        if v == None:
            node.right = None
        else:
            node.right = TreeNode(v)
            nodes.append(node.right)
        i += 1

    return tree


def unmake_tree(tree: TreeNode) -> List[int]:
    res = []
    q = deque()
    q.append(tree)
    while len(q) > 0:
        n = q.popleft()
        if n != None:
            res.append(n.val)
            q.append(n.left)
            q.append(n.right)
        else:
            res.append(None)

    while res[-1] == None:
        res.pop()
    return res


def test_make_tree():
    tree = make_tree([1, 2, 3])
    assert tree != None and tree.val == 1
    assert tree.left != None and tree.left.val == 2
    assert tree.right != None and tree.right.val == 3

    data = unmake_tree(tree)
    assert data == [1, 2, 3]

    tree = make_tree([1, 2, 3, None, None, 4, 5])
    assert tree != None and tree.val == 1
    assert tree.left != None and tree.left.val == 2
    assert tree.right != None and tree.right.val == 3
    assert tree.left.left == None and tree.left.right == None
    assert tree.right.left != None and tree.right.left.val == 4 and tree.right.right != None and tree.right.right.val == 5

    data = unmake_tree(tree)
    assert data == [1, 2, 3, None, None, 4, 5]


def test_tree_serde():
    codec = Codec()
    data = [1, 2, 3, None, None, 4, 5]
    root = make_tree(data)
    s = codec.serialize(root)
    d = codec.deserialize(s)
    res = unmake_tree(d)
    assert res == data
