import heapq
from typing import List, Tuple

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[Tuple[int, int]]) -> List[int]:
        graph = {i: [] for i in range(n)}

        for index in range(n - 1):
            graph[index].append((index + 1, 1))

        def dijkstra() -> int:
            dist = [float('inf')] * n
            dist[0] = 0
            priority_queue = [(0, 0)]  # (distance, node)

            while priority_queue:
                curr_dist, curr_node = heapq.heappop(priority_queue)

                if curr_dist > dist[curr_node]:
                    continue

                for adj_node, edge_weight in graph[curr_node]:
                    total_dist = curr_dist + edge_weight
                    if total_dist < dist[adj_node]:
                        dist[adj_node] = total_dist
                        heapq.heappush(priority_queue, (total_dist, adj_node))

            return dist[n - 1]

        results = []
        for start_node, weight_val in queries:
            graph[start_node].append((weight_val, 1))
            results.append(dijkstra())

        return results