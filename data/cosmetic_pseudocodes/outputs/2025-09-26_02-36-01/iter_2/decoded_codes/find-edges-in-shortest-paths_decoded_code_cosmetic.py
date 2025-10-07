from collections import defaultdict
import heapq
from math import inf
from typing import List, Tuple

class Solution:
    def findAnswer(self, n: int, edges: List[Tuple[int, int, int]]) -> List[bool]:
        adjacency_map = defaultdict(list)
        idx = 0
        while idx < len(edges):
            src, dst, wgt = edges[idx]
            adjacency_map[src].append((dst, wgt))
            adjacency_map[dst].append((src, wgt))
            idx += 1

        distances = [inf] * n
        distances[0] = 0
        heap_list = [(0, 0)]

        while heap_list:
            curr_distance, node = heapq.heappop(heap_list)
            if curr_distance > distances[node]:
                continue
            for neighbor, weight in adjacency_map[node]:
                possible_distance = curr_distance + weight
                if possible_distance < distances[neighbor]:
                    distances[neighbor] = possible_distance
                    heapq.heappush(heap_list, (possible_distance, neighbor))

        critical_edges = set()
        to_visit = [(n - 1, distances[n - 1])]
        visited_flags = [False] * n

        while to_visit:
            curr_node, curr_dist = to_visit.pop()
            if visited_flags[curr_node]:
                continue
            visited_flags[curr_node] = True

            for adj_node, edge_cost in adjacency_map[curr_node]:
                check_value = distances[adj_node] + edge_cost
                if curr_dist == check_value:
                    low_idx = min(curr_node, adj_node)
                    high_idx = max(curr_node, adj_node)
                    critical_edges.add((low_idx, high_idx))
                    to_visit.append((adj_node, distances[adj_node]))

        result_list = []
        for a, b, _ in edges:
            min_node = a if a < b else b
            max_node = a if a >= b else b
            result_list.append((min_node, max_node) in critical_edges)

        return result_list