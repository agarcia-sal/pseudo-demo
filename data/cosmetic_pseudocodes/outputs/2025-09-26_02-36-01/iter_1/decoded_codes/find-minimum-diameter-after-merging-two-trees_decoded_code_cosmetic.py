from collections import deque
from math import inf

class Solution:
    def bfs(self, graph, start):
        count_nodes = len(graph)
        visited_nodes = [False] * count_nodes
        bfs_queue = deque([(start, 0)])
        visited_nodes[start] = True
        far_node = start
        greatest_dist = 0

        while bfs_queue:
            current_node, dist = bfs_queue.popleft()

            if dist > greatest_dist:
                greatest_dist = dist
                far_node = current_node

            for adj_node in graph[current_node]:
                if not visited_nodes[adj_node]:
                    visited_nodes[adj_node] = True
                    bfs_queue.append((adj_node, dist + 1))

        return far_node, greatest_dist

    def tree_diameter(self, graph):
        initial_node = 0
        farthest_node, _ = self.bfs(graph, initial_node)
        _, diameter_length = self.bfs(graph, farthest_node)
        return diameter_length

    def maximum_path_length_from_node(self, graph, start_node):
        size = len(graph)
        visited_flags = [False] * size
        exploration_queue = deque([(start_node, 0)])
        visited_flags[start_node] = True
        max_dist = 0

        while exploration_queue:
            node, dist = exploration_queue.popleft()

            if dist > max_dist:
                max_dist = dist

            for neighbor_node in graph[node]:
                if not visited_flags[neighbor_node]:
                    visited_flags[neighbor_node] = True
                    exploration_queue.append((neighbor_node, dist + 1))

        return max_dist

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

        diam1 = self.tree_diameter(graph_one)
        diam2 = self.tree_diameter(graph_two)

        longest_paths_1 = [self.maximum_path_length_from_node(graph_one, i) for i in range(size1)]
        longest_paths_2 = [self.maximum_path_length_from_node(graph_two, j) for j in range(size2)]

        minimal_diameter = inf

        for u in range(size1):
            for v in range(size2):
                combined_length = max(diam1, diam2, longest_paths_1[u] + longest_paths_2[v] + 1)
                if combined_length < minimal_diameter:
                    minimal_diameter = combined_length

        return minimal_diameter