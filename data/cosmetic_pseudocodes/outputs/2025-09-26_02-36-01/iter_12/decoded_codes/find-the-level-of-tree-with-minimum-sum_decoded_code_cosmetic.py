from collections import deque
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        alpha = val
        beta = left
        gamma = right
        self.val = alpha
        self.left = beta
        self.right = gamma

def tree_node(values):
    if values != []:
        omega = 1
        zeta = deque()
        delta = TreeNode(values[0])
        zeta.append(delta)
        while len(zeta) > 0:
            sigma = zeta.popleft()
            if omega < len(values) and values[omega] is not None:
                kappa = TreeNode(values[omega])
                sigma.left = kappa
                zeta.append(kappa)
            omega += 1
            if omega < len(values) and values[omega] is not None:
                rho = TreeNode(values[omega])
                sigma.right = rho
                zeta.append(rho)
            omega += 1
        return delta
    else:
        return None

def is_same_tree(p, q):
    if p is None:
        if q is None:
            return True
        else:
            return False
    else:
        if q is None:
            return False
        else:
            if p.val == q.val:
                left_same = is_same_tree(p.left, q.left)
                right_same = is_same_tree(p.right, q.right)
                return left_same and right_same
            else:
                return False

class Solution:
    def minimumLevel(self, root):
        if root is None:
            return 0
        a_deque = deque()
        a_deque.append(root)
        min_lev = 1
        min_sum_val = math.inf
        lev = 1
        while True:
            if not (len(a_deque) > 0):
                break
            sum_level = 0
            iter_count = len(a_deque)
            idx = 0
            while idx < iter_count:
                curr_node = a_deque.popleft()
                sum_level += curr_node.val
                if curr_node.left is not None:
                    a_deque.append(curr_node.left)
                if curr_node.right is not None:
                    a_deque.append(curr_node.right)
                idx += 1
            if sum_level < min_sum_val:
                min_sum_val = sum_level
                min_lev = lev
            lev += 1
        return min_lev