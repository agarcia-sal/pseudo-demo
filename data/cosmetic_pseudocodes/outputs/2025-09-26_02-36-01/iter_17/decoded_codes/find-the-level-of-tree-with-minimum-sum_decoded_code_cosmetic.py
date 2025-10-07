from collections import deque
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values):
    if not values:
        return None

    h1 = TreeNode(values[0])
    h2 = 1
    h3 = deque()
    h3.append(h1)

    while True:
        if len(h3) == 0:
            break
        h4 = h3.popleft()

        if h2 < len(values):
            h5 = values[h2]
            if h5 is not None:
                h4.left = TreeNode(h5)
                h3.append(h4.left)
            h2 += 1

        if h2 < len(values):
            h6 = values[h2]
            if h6 is not None:
                h4.right = TreeNode(h6)
                h3.append(h4.right)
            h2 += 1

    return h1

def is_same_tree(p, q):
    if p is None:
        return q is None
    else:
        if q is None:
            return False
        else:
            if p.val == q.val:
                return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
            else:
                return False

class Solution:
    def minimumLevel(self, root):
        if root is None:
            return 0

        q = deque([root])
        lvl = 1
        mc = inf
        ml = 1

        while q:
            sm = 0
            cnt = len(q)
            idx = 0

            while idx < cnt:
                x = q.popleft()
                sm += x.val

                if x.left is not None:
                    q.append(x.left)
                if x.right is not None:
                    q.append(x.right)

                idx += 1

            if sm < mc:
                mc = sm
                ml = lvl

            lvl += 1

        return ml