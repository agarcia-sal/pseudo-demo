from math import inf
from typing import List, Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(valList: List[Optional[int]]) -> Optional[TreeNode]:
    if not valList:
        return None

    def extract_node(queueRef: List[TreeNode]) -> TreeNode:
        return queueRef.pop(0)

    root = TreeNode(valList[0])
    cursor = 0
    container = [root]

    while container and cursor < len(valList):
        current = extract_node(container)

        if cursor + 1 < len(valList) and valList[cursor + 1] is not None:
            childLeft = TreeNode(valList[cursor + 1])
            current.left = childLeft
            container.append(childLeft)

        cursor += 2

        if cursor - 1 < len(valList) and valList[cursor - 1] is not None:
            childRight = TreeNode(valList[cursor - 1])
            current.right = childRight
            container.append(childRight)

    return root

def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def compare_nodes(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.val != b.val:
            return False
        return compare_nodes(a.left, b.left) and compare_nodes(a.right, b.right)
    return compare_nodes(p, q)

class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def append_children_if_not_none(nodeRef: TreeNode, queRef: List[TreeNode]) -> None:
            if nodeRef.left is not None:
                queRef.append(nodeRef.left)
            if nodeRef.right is not None:
                queRef.append(nodeRef.right)

        q = [root]
        ret_level = 1
        best_sum = inf
        current_level = 1

        while q:
            temp_sum = 0
            count = len(q)

            # Process nodes at current level recursively
            def process_nodes(idx: int) -> None:
                nonlocal temp_sum
                if idx > count:
                    return
                nd = q.pop(0)
                temp_sum += nd.val
                append_children_if_not_none(nd, q)
                process_nodes(idx + 1)

            process_nodes(1)

            if temp_sum < best_sum:
                best_sum = temp_sum
                ret_level = current_level
            current_level += 1

        return ret_level