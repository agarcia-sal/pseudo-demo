from collections import deque
from math import inf

class TreeNode:
    def __init__(self, alpha=0, beta=None, gamma=None):
        self.val = alpha
        self.left = beta
        self.right = gamma

def tree_node(omega):
    if omega == []:
        return None
    phi = TreeNode(omega[0])
    delta = 1
    sigma = deque()
    sigma.append(phi)
    while True:
        if not sigma:
            break
        epsilon = sigma.popleft()
        if delta < len(omega):
            if omega[delta] is not None:
                epsilon.left = TreeNode(omega[delta])
                sigma.append(epsilon.left)
            delta += 1
        if delta < len(omega):
            if omega[delta] is not None:
                epsilon.right = TreeNode(omega[delta])
                sigma.append(epsilon.right)
            delta += 1
    return phi

def is_same_tree(rho, tau):
    if rho is None and tau is None:
        return True
    if rho is None or tau is None:
        return False
    if rho.val != tau.val:
        return False
    return is_same_tree(rho.left, tau.left) and is_same_tree(rho.right, tau.right)

class Solution:
    def minimumLevel(self, zeta):
        if zeta is None:
            return 0
        omega = deque([zeta])
        alpha = 1
        beta = inf
        gamma = 1
        while True:
            if not omega:
                break
            delta = 0
            epsilon = 0
            # Process all nodes at current level
            while delta < len(omega):
                eta = omega.popleft()
                epsilon += eta.val
                if eta.left is not None:
                    omega.append(eta.left)
                if eta.right is not None:
                    omega.append(eta.right)
                delta += 1
            if epsilon < beta:
                beta = epsilon
                alpha = gamma
            gamma += 1
        return alpha