from collections import defaultdict
from typing import List

class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        maximum_size = 1

        def dfs(current_node: int, parent_node: int) -> int:
            nonlocal maximum_size
            count_same_color = 1
            flag_all_children_same = True

            for neighbor_node in graph[current_node]:
                if neighbor_node != parent_node:
                    subtree_size = dfs(neighbor_node, current_node)
                    if subtree_size == 0:
                        flag_all_children_same = False
                    else:
                        colors_match = colors[neighbor_node] == colors[current_node]
                        if colors_match:
                            count_same_color += subtree_size
                        else:
                            flag_all_children_same = False

            if flag_all_children_same:
                if maximum_size < count_same_color:
                    maximum_size = count_same_color
                return count_same_color
            else:
                return 0

        dfs(0, -1)

        return maximum_size