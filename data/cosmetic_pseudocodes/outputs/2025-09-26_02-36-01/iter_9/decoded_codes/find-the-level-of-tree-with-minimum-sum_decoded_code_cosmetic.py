from collections import deque
from math import inf

class TreeNode:
    def __init__(self, alpha=0, beta=None, gamma=None):
        self.val = alpha
        self.left = beta
        self.right = gamma

def tree_node(omega):
    if not has_elements(omega):
        return None

    delta = create_node(value_at(omega, 0))
    tau = 1
    sigma = deque_create()
    deque_append(sigma, delta)

    while True:
        if deque_is_empty(sigma):
            break

        mu = deque_popleft(sigma)

        if less_than(tau, collection_length(omega)):
            epsilon = get_element(omega, tau)
            if not_equal(epsilon, None):
                mu.left = create_node(epsilon)
                deque_append(sigma, mu.left)
        tau += 1

        if less_than(tau, collection_length(omega)):
            epsilon = get_element(omega, tau)
            if not_equal(epsilon, None):
                mu.right = create_node(epsilon)
                deque_append(sigma, mu.right)
        tau += 1

    return delta

def is_same_tree(xi, upsilon):
    if both_none(xi, upsilon):
        return True
    if either_none(xi, upsilon):
        return False
    if not_equal(xi.val, upsilon.val):
        return False
    return and_bool(is_same_tree(xi.left, upsilon.left), is_same_tree(xi.right, upsilon.right))

class Solution:
    def minimumLevel(self, phi):
        if equal_none(phi):
            return 0

        kappa_queue = deque_create()
        deque_append(kappa_queue, phi)

        zeta_level = 1
        theta_min_sum = positive_infinity()
        rho_level = 1

        while not deque_is_empty(kappa_queue):
            eta_sum = 0
            xi_counter = 0
            chi_limit = deque_length(kappa_queue)

            # count_loop modifies xi_counter and eta_sum via recursion,
            # to reflect that in Python integers are immutable, we use a list to hold them
            acc = [0]  # to accumulate sum

            def count_loop(limit, index_ref, q, acc_sum_ref):
                def RECURSIVE_HELPER(lim, idx, queue_ref, sum_ref):
                    if idx >= lim:
                        return
                    current_node = deque_popleft(queue_ref)
                    sum_ref[0] += current_node.val
                    if not_equal(current_node.left, None):
                        deque_append(queue_ref, current_node.left)
                    if not_equal(current_node.right, None):
                        deque_append(queue_ref, current_node.right)
                    RECURSIVE_HELPER(lim, idx + 1, queue_ref, sum_ref)
                RECURSIVE_HELPER(limit, index_ref, q, acc_sum_ref)

            count_loop(chi_limit, xi_counter, kappa_queue, acc)
            eta_sum = acc[0]

            if less_than(eta_sum, theta_min_sum):
                theta_min_sum = eta_sum
                zeta_level = rho_level
            rho_level += 1

        return zeta_level

def count_loop(limit, index_ref, q, acc_sum_ref):
    def RECURSIVE_HELPER(lim, idx, queue_ref, sum_ref):
        if idx >= lim:
            return
        current_node = deque_popleft(queue_ref)
        sum_ref[0] += current_node.val
        if not_equal(current_node.left, None):
            deque_append(queue_ref, current_node.left)
        if not_equal(current_node.right, None):
            deque_append(queue_ref, current_node.right)
        RECURSIVE_HELPER(lim, idx + 1, queue_ref, sum_ref)
    RECURSIVE_HELPER(limit, index_ref, q, acc_sum_ref)

def both_none(a, b):
    return equal_none(a) and equal_none(b)

def either_none(a, b):
    return equal_none(a) or equal_none(b)

def equal_none(x):
    return x is None

def not_equal(a, b):
    return not (a == b)

def less_than(a, b):
    return (a - b) < 0

def create_node(value):
    return TreeNode(value)

def has_elements(coll):
    return not (collection_length(coll) == 0)

def value_at(coll, pos):
    return get_element(coll, pos)

def collection_length(coll):
    return len(coll)

def get_element(coll, idx):
    return coll[idx]

def deque_create():
    return deque()

def deque_append(dq, element):
    dq.append(element)

def deque_popleft(dq):
    return dq.popleft()

def deque_is_empty(dq):
    return len(dq) == 0

def deque_length(dq):
    return len(dq)

def and_bool(a, b):
    if a:
        if b:
            return True
        else:
            return False
    else:
        return False

def positive_infinity():
    return inf