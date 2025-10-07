import heapq
from collections import defaultdict
from math import inf

class Solution:
    def minimumTime(self, n, edges, disappear):
        adjacency = defaultdict(list)

        for node_a, node_b, dist in edges:
            adjacency[node_a].append((node_b, dist))
            adjacency[node_b].append((node_a, dist))

        shortest_paths = [inf] * n
        shortest_paths[0] = 0

        heap = [(0, 0)]  # (distance, node)

        while heap:
            extracted_distance, extracted_node = heapq.heappop(heap)

            if extracted_distance >= disappear[extracted_node]:
                continue

            if extracted_distance > shortest_paths[extracted_node]:
                continue

            for adjacent_node, edge_len in adjacency[extracted_node]:
                new_distance = extracted_distance + edge_len
                if new_distance < shortest_paths[adjacent_node] and new_distance < disappear[adjacent_node]:
                    shortest_paths[adjacent_node] = new_distance
                    heapq.heappush(heap, (new_distance, adjacent_node))

        output = [-1] * n
        for pos in range(n):
            if shortest_paths[pos] < disappear[pos]:
                output[pos] = shortest_paths[pos]

        return output