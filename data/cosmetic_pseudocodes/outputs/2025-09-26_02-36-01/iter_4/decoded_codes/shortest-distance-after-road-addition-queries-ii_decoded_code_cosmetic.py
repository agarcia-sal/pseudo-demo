import heapq
from collections import defaultdict
from typing import List, Tuple

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[Tuple[int, int]]) -> List[int]:
        adjacency = defaultdict(list)
        for node in range(n - 1):
            adjacency[node].append((node + 1, 1))

        def dijkstra() -> int:
            distances = [float('inf')] * n
            distances[0] = 0
            priority_queue = [(0, 0)]

            while priority_queue:
                current_distance, current_vertex = heapq.heappop(priority_queue)
                if current_distance >= distances[current_vertex]:
                    continue
                for neighbor_vertex, edge_weight in adjacency[current_vertex]:
                    tentative_distance = current_distance + edge_weight
                    if tentative_distance < distances[neighbor_vertex]:
                        distances[neighbor_vertex] = tentative_distance
                        heapq.heappush(priority_queue, (tentative_distance, neighbor_vertex))
            return distances[n - 1]

        answers = []
        for start_node, weight_value in queries:
            adjacency[start_node].append((weight_value, 1))  # Edge tuple format as per original code: (neighbor, weight)
            shortest_path_length = dijkstra()
            answers.append(shortest_path_length)

        return answers