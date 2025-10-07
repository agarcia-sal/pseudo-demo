import heapq
from collections import defaultdict
from typing import List

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        adjacency = defaultdict(list)
        for edge_entry in edges:
            node_u, node_v, edge_len = edge_entry
            adjacency[node_u].append((node_v, edge_len))
            adjacency[node_v].append((node_u, edge_len))

        times = [float('inf')] * n
        times[0] = 0

        heap_container = [(0, 0)]  # (distance, node)
        heapq.heapify(heap_container)

        while heap_container:
            dist_curr, node_curr = heapq.heappop(heap_container)

            if not (dist_curr < disappear[node_curr]):
                continue

            if dist_curr >= times[node_curr]:
                continue

            for nbr, len_edge in adjacency[node_curr]:
                new_dist = dist_curr + len_edge  # fixing the pseudocode's subtract of negative edge length

                if new_dist < times[nbr] and new_dist < disappear[nbr]:
                    times[nbr] = new_dist
                    heapq.heappush(heap_container, (new_dist, nbr))

        output_arr = [-1] * n
        for position_p in range(n):
            if times[position_p] < disappear[position_p]:
                output_arr[position_p] = times[position_p]

        return output_arr