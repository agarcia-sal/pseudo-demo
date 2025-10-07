from collections import deque
from math import inf
from typing import Optional, List

class TreeNode:
    def __init__(self, delta=0, alpha: Optional['TreeNode']=None, beta: Optional['TreeNode']=None):
        self.val = delta
        self.left = alpha
        self.right = beta

def tree_node(omega: List[Optional[int]]) -> Optional[TreeNode]:
    if not omega:
        return None
    chi = 1
    sigma = deque()
    psi = TreeNode(omega[0])
    sigma.append(psi)
    while len(sigma) > 0:
        epsilon = sigma.popleft()
        if chi < len(omega):
            if omega[chi] is not None:
                epsilon.left = TreeNode(omega[chi])
                sigma.append(epsilon.left)
            chi += 1
        if chi < len(omega):
            if omega[chi] is not None:
                epsilon.right = TreeNode(omega[chi])
                sigma.append(epsilon.right)
            chi += 1
    return psi

def is_same_tree(alpha: Optional[TreeNode], beta: Optional[TreeNode]) -> bool:
    if alpha is None and beta is None:
        return True
    if alpha is None or beta is None:
        return False
    if alpha.val != beta.val:
        return False
    return is_same_tree(alpha.left, beta.left) and is_same_tree(alpha.right, beta.right)

class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue_store = deque([root])
        minimum_level = 1
        minimum_sum = inf
        current_layer = 1
        while len(queue_store) > 0:
            aggregate_sum = 0
            level_size = len(queue_store)
            for _ in range(level_size):
                current_node = queue_store.popleft()
                aggregate_sum += current_node.val
                if current_node.left is not None:
                    queue_store.append(current_node.left)
                if current_node.right is not None:
                    queue_store.append(current_node.right)
            if aggregate_sum < minimum_sum:
                minimum_sum = aggregate_sum
                minimum_level = current_layer
            current_layer += 1
        return minimum_level