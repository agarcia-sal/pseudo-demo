from collections import deque
from math import inf

class Solution:
    def bfs(self, graph, start):
        total_nodes = len(graph)
        status_flags = [False] * total_nodes
        dequeue_structure = deque()
        dequeue_structure.append((start, 0))
        status_flags[start] = True
        current_farthest = start
        greatest_distance = 0

        while dequeue_structure:
            current_node, current_distance = dequeue_structure.popleft()
            if current_distance > greatest_distance:
                greatest_distance = current_distance
                current_farthest = current_node
            for adjacent_node in graph[current_node]:
                if not status_flags[adjacent_node]:
                    status_flags[adjacent_node] = True
                    dequeue_structure.append((adjacent_node, current_distance + 1))

        return current_farthest, greatest_distance

    def tree_diameter(self, graph):
        initial_node = 0
        far_node, _ = self.bfs(graph, initial_node)
        _, max_diameter = self.bfs(graph, far_node)
        return max_diameter

    def maximum_path_length_from_node(self, graph, node):
        total_length = len(graph)
        visited_marks = [False] * total_length
        node_queue = deque()
        node_queue.append((node, 0))
        visited_marks[node] = True
        max_dist_found = 0

        while node_queue:
            current_node, current_dist = node_queue.popleft()
            if current_dist > max_dist_found:
                max_dist_found = current_dist
            for neighbor_node in graph[current_node]:
                if not visited_marks[neighbor_node]:
                    visited_marks[neighbor_node] = True
                    node_queue.append((neighbor_node, current_dist + 1))

        return max_dist_found

    def minimumDiameterAfterMerge(self, edges1, edges2):
        len_edges1_plus = len(edges1) + 1
        len_edges2_plus = len(edges2) + 1

        g1 = [[] for _ in range(len_edges1_plus)]
        g2 = [[] for _ in range(len_edges2_plus)]

        for element_x, element_y in edges1:
            g1[element_x].append(element_y)
            g1[element_y].append(element_x)

        for element_p, element_q in edges2:
            g2[element_p].append(element_q)
            g2[element_q].append(element_p)

        diam1 = self.tree_diameter(g1)
        diam2 = self.tree_diameter(g2)

        longest_paths_1 = []
        for index_i in range(len_edges1_plus):
            longest_paths_1.append(self.maximum_path_length_from_node(g1, index_i))

        longest_paths_2 = []
        for index_j in range(len_edges2_plus):
            longest_paths_2.append(self.maximum_path_length_from_node(g2, index_j))

        minimal_possible_diameter = inf

        for u_index in range(len_edges1_plus):
            for v_index in range(len_edges2_plus):
                candidate_diameter = diam1 if diam1 > diam2 else diam2
                combined_path = longest_paths_1[u_index] + longest_paths_2[v_index] + 1
                if combined_path > candidate_diameter:
                    candidate_diameter = combined_path
                if candidate_diameter < minimal_possible_diameter:
                    minimal_possible_diameter = candidate_diameter

        return minimal_possible_diameter