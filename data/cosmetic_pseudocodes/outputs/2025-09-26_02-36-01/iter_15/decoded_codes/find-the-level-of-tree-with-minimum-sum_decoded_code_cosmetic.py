from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def tree_node(values):
    if values == []:
        return None
    k = 1
    m = deque()
    root = TreeNode(values[0])
    m.append(root)
    while len(m) > 0:
        w = m.popleft()
        if k < len(values):
            if values[k] is not None:
                w.left = TreeNode(values[k])
                m.append(w.left)
            k += 1
        if k < len(values):
            if values[k] is not None:
                w.right = TreeNode(values[k])
                m.append(w.right)
            k += 1
    return root


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    else:
        if p is None or q is None:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        y = deque()
        y.append(root)
        h = 1
        g = float("inf")
        r = 1
        while len(y) > 0:
            f = 0
            x = 0
            length = len(y)
            while x < length:
                t = y.popleft()
                f += t.val
                if t.left is not None:
                    y.append(t.left)
                if t.right is not None:
                    y.append(t.right)
                x += 1
            if f < g:
                g = f
                h = r
            r += 1
        return h