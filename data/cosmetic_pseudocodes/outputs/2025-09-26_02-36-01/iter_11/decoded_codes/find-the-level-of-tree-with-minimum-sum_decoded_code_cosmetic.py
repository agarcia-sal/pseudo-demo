from collections import deque
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values):
    def make_node(value):
        return TreeNode(val=value)

    if not values:
        return None

    idx_counter = 1
    node_queue = deque()
    root = make_node(values[0])
    node_queue.append(root)

    # Helper functions capture idx_counter by nonlocal usage inside the loop instead of here

    def remove_first(deq):
        return deq.popleft()

    while True:
        if not node_queue:
            break

        current_node = remove_first(node_queue)

        left_node = None
        right_node = None

        if idx_counter < len(values):
            val_left = values[idx_counter]
            if val_left is not None:
                left_node = make_node(val_left)
                node_queue.append(left_node)
            idx_counter += 1

        if idx_counter < len(values):
            val_right = values[idx_counter]
            if val_right is not None:
                right_node = make_node(val_right)
                node_queue.append(right_node)
            idx_counter += 1

        current_node.left = left_node
        current_node.right = right_node

    return root

def is_same_tree(p, q):
    def nodes_none(x, y):
        return (x is None) and (y is None)

    def one_none(x, y):
        return (x is None) or (y is None)

    if nodes_none(p, q):
        return True
    elif one_none(p, q):
        return False
    else:
        val_match = not (p.val != q.val)
        if not val_match:
            return False
        else:
            left_comp = is_same_tree(p.left, q.left)
            right_comp = is_same_tree(p.right, q.right)
            return left_comp and right_comp

class Solution:
    def minimumLevel(self, root):
        def init_deque_with(item):
            dq = deque()
            dq.append(item)
            return dq

        def add_node_if_exists(queue_comma_n, n):
            if n is not None:
                queue_comma_n.append(n)

        if root is None:
            return 0

        node_q = init_deque_with(root)
        current_level = 1
        minimal_level = 1
        minimal_sum = inf

        def sum_level(queue_ref):
            acc_sum = 0
            size = len(queue_ref)

            def recur_sum(accum, rem):
                if rem == 0:
                    return accum
                else:
                    current_node = queue_ref.popleft()
                    new_accum = accum + current_node.val
                    add_node_if_exists(queue_ref, current_node.left)
                    add_node_if_exists(queue_ref, current_node.right)
                    return recur_sum(new_accum, rem - 1)

            return recur_sum(acc_sum, size)

        while True:
            if not node_q:
                break

            level_total = sum_level(node_q)
            if level_total < minimal_sum:
                minimal_sum = level_total
                minimal_level = current_level

            current_level += 1

        return minimal_level