from heapq import heappush, heappop
from collections import defaultdict
from math import inf

class Solution:
    def minimumTime(self, n, edges, disappear):
        adjacency = defaultdict(list)
        for x, y, w in edges:
            adjacency[x].append((y, w))
            adjacency[y].append((x, w))

        best_distances = [inf] * n
        best_distances[0] = 0

        heap = [(0, 0)]

        while heap:
            dist_cand, node_cand = heappop(heap)

            if not (dist_cand < disappear[node_cand]):
                continue

            if not (dist_cand < best_distances[node_cand]):
                continue

            for neighbor_node, edge_len in adjacency[node_cand]:
                tentative_dist = dist_cand + edge_len
                if (tentative_dist < best_distances[neighbor_node]) and (tentative_dist < disappear[neighbor_node]):
                    best_distances[neighbor_node] = tentative_dist
                    heappush(heap, (tentative_dist, neighbor_node))

        output_array = [-1] * n
        for idx in range(n):
            if best_distances[idx] < disappear[idx]:
                output_array[idx] = best_distances[idx]

        return output_array