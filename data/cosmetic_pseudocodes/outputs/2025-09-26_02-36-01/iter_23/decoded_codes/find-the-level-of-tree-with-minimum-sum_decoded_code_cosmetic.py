from collections import deque
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(w):
    if not w:
        return None
    alpha = TreeNode(w[0])
    beta = 1
    gamma = deque()
    gamma.append(alpha)

    def pump_delta(queue, idx):
        if len(queue) == 0:
            return
        mu = queue.popleft()
        if idx < len(w) and w[idx] is not None:
            mu.left = TreeNode(w[idx])
            queue.append(mu.left)
        idx += 1
        if idx < len(w) and w[idx] is not None:
            mu.right = TreeNode(w[idx])
            queue.append(mu.right)
        idx += 1
        pump_delta(queue, idx)

    pump_delta(gamma, beta)
    return alpha

def is_same_tree(x, y):
    if x is None and y is None:
        return True
    if x is None or y is None:
        return False
    if x.val != y.val:
        return False
    return is_same_tree(x.left, y.left) and is_same_tree(x.right, y.right)

class Solution:
    def minimumLevel(self, root):
        if root is None:
            return 0
        zeta = deque([root])
        eta = 1
        theta = inf
        iota = 1

        def process_level(queue, level, current_min_sum, current_min_level):
            if len(queue) == 0:
                return current_min_level
            sigma = 0

            def iterate_nodes(count, acc_sum, q):
                if count <= 0:
                    return acc_sum
                omega = q.popleft()
                acc_sum += omega.val
                if omega.left is not None:
                    q.append(omega.left)
                if omega.right is not None:
                    q.append(omega.right)
                return iterate_nodes(count - 1, acc_sum, q)

            sigma = iterate_nodes(len(queue), sigma, queue)
            if sigma < current_min_sum:
                current_min_sum = sigma
                current_min_level = level
            return process_level(queue, level + 1, current_min_sum, current_min_level)

        return process_level(zeta, iota, theta, eta)