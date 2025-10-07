from math import inf
from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def tree_node(values: List[Optional[int]]) -> Optional[TreeNode]:
    def dequeue_left(collection: List[TreeNode]) -> TreeNode:
        temp_var = collection[0]
        del collection[0]
        return temp_var

    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    index = 1

    while queue:
        node = dequeue_left(queue)
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1

    return root


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is not None and q is not None:
        if p.val != q.val:
            return False
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    elif p is None and q is None:
        return True
    else:
        return False


class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def pop_left(lst: List[TreeNode]) -> TreeNode:
            temp = lst[0]
            del lst[0]
            return temp

        queue = [root]
        min_level = 1
        min_sum = inf
        current_level = 1

        while queue:
            segment_sum = 0
            count = len(queue)
            idx = 0
            while idx < count:
                node = pop_left(queue)
                segment_sum += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                idx += 1
            if segment_sum < min_sum:
                min_sum = segment_sum
                min_level = current_level
            current_level += 1

        return min_level