import heapq
from collections import defaultdict
from math import inf
from typing import List, Tuple

class Solution:
    def findAnswer(self, n: int, edges: List[Tuple[int, int, int]]) -> List[bool]:
        adjacency_map = defaultdict(list)
        for x, y, z in edges:
            adjacency_map[x].append((y, z))
            adjacency_map[y].append((x, z))

        distances = [inf] * n
        distances[0] = 0

        priority_queue = [(0, 0)]  # (distance, vertex)
        heapq.heapify(priority_queue)

        while priority_queue:
            current_distance, vertex = heapq.heappop(priority_queue)
            if current_distance > distances[vertex]:
                continue

            for neighbor, weight in adjacency_map[vertex]:
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    heapq.heappush(priority_queue, (tentative_distance, neighbor))

        path_edges = set()
        traversal_stack = [(n - 1, distances[n - 1])]
        visited_flags = [False] * n

        while traversal_stack:
            current_vertex, curr_dist = traversal_stack.pop()
            if visited_flags[current_vertex]:
                continue
            visited_flags[current_vertex] = True

            for adjacent_vertex, edge_weight in adjacency_map[current_vertex]:
                if curr_dist == distances[adjacent_vertex] + edge_weight:
                    min_vertex = min(current_vertex, adjacent_vertex)
                    max_vertex = max(current_vertex, adjacent_vertex)
                    path_edges.add((min_vertex, max_vertex))
                    traversal_stack.append((adjacent_vertex, distances[adjacent_vertex]))

        results = []
        for a, b, _ in edges:
            lower_vertex = min(a, b)
            upper_vertex = max(a, b)
            results.append((lower_vertex, upper_vertex) in path_edges)

        return results