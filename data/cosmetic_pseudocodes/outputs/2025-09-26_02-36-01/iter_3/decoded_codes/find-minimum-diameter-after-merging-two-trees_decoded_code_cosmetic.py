from collections import deque
from math import inf

class Solution:
    def bfs(self, graph, start):
        length_graph = len(graph)
        marked_nodes = [False] * length_graph
        traversal_queue = deque([(start, 0)])
        marked_nodes[start] = True
        candidate_node = start
        max_dist = 0

        while traversal_queue:
            current_node, curr_dist = traversal_queue.popleft()
            if curr_dist > max_dist:
                max_dist = curr_dist
                candidate_node = current_node

            for adj_node in graph[current_node]:
                if not marked_nodes[adj_node]:
                    marked_nodes[adj_node] = True
                    traversal_queue.append((adj_node, curr_dist + 1))

        return candidate_node, max_dist

    def tree_diameter(self, graph):
        initial_start = 0
        endpoint, _ = self.bfs(graph, initial_start)
        _, longest_dist = self.bfs(graph, endpoint)
        return longest_dist

    def maximum_path_length_from_node(self, graph, node):
        nodes_count = len(graph)
        visited_nodes = [False] * nodes_count
        exploration_queue = deque([(node, 0)])
        visited_nodes[node] = True
        maximum_length = 0

        while exploration_queue:
            curr_node, distance = exploration_queue.popleft()
            if distance > maximum_length:
                maximum_length = distance

            for neighbour_node in graph[curr_node]:
                if not visited_nodes[neighbour_node]:
                    visited_nodes[neighbour_node] = True
                    exploration_queue.append((neighbour_node, distance + 1))

        return maximum_length

    def minimumDiameterAfterMerge(self, edges1, edges2):
        size_g1 = len(edges1) + 1
        size_g2 = len(edges2) + 1

        trees1 = [[] for _ in range(size_g1)]
        trees2 = [[] for _ in range(size_g2)]

        for first_node, second_node in edges1:
            trees1[first_node].append(second_node)
            trees1[second_node].append(first_node)

        for first_node, second_node in edges2:
            trees2[first_node].append(second_node)
            trees2[second_node].append(first_node)

        diameter_tree1 = self.tree_diameter(trees1)
        diameter_tree2 = self.tree_diameter(trees2)

        max_paths_tree1 = [self.maximum_path_length_from_node(trees1, i) for i in range(size_g1)]
        max_paths_tree2 = [self.maximum_path_length_from_node(trees2, i) for i in range(size_g2)]

        minimum_possible_diameter = inf

        for outer in range(size_g1):
            for inner in range(size_g2):
                candidate_diameter_candidates = [
                    diameter_tree1,
                    diameter_tree2,
                    max_paths_tree1[outer] + max_paths_tree2[inner] + 1
                ]
                candidate_diameter = max(candidate_diameter_candidates)

                if candidate_diameter < minimum_possible_diameter:
                    minimum_possible_diameter = candidate_diameter

        return minimum_possible_diameter