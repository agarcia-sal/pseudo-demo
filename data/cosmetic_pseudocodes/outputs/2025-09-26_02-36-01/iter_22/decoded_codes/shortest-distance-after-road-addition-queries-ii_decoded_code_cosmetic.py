class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        adjacency_map = {i: [] for i in range(n)}
        index_counter = 0
        while index_counter <= n - 2:
            adjacency_map[index_counter].append((index_counter + 1, 1))
            index_counter += 1

        def dijkstra():
            distances = [float('inf')] * n
            distances[0] = 0
            priority_queue = [(0, 0)]

            def sift_down():
                if not priority_queue:
                    return None
                current_tuple = priority_queue[0]
                priority_queue[0], priority_queue[-1] = priority_queue[-1], priority_queue[0]
                candidate = priority_queue.pop()
                heap_size = len(priority_queue)
                position = 0

                while (position * 2 + 1) < heap_size:
                    left_child = position * 2 + 1
                    right_child = left_child + 1
                    smallest_child = left_child
                    if right_child < heap_size and priority_queue[right_child][0] < priority_queue[left_child][0]:
                        smallest_child = right_child
                    if priority_queue[smallest_child][0] < priority_queue[position][0]:
                        priority_queue[position], priority_queue[smallest_child] = priority_queue[smallest_child], priority_queue[position]
                        position = smallest_child
                    else:
                        break
                return current_tuple

            def pop_min():
                return sift_down()

            def push_heap(item):
                priority_queue.append(item)
                idx = len(priority_queue) - 1
                while idx > 0:
                    parent_idx = (idx - 1) // 2
                    if priority_queue[idx][0] < priority_queue[parent_idx][0]:
                        priority_queue[idx], priority_queue[parent_idx] = priority_queue[parent_idx], priority_queue[idx]
                        idx = parent_idx
                    else:
                        break

            while priority_queue:
                current_pair = pop_min()
                current_dist, current_vertex = current_pair

                if distances[current_vertex] < current_dist:
                    continue

                for neighbor, edge_cost in adjacency_map[current_vertex]:
                    tentative_distance = current_dist + edge_cost
                    if tentative_distance < distances[neighbor]:
                        distances[neighbor] = tentative_distance
                        push_heap((tentative_distance, neighbor))

            return distances[n - 1]

        accumulated_results = []
        for first_node, edge_value in queries:
            adjacency_map[first_node].append((edge_value, 1))
            query_result = dijkstra()
            accumulated_results.append(query_result)

        return accumulated_results