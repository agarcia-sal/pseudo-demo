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
    queue = deque([root])
    index = 1
    while queue:
        current = queue.popleft()
        if index < len(values) and values[index] is not None:
            current.left = TreeNode(values[index])
            queue.append(current.left)
        index += 1
        if index < len(values) and values[index] is not None:
            current.right = TreeNode(values[index])
            queue.append(current.right)
        index += 1
    return root

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    left_check = is_same_tree(p.left, q.left)
    right_check = is_same_tree(p.right, q.right)
    return left_check and right_check

class Solution:
    def minimumLevel(self, root):
        if root is None:
            return 0
        queue = deque([root])
        minimal_level = 1
        minimal_sum = inf
        current_level = 1
        while queue:
            current_sum = 0
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                current_sum += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if current_sum < minimal_sum:
                minimal_sum = current_sum
                minimal_level = current_level
            current_level += 1
        return minimal_level