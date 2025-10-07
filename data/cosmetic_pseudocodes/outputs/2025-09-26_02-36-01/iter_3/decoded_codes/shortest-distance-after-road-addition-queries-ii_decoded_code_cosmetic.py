from math import inf

class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        adjacency_map = {i: [] for i in range(n)}
        idx = 0
        while idx < n - 1:
            next_node = idx + 1
            edge_weight = 1
            adjacency_map[idx].append([next_node, edge_weight])
            idx += 1

        def dijkstra():
            distances = [inf] * n
            distances[0] = 0
            priority_queue = [[0, 0]]

            while priority_queue:
                priority_queue.sort(key=lambda x: x[0])
                current_distance, current_vertex = priority_queue.pop(0)

                if current_distance > distances[current_vertex]:
                    continue

                list_neighbors = adjacency_map[current_vertex]
                j = 0
                while j < len(list_neighbors):
                    neighbor_node, edge_cost = list_neighbors[j]
                    new_distance = current_distance + edge_cost
                    if new_distance < distances[neighbor_node]:
                        distances[neighbor_node] = new_distance
                        priority_queue.append([new_distance, neighbor_node])
                    j += 1

            return distances[n - 1]

        output_list = []
        iter_idx = 0
        while iter_idx < len(queries):
            source, destination = queries[iter_idx]
            adjacency_map[source].append([destination, 1])
            output_list.append(dijkstra())
            iter_idx += 1

        return output_list