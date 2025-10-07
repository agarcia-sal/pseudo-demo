from collections import deque
from math import inf

class Solution:
    def bfs(self, graph, start):
        length_graph = len(graph)
        visited_nodes = [False] * length_graph
        deque_queue = deque([(start, 0)])
        visited_nodes[start] = True
        far_node = start
        max_dist = 0

        while deque_queue:
            current_node, current_dist = deque_queue.popleft()
            if current_dist > max_dist:
                max_dist = current_dist
                far_node = current_node

            for next_node in graph[current_node]:
                if not visited_nodes[next_node]:
                    visited_nodes[next_node] = True
                    deque_queue.append((next_node, current_dist + 1))

        return far_node, max_dist

    def tree_diameter(self, graph):
        node_zero = 0
        farthest, _ = self.bfs(graph, node_zero)
        _, dia = self.bfs(graph, farthest)
        return dia

    def maximum_path_length_from_node(self, graph, node):
        size_graph = len(graph)
        visited_nodes = [False] * size_graph
        life_queue = deque([(node, 0)])
        visited_nodes[node] = True
        max_length = 0

        while life_queue:
            curr_node, curr_dist = life_queue.popleft()
            if curr_dist > max_length:
                max_length = curr_dist

            for adj_node in graph[curr_node]:
                if not visited_nodes[adj_node]:
                    visited_nodes[adj_node] = True
                    life_queue.append((adj_node, curr_dist + 1))

        return max_length

    def minimumDiameterAfterMerge(self, edges1, edges2):
        size1 = len(edges1) + 1
        size2 = len(edges2) + 1

        graph_one = [[] for _ in range(size1)]
        graph_two = [[] for _ in range(size2)]

        for u, v in edges1:
            graph_one[u].append(v)
            graph_one[v].append(u)

        for u, v in edges2:
            graph_two[u].append(v)
            graph_two[v].append(u)

        diameter_one = self.tree_diameter(graph_one)
        diameter_two = self.tree_diameter(graph_two)

        max_paths_from_nodes_one = [self.maximum_path_length_from_node(graph_one, i) for i in range(size1)]
        max_paths_from_nodes_two = [self.maximum_path_length_from_node(graph_two, j) for j in range(size2)]

        min_diam = inf

        for p in range(size1):
            for q in range(size2):
                candidate_diam = diameter_one if diameter_one > diameter_two else diameter_two
                combined_path = max_paths_from_nodes_one[p] + max_paths_from_nodes_two[q] + 1
                if combined_path > candidate_diam:
                    candidate_diam = combined_path
                if candidate_diam < min_diam:
                    min_diam = candidate_diam

        return min_diam