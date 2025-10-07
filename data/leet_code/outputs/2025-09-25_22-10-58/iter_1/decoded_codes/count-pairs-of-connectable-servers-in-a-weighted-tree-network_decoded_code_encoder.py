from collections import defaultdict
from typing import List, Tuple


class Solution:
    def countPairsOfConnectableServers(self, edges: List[Tuple[int, int, int]], signalSpeed: int) -> List[int]:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        n = len(graph)
        result = [0] * n

        def dfs(node: int, parent: int, distance: int, path: List[int]) -> int:
            if distance % signalSpeed == 0:
                path.append(node)
            count = 0
            for neighbor, weight in graph[node]:
                if neighbor != parent:
                    count += dfs(neighbor, node, distance + weight, path)
            if distance % signalSpeed == 0:
                return count + 1
            else:
                return count

        def count_pairs_through_c(c: int) -> int:
            paths = []
            for neighbor, weight in graph[c]:
                path = []
                dfs(neighbor, c, weight, path)
                paths.append(path)
            total_pairs = 0
            length = len(paths)
            for i in range(length - 1):
                for j in range(i + 1, length):
                    total_pairs += len(paths[i]) * len(paths[j])
            return total_pairs

        for c in range(n):
            result[c] = count_pairs_through_c(c)
        return result