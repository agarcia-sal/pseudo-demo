from collections import defaultdict
from typing import List

class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        self.result = 1

        def dfs(node: int, parent: int) -> int:
            same_color_count = 1
            all_children_same_color = True
            for neighbor in tree[node]:
                if neighbor != parent:
                    child_count = dfs(neighbor, node)
                    if child_count == 0:
                        all_children_same_color = False
                    elif colors[neighbor] == colors[node]:
                        same_color_count += child_count
                    else:
                        all_children_same_color = False
            if all_children_same_color:
                if same_color_count > self.result:
                    self.result = same_color_count
                return same_color_count
            else:
                return 0

        dfs(0, -1)
        return self.result