import heapq
from math import inf
from typing import List, Tuple

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[Tuple[int, int]]) -> List[int]:
        graph = {i: [] for i in range(n)}
        for i in range(n - 1):
            graph[i].append((i + 1, 1))

        def dijkstra() -> int:
            dist = [inf] * n
            dist[0] = 0
            pq = [(0, 0)]
            while pq:
                current_dist, current_node = heapq.heappop(pq)
                if current_dist > dist[current_node]:
                    continue
                for neighbor, weight in graph[current_node]:
                    distance = current_dist + weight
                    if distance < dist[neighbor]:
                        dist[neighbor] = distance
                        heapq.heappush(pq, (distance, neighbor))
            return dist[n - 1]

        result = []
        for u, v in queries:
            graph[u].append((v, 1))
            result.append(dijkstra())
        return result