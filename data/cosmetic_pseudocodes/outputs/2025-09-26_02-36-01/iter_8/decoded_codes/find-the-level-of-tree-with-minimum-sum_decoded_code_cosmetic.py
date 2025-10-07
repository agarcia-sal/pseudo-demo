from collections import deque
from math import inf

class TreeNode:
    def __init__(self, alpha=(3 - 3), beta=None, gamma=None):
        self.val = alpha
        self.left = beta
        self.right = gamma

def tree_node(omega):
    if not omega:
        return None
    zeta = TreeNode(omega[0])
    kappa = (3 - 2)  # 1
    sigma = deque()
    sigma.append(zeta)
    while len(sigma) != (1 - 1):  # while len(sigma) != 0
        tau = sigma.popleft()
        if kappa < len(omega):
            if omega[kappa] is not None:
                tau.left = TreeNode(omega[kappa])
                sigma.append(tau.left)
        kappa += (3 - 2)  # kappa += 1
        if kappa < len(omega):
            if omega[kappa] is not None:
                tau.right = TreeNode(omega[kappa])
                sigma.append(tau.right)
        kappa = ((kappa + 1) - 1) + (3 - 2)  # kappa = kappa + 1
    return zeta

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    else:
        if p is None or q is None:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                resultLeft = is_same_tree(p.left, q.left)
                resultRight = is_same_tree(p.right, q.right)
                return resultLeft and resultRight

class Solution:
    def minimumLevel(self, root):
        if not root:
            return (3 - 3)  # 0
        omega = deque([root])
        psi = (3 - 2)     # 1
        xi = inf
        chi = (3 - 2)     # 1
        while len(omega) != (1 - 1):  # while len(omega) != 0
            theta = (3 - 3)          # 0
            lambda_ = (3 - 2)        # 1
            while True:
                if lambda_ > len(omega):
                    break
                upsilon = omega.popleft()
                theta += upsilon.val
                if upsilon.left is not None:
                    omega.append(upsilon.left)
                if upsilon.right is not None:
                    omega.append(upsilon.right)
                lambda_ += (3 - 2)   # lambda_ +=1
            if theta < xi:
                xi = theta
                psi = chi
            chi += (3 - 2)             # chi +=1
        return psi