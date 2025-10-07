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
    root = TreeNode(values[0])
    idx = 1
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if idx < len(values) and values[idx] is not None:
            node.left = TreeNode(values[idx])
            queue.append(node.left)
        idx += 1
        if idx < len(values) and values[idx] is not None:
            node.right = TreeNode(values[idx])
            queue.append(node.right)
        idx += 1
    return root

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    left_eq = is_same_tree(p.left, q.left)
    right_eq = is_same_tree(p.right, q.right)
    return left_eq and right_eq

class Solution:
    def minimumLevel(self, root):
        if root is None:
            return 0
        queue = deque([root])
        minL = 1
        minS = inf
        curL = 1
        while queue:
            sumLvl = 0
            lengthQ = len(queue)
            for _ in range(lengthQ):
                node = queue.popleft()
                sumLvl += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if sumLvl < minS:
                minS = sumLvl
                minL = curL
            curL += 1
        return minL