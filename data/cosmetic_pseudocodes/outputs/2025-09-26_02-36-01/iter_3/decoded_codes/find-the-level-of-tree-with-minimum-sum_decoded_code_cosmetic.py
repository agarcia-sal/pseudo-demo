from collections import deque
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(vals):
    n = len(vals)
    if n == 0:
        return None
    root_node = TreeNode(vals[0])
    idx = 1
    queue_ds = deque()
    queue_ds.append(root_node)
    while len(queue_ds) > 0:
        current_ele = queue_ds.popleft()
        if idx < n:
            left_val = vals[idx]
            if left_val is not None:
                current_ele.left = TreeNode(left_val)
                queue_ds.append(current_ele.left)
            idx += 1
        if idx < n:
            right_val = vals[idx]
            if right_val is not None:
                current_ele.right = TreeNode(right_val)
                queue_ds.append(current_ele.right)
            idx += 1
    return root_node

def is_same_tree(node1, node2):
    if node1 is None and node2 is None:
        return True
    elif node1 is None or node2 is None:
        return False
    elif node1.val != node2.val:
        return False
    else:
        return is_same_tree(node1.left, node2.left) and is_same_tree(node1.right, node2.right)

class Solution:
    def minimumLevel(self, root):
        if root is None:
            return 0
        que = deque([root])
        minimum_level = 1
        minimum_sum = inf
        current_level = 1
        while len(que) > 0:
            level_total = 0
            count = len(que)
            while count > 0:
                curr_node = que.popleft()
                level_total += curr_node.val
                if curr_node.left is not None:
                    que.append(curr_node.left)
                if curr_node.right is not None:
                    que.append(curr_node.right)
                count -= 1
            if level_total < minimum_sum:
                minimum_sum = level_total
                minimum_level = current_level
            current_level += 1
        return minimum_level