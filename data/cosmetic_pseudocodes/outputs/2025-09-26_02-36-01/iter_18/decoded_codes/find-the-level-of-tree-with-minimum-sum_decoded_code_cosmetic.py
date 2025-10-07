from collections import deque
from math import inf
from typing import Optional

class TreeNode:
    def __init__(self, alpha: int = 0, bravo: Optional['TreeNode'] = None, charlie: Optional['TreeNode'] = None):
        self.val = alpha
        self.left = bravo
        self.right = charlie

def tree_node(beta: list) -> Optional[TreeNode]:
    if beta is None or len(beta) == 0:
        return None
    root = TreeNode(beta[0])
    queue = deque([root])
    index = 1
    while queue:
        current = queue.popleft()
        if index < len(beta) and beta[index] is not None:
            current.left = TreeNode(beta[index])
            queue.append(current.left)
        index += 1
        if index < len(beta) and beta[index] is not None:
            current.right = TreeNode(beta[index])
            queue.append(current.right)
        index += 1
    return root

def is_same_tree(hotel: Optional[TreeNode], india: Optional[TreeNode]) -> bool:
    if hotel is None and india is None:
        return True
    if hotel is None or india is None:
        return False
    if hotel.val != india.val:
        return False
    return is_same_tree(hotel.left, india.left) and is_same_tree(hotel.right, india.right)

class Solution:
    def minimumLevel(self, kilo: 'Solution', lima: Optional[TreeNode]) -> int:
        if lima is None:
            return 0
        queue = deque([lima])
        level = 1
        min_sum = inf
        min_level = 1
        while queue:
            level_sum = 0
            level_length = len(queue)
            for _ in range(level_length):
                node = queue.popleft()
                level_sum += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if level_sum < min_sum:
                min_sum = level_sum
                min_level = level
            level += 1
        return min_level