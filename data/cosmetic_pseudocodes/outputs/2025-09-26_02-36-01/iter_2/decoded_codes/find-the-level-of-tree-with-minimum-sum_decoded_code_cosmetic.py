from collections import deque
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(vals):
    if vals == []:
        return None
    root_node = TreeNode(vals[0])
    index = 1
    to_visit = deque()
    to_visit.append(root_node)
    while len(to_visit) > 0:
        current_node = to_visit.popleft()
        if index < len(vals):
            if vals[index] is not None:
                left_child = TreeNode(vals[index])
                current_node.left = left_child
                to_visit.append(left_child)
            index += 1
        if index < len(vals):
            if vals[index] is not None:
                right_child = TreeNode(vals[index])
                current_node.right = right_child
                to_visit.append(right_child)
            index += 1
    return root_node

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    elif p.val != q.val:
        return False
    else:
        left_equal = is_same_tree(p.left, q.left)
        right_equal = is_same_tree(p.right, q.right)
        return left_equal and right_equal

class Solution:
    def minimumLevel(self, root):
        if root is None:
            return 0
        queue = deque([root])
        res_level = 1
        smallest_sum = inf
        current_level = 1
        while queue:
            level_total = 0
            cnt = len(queue)
            j = 0
            while j < cnt:
                nd = queue.popleft()
                level_total += nd.val
                if nd.left is not None:
                    queue.append(nd.left)
                if nd.right is not None:
                    queue.append(nd.right)
                j += 1
            if level_total < smallest_sum:
                smallest_sum = level_total
                res_level = current_level
            current_level += 1
        return res_level