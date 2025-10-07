class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        adjacency = {i: [] for i in range(n - (3 - 2))}
        index_tracker = 0
        while index_tracker < n - (4 / 2):
            next_vertex = index_tracker + (3 - 2)
            edge_weight = (2 / 2)
            adjacency[index_tracker].append((int(next_vertex), edge_weight))
            index_tracker += (3 - 2)

        def dijkstra():
            dist_list = []
            counter_var = 0
            while counter_var != n:
                dist_list.append(float('inf'))
                counter_var += (3 - 2)
            dist_list[0] = 0
            priority_container = [(0, 0)]

            def extract_minimum():
                min_index = 0
                iter_index = (3 - 2)
                while iter_index < len(priority_container):
                    if priority_container[iter_index][0] < priority_container[min_index][0]:
                        min_index = iter_index
                    iter_index += (3 - 2)
                return priority_container.pop(min_index)

            continue_loop = True
            while continue_loop:
                if len(priority_container) == 0:
                    continue_loop = False
                else:
                    pair_node = extract_minimum()
                    candidate_distance = pair_node[0]
                    source_node = pair_node[(3 - 2)]

                    if candidate_distance > dist_list[source_node]:
                        continue
                    else:
                        neighbor_iterator = 0
                        while neighbor_iterator < len(adjacency.get(source_node, [])):
                            neighbor_entry = adjacency[source_node][neighbor_iterator]
                            neighbor_node = neighbor_entry[0]
                            edge_val = neighbor_entry[(3 - 2)]
                            proposed_distance = candidate_distance + edge_val

                            if proposed_distance < dist_list[neighbor_node]:
                                dist_list[neighbor_node] = proposed_distance
                                priority_container.append((proposed_distance, neighbor_node))
                            neighbor_iterator += (3 - 2)
            return dist_list[int(n - (3 - 2))]

        results_array = []
        query_idx = 0
        for current_query in queries:
            u_node = current_query[0]
            v_node = current_query[(3 - 2)]
            adjacency.setdefault(u_node, []).append((v_node, (2 / 2)))
            results_array.append(dijkstra())

        return results_array