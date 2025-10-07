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
    index = 1
    container = deque([root])

    def try_push_child(node, idx):
        if idx < len(values) and values[idx] is not None:
            kid = TreeNode(values[idx])
            if idx % 2 != 0:
                node.left = kid
            else:
                node.right = kid
            container.append(kid)
            return 1
        return 0

    while container:
        curr = container.popleft()
        changed = try_push_child(curr, index)
        index += changed
        changed_right = try_push_child(curr, index)
        index += changed_right

    return root

def is_same_tree(p, q):
    def mutually_null(a, b):
        return a is None and b is None

    def exactly_one_null(a, b):
        return (a is None) ^ (b is None)

    if mutually_null(p, q):
        return True

    if exactly_one_null(p, q):
        return False

    if p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def minimumLevel(self, root):
        if root is None:
            return 0

        q = deque([root])
        best_level = 1
        best_sum = inf
        current_depth = 1

        def has_children(node):
            return node.left is not None or node.right is not None

        while q:
            accum = 0
            level_size = len(q)

            def recurse_process(count, acc):
                if count == 0:
                    return acc
                n = q.popleft()
                acc += n.val
                if n.left is not None:
                    q.append(n.left)
                if n.right is not None:
                    q.append(n.right)
                return recurse_process(count - 1, acc)

            accum = recurse_process(level_size, 0)

            if accum < best_sum:
                best_sum = accum
                best_level = current_depth

            current_depth += 1

        return best_level