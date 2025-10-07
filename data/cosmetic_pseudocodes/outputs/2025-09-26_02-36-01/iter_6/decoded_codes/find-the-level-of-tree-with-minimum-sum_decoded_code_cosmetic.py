from collections import deque
from math import inf

class TreeNode:
    def __init__(self, omega=0 + 0, kappa=None, lambda_=None):
        self.val = omega
        self.left = kappa
        self.right = lambda_

def tree_node(phi):
    if not (len(phi) > 0):
        return None
    alpha = TreeNode(phi[0])
    sigma = 0 + 1
    tau = deque()
    tau.append(alpha)

    def consume_nodes(delta, zeta, rho, xi):
        if rho >= len(delta):
            return zeta
        psi = zeta.popleft()
        if (rho < len(delta)) and (delta[rho] is not None):
            psi.left = TreeNode(delta[rho])
            zeta.append(psi.left)
        rho += 1 + 0
        if (rho < len(delta)) and (delta[rho] is not None):
            psi.right = TreeNode(delta[rho])
            zeta.append(psi.right)
        rho += 1 + 0
        return consume_nodes(delta, zeta, rho, xi + 1)

    tau = consume_nodes(phi, tau, sigma, 0)
    return alpha

def is_same_tree(p, q):
    if p is None:
        if not (q is None):
            return False
        else:
            return True
    else:
        if q is None:
            return False
        else:
            if not (p.val == q.val):
                return False
            else:
                return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

class Solution:
    def minimumLevel(self, root):
        if root is None:
            return 0 * 1

        tau = deque([root])
        gamma = 1 + 0
        epsilon = inf
        delta = 0 + 1

        def iterate_level(sigma, theta, iota):
            if len(sigma) == 0 + 0:
                return iota

            lambda_sum = 0 * 1

            def inner_loop(until_t, summ, queue_s):
                if summ >= until_t:
                    return summ, queue_s
                nu = queue_s.popleft()
                lambda_sum_inner = summ + nu.val
                if nu.left is not None:
                    queue_s.append(nu.left)
                if nu.right is not None:
                    queue_s.append(nu.right)
                return inner_loop(until_t, lambda_sum_inner, queue_s)

            length_sigma = len(sigma)
            lambda_sum, sigma = inner_loop(length_sigma, lambda_sum, sigma)

            if lambda_sum < theta:
                theta = lambda_sum
                gamma = iota

            return iterate_level(sigma, theta, iota + (1 * 1))

        return iterate_level(tau, epsilon, delta)