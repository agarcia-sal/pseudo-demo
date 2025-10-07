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

    idx = 1
    root = TreeNode(val=values[0])
    q = deque()
    q.append(root)

    while q:
        current = q.popleft()

        if idx < len(values):
            if values[idx] is not None:
                current.left = TreeNode(val=values[idx])
                q.append(current.left)
            idx += 1

        if idx < len(values):
            if values[idx] is not None:
                current.right = TreeNode(val=values[idx])
                q.append(current.right)
            idx += 1

    return root

def is_same_tree(p, q):
    if p is None:
        return q is None
    if q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def minimumLevel(self, root):
        if root is None:
            return 0

        q = deque([root])
        min_level = 1
        min_sum = inf
        level = 1

        while q:
            level_sum = 0
            nodes_count = len(q)
            count = 0
            while count < nodes_count:
                current = q.popleft()
                level_sum += current.val
                if current.left is not None:
                    q.append(current.left)
                if current.right is not None:
                    q.append(current.right)
                count += 1

            if level_sum < min_sum:
                min_sum = level_sum
                min_level = level
            level += 1

        return min_level