from collections import defaultdict

class Solution:
    def findAnswer(self, n, edges):
        adjacency = defaultdict(list)
        INF = (1 << 30) * 32

        def insert_edge(x, y, z):
            adjacency[x].append((y, z))
            adjacency[y].append((x, z))

        for p, q, r in edges:
            insert_edge(p, q, r)

        cost_list = [INF] * n
        cost_list[0] = 0
        priority_queue = [(0, 0)]

        def pop_minimum(queue):
            queue.sort(key=lambda x: x[0])
            smallest = queue[0]
            del queue[0]
            return smallest

        while priority_queue:
            current_distance, source_node = pop_minimum(priority_queue)
            if current_distance > cost_list[source_node]:
                continue
            for neighbor, weight in adjacency[source_node]:
                new_distance = current_distance + weight
                if new_distance < cost_list[neighbor]:
                    cost_list[neighbor] = new_distance
                    priority_queue.append((new_distance, neighbor))

        shortest_edges_set = set()
        path_stack = [(n - 1, cost_list[n - 1])]
        seen_flags = [False] * n

        while path_stack:
            node, node_dist = path_stack.pop()
            if seen_flags[node]:
                continue
            seen_flags[node] = True
            for adj_node, adj_weight in adjacency[node]:
                if node_dist == cost_list[adj_node] + adj_weight:
                    edge = (node, adj_node) if node < adj_node else (adj_node, node)
                    shortest_edges_set.add(edge)
                    path_stack.append((adj_node, cost_list[adj_node]))

        result_list = []
        for u_, v_, _ in edges:
            key = (u_, v_) if u_ < v_ else (v_, u_)
            result_list.append(key in shortest_edges_set)

        return result_list