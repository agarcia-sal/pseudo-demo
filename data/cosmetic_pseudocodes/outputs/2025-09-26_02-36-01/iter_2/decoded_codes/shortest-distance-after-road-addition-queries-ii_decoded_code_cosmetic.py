import heapq
from math import inf
from collections import defaultdict

class Solution:
    def shortestDistanceAfterQueries(self, total_nodes, query_list):
        adjacency_map = {i: [] for i in range(total_nodes)}
        for index_counter in range(total_nodes - 1):
            successor_node = index_counter + 1
            edge_weight = 1
            adjacency_map[index_counter].append([successor_node, edge_weight])

        def dijkstra():
            distances_array = [inf] * total_nodes
            distances_array[0] = 0
            priority_queue = [(0, 0)]  # (distance, node)
            while priority_queue:
                lowest_distance, current_vertex = heapq.heappop(priority_queue)
                if lowest_distance > distances_array[current_vertex]:
                    continue
                for edge_info in adjacency_map[current_vertex]:
                    neighbor_node, weight_value = edge_info
                    accum_distance = lowest_distance + weight_value
                    if accum_distance < distances_array[neighbor_node]:
                        distances_array[neighbor_node] = accum_distance
                        heapq.heappush(priority_queue, (accum_distance, neighbor_node))
            return distances_array[total_nodes - 1]

        answers = []
        for current_query in query_list:
            origin_node, destination_node = current_query
            adjacency_map[origin_node].append([destination_node, 1])
            answers.append(dijkstra())

        return answers