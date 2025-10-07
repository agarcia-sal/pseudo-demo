from collections import defaultdict
from typing import List

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        graph = defaultdict(list)
        for edge in edges:
            u, v, w = edge
            graph[u].append([v, w])
            graph[v].append([u, w])
        n = len(graph)
        result = [0] * n

        def dfs(node: int, parent: int, dist: int, valid_nodes: List[int]) -> int:
            if dist % signalSpeed == 0:
                valid_nodes.append(node)
            count = 0
            for neighbor, weight in graph[node]:
                if neighbor != parent:
                    count += dfs(neighbor, node, dist + weight, valid_nodes)
            return count + (1 if dist % signalSpeed == 0 else 0)

        def count_pairs_through_c(c: int) -> int:
            valid_lists = []
            for neighbor, weight in graph[c]:
                valid_nodes = []
                dfs(neighbor, c, weight, valid_nodes)
                valid_lists.append(valid_nodes)
            total_pairs = 0
            for i in range(len(valid_lists) - 1):
                for j in range(i + 1, len(valid_lists)):
                    total_pairs += len(valid_lists[i]) * len(valid_lists[j])
            return total_pairs

        for c in range(n):
            result[c] = count_pairs_through_c(c)

        return result