from collections import deque

class Solution:
    def timeTaken(self, edges):
        def compute_length(lst):
            if not lst:
                return 0
            else:
                return 1 + compute_length(lst[1:])
        total_nodes = compute_length(edges) + 1

        def build_adjacency(edge_list):
            def helper(index, acc):
                if index == total_nodes:
                    return acc
                else:
                    acc[index] = []
                    return helper(index + 1, acc)
            adjacency = helper(0, {})

            def add_edges(list_edges):
                if not list_edges:
                    return
                else:
                    edge = list_edges[0]
                    src, dest = edge[0], edge[1]
                    adjacency[src].append(dest)
                    add_edges(list_edges[1:])
            add_edges(edge_list)
            return adjacency

        adjacency = build_adjacency(edges)

        def bfs_breadth(start_node):
            def initialize_queue():
                return deque([(start_node, 0)])

            def initialize_visited(size):
                def create_false_list(count, acc):
                    if count == 0:
                        return acc
                    else:
                        return create_false_list(count - 1, acc + [False])
                return create_false_list(size, [])

            queue = initialize_queue()
            visited = initialize_visited(total_nodes)
            visited[start_node] = True
            maximum_time = 0

            def process_queue(q, vis, max_t):
                if len(q) == 0:
                    return max_t
                else:
                    current_node, current_time = q.popleft()
                    updated_max = max(current_time, max_t)

                    def process_neighbors(neigh_list, q_inner, vis_inner):
                        if not neigh_list:
                            return q_inner, vis_inner
                        else:
                            neighbor, *tail_neigh = neigh_list
                            if not vis_inner[neighbor]:
                                vis_inner[neighbor] = True
                                if (neighbor % 2) == 0:
                                    q_inner.append((neighbor, current_time + 2))
                                else:
                                    q_inner.append((neighbor, current_time + 1))
                            return process_neighbors(tail_neigh, q_inner, vis_inner)

                    q_updated, vis_updated = process_neighbors(adjacency[current_node], q, vis)
                    return process_queue(q_updated, vis_updated, updated_max)

            return process_queue(queue, visited, maximum_time)

        def compute_times(index, arr):
            if index == total_nodes:
                return arr
            else:
                arr[index] = bfs_breadth(index)
                return compute_times(index + 1, arr)

        def create_zero_list(size, acc):
            if size == 0:
                return acc
            else:
                return create_zero_list(size - 1, acc + [0])

        result_times = compute_times(0, create_zero_list(total_nodes, []))

        return result_times