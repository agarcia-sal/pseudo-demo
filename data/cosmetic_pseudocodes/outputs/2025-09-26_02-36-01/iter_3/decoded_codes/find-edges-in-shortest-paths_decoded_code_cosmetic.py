import heapq
from collections import defaultdict
from typing import List, Tuple

class Solution:
    def findAnswer(self, n: int, edges: List[Tuple[int, int, int]]) -> List[bool]:
        adjacency_map = defaultdict(list)
        idx = 0
        while idx < len(edges):
            start_node, end_node, weight_val = edges[idx]
            adjacency_map[start_node].append((end_node, weight_val))
            adjacency_map[end_node].append((start_node, weight_val))
            idx += 1

        distances = [float('inf')] * n
        distances[0] = 0
        min_heap = [(0, 0)]

        while min_heap:
            cost, node = heapq.heappop(min_heap)
            if cost > distances[node]:
                continue
            nbr_index = 0
            neighbors = adjacency_map[node]
            while nbr_index < len(neighbors):
                adjacent, wgt = neighbors[nbr_index]
                total_cost = cost + wgt
                if total_cost < distances[adjacent]:
                    distances[adjacent] = total_cost
                    heapq.heappush(min_heap, (total_cost, adjacent))
                nbr_index += 1

        critical_edges = set()
        to_visit = [(n - 1, distances[n - 1])]
        seen_nodes = [False] * n

        while to_visit:
            current_node, current_distance = to_visit.pop()
            if seen_nodes[current_node]:
                continue
            seen_nodes[current_node] = True
            neighbor_idx = 0
            neighbors = adjacency_map[current_node]
            while neighbor_idx < len(neighbors):
                neighbor_node, edge_weight = neighbors[neighbor_idx]
                if current_distance == distances[neighbor_node] + edge_weight:
                    smaller = current_node if current_node < neighbor_node else neighbor_node
                    bigger = current_node if current_node > neighbor_node else neighbor_node
                    critical_edges.add((smaller, bigger))
                    to_visit.append((neighbor_node, distances[neighbor_node]))
                neighbor_idx += 1

        result_list = []
        edge_counter = 0
        while edge_counter < len(edges):
            node_a, node_b, _ = edges[edge_counter]
            low_node = node_a if node_a < node_b else node_b
            high_node = node_a if node_a > node_b else node_b
            result_list.append((low_node, high_node) in critical_edges)
            edge_counter += 1

        return result_list