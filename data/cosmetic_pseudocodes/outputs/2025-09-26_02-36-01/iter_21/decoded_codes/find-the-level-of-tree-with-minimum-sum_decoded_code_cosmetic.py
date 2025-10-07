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

    alpha = TreeNode(values[0])
    bravo = 1
    charlie = deque()
    charlie.append(alpha)

    while charlie:
        delta = charlie.popleft()
        if bravo < len(values) and values[bravo] is not None:
            delta.left = TreeNode(values[bravo])
            charlie.append(delta.left)
        bravo += 1

        if bravo < len(values) and values[bravo] is not None:
            delta.right = TreeNode(values[bravo])
            charlie.append(delta.right)
        bravo += 1

    return alpha

def is_same_tree(p, q):
    def compare_nodes(a, b):
        if a is None:
            return b is None
        if b is None:
            return False
        if a.val != b.val:
            return False
        return compare_nodes(a.left, b.left) and compare_nodes(a.right, b.right)
    return compare_nodes(p, q)

class Solution:
    def minimumLevel(self, root):
        def add_if_not_none(q, n):
            if n is not None:
                q.append(n)

        if root is None:
            return 0

        queue = deque([root])
        level_counter = 1
        minimum_sum = inf
        minimum_level = 1

        def process_level(q):
            sum_accumulator = 0
            def process_nodes(count):
                nonlocal sum_accumulator
                if count == 0:
                    return sum_accumulator
                node = q.popleft()
                sum_accumulator += node.val
                add_if_not_none(q, node.left)
                add_if_not_none(q, node.right)
                return process_nodes(count - 1)
            return process_nodes(len(q))

        while queue:
            current_level_sum = process_level(queue)
            if current_level_sum < minimum_sum:
                minimum_sum = current_level_sum
                minimum_level = level_counter
            level_counter += 1

        return minimum_level