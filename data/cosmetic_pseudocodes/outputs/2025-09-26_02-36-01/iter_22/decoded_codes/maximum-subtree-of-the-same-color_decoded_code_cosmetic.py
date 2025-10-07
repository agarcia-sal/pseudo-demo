from collections import defaultdict
from typing import List

class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        adjacency_map = defaultdict(list)
        for x, y in edges:
            adjacency_map[x].append(y)
            adjacency_map[y].append(x)

        result = 1

        def dfs(current_node: int, parent_node: int) -> int:
            nonlocal result
            counter_same_color = 1
            flag_all_children_match = True

            for adjacent_node in adjacency_map[current_node]:
                if adjacent_node != parent_node:
                    subtree_size = dfs(adjacent_node, current_node)
                    if subtree_size == 0:
                        flag_all_children_match = False
                    else:
                        if colors[adjacent_node] == colors[current_node]:
                            counter_same_color += subtree_size
                        else:
                            flag_all_children_match = False

            if flag_all_children_match:
                if counter_same_color > result:
                    result = counter_same_color
                return counter_same_color
            else:
                return 0

        dfs(0, -1)
        return result