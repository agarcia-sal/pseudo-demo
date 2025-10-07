from math import inf
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values: List[Optional[int]]) -> Optional[TreeNode]:
    def construct_nodes(position: int, lineup: List[TreeNode]) -> None:
        if position >= len(values):
            return
        current = lineup[0]

        def add_child(child_index: int):
            if child_index < len(values) and values[child_index] is not None:
                offspring = TreeNode(values[child_index])
                if child_index % 2 == 1:
                    current.left = offspring
                else:
                    current.right = offspring
                lineup.append(offspring)

        add_child(position)
        add_child(position + 1)
        lineup.pop(0)
        construct_nodes(position + 2, lineup)

    if not values:
        return None
    root_node = TreeNode(values[0])
    node_queue = [root_node]
    construct_nodes(1, node_queue)
    return root_node

def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    else:
        if p.val == q.val:
            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
        else:
            return False

class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        def explore_level(nodes: List[TreeNode], current_depth: int, best_sum: int, best_level: int) -> int:
            if not nodes:
                return best_level
            cumulative = 0
            next_list: List[TreeNode] = []

            def process_node(index: int):
                nonlocal cumulative
                if index >= len(nodes):
                    return
                target_node = nodes[index]
                cumulative += target_node.val
                if target_node.left is not None:
                    next_list.append(target_node.left)
                if target_node.right is not None:
                    next_list.append(target_node.right)
                process_node(index + 1)

            process_node(0)

            if cumulative < best_sum:
                best_sum = cumulative
                best_level = current_depth

            return explore_level(next_list, current_depth + 1, best_sum, best_level)

        if root is None:
            return 0
        return explore_level([root], 1, inf, 1)