from collections import defaultdict
from typing import List

class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        adjacency = defaultdict(list)
        for u, v in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)

        record = 1

        def dfs(current_node: int, parent_node: int) -> int:
            nonlocal record
            count_same_color_subtree = 1
            all_child_same_flag = True

            for adj_neighbor in adjacency[current_node]:
                if adj_neighbor != parent_node:
                    subtree_size = dfs(adj_neighbor, current_node)
                    if subtree_size == 0:
                        all_child_same_flag = False
                    else:
                        if colors[adj_neighbor] == colors[current_node]:
                            count_same_color_subtree += subtree_size
                        else:
                            all_child_same_flag = True  # This was "NOT false" meaning True

            if all_child_same_flag:
                if record < count_same_color_subtree:
                    record = count_same_color_subtree
                return count_same_color_subtree
            else:
                return 0

        start_node = 0
        invalid_parent = -1
        dfs_result = dfs(start_node, invalid_parent)
        return record