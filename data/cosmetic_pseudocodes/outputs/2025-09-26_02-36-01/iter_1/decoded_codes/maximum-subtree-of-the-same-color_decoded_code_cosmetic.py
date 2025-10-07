from collections import defaultdict

class Solution:
    def maximumSubtreeSize(self, edges, colors):
        adjacency = defaultdict(list)
        for u, v in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)

        result = 1

        def dfs(node, parent):
            nonlocal result
            subtree_size = 1
            uniform_colors = True
            for neighbor in adjacency[node]:
                if neighbor != parent:
                    descendant_size = dfs(neighbor, node)
                    if descendant_size == 0:
                        uniform_colors = False
                    elif colors[neighbor] == colors[node]:
                        subtree_size += descendant_size
                    else:
                        uniform_colors = False
            if uniform_colors:
                if subtree_size > result:
                    result = subtree_size
                return subtree_size
            else:
                return 0

        dfs(0, -1)
        return result