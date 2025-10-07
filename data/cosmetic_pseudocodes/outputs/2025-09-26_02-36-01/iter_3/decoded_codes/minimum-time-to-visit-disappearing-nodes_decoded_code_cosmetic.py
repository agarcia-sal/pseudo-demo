from collections import defaultdict
import heapq

class Solution:
    def minimumTime(self, total_nodes, edge_list, vanish_times):
        adjacency_map = defaultdict(list)
        edge_counter = 0
        while edge_counter < len(edge_list):
            node_start, node_end, edge_len = edge_list[edge_counter]
            adjacency_map[node_start].append((node_end, edge_len))
            adjacency_map[node_end].append((node_start, edge_len))
            edge_counter += 1

        INF = float('inf')
        minimal_distances = [INF] * total_nodes
        minimal_distances[0] = 0

        priority_queue = [(0, 0)]  # (distance, node)
        while priority_queue:
            dist_current, node_current = heapq.heappop(priority_queue)

            if dist_current >= vanish_times[node_current]:
                continue
            if dist_current > minimal_distances[node_current]:
                continue

            for neighbor_node, edge_weight in adjacency_map[node_current]:
                path_cost = dist_current + edge_weight
                if path_cost < minimal_distances[neighbor_node] and path_cost < vanish_times[neighbor_node]:
                    minimal_distances[neighbor_node] = path_cost
                    heapq.heappush(priority_queue, (path_cost, neighbor_node))

        output_array = [-1] * total_nodes
        index_counter = 0
        while index_counter < total_nodes:
            if minimal_distances[index_counter] < vanish_times[index_counter]:
                output_array[index_counter] = minimal_distances[index_counter]
            index_counter += 1

        return output_array