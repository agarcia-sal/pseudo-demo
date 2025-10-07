from collections import deque
from math import inf

class Solution:
    def bfs(self, graph, start):
        total_nodes = len(graph)
        visited_nodes = [False] * total_nodes
        traversal_queue = deque([(start, 0)])
        visited_nodes[start] = True
        far_node = start
        greatest_distance = 0

        def process_queue():
            if not traversal_queue:
                return

            current_node, current_distance = traversal_queue.popleft()

            if current_distance > greatest_distance:
                nonlocal greatest_distance, far_node
                greatest_distance = current_distance
                far_node = current_node

            neighbor_iterator = 0
            while neighbor_iterator < len(graph[current_node]):
                adjacent = graph[current_node][neighbor_iterator]
                if not visited_nodes[adjacent]:
                    visited_nodes[adjacent] = True
                    traversal_queue.append((adjacent, current_distance + 1))
                neighbor_iterator += 1

            process_queue()

        process_queue()
        return far_node, greatest_distance

    def tree_diameter(self, graph):
        initial_node = 0
        temp_farthest, _ = self.bfs(graph, initial_node)
        _, diameter_value = self.bfs(graph, temp_farthest)
        return diameter_value

    def maximum_path_length_from_node(self, graph, node):
        graph_size = len(graph)
        visited_flags = [False] * graph_size
        bfs_queue = deque([(node, 0)])
        visited_flags[node] = True
        max_dist = 0

        def iterate_bfs():
            if not bfs_queue:
                return

            current_vertex, current_dist = bfs_queue.popleft()

            if current_dist > max_dist:
                nonlocal max_dist
                max_dist = current_dist

            n_index = 0
            while n_index < len(graph[current_vertex]):
                child_node = graph[current_vertex][n_index]
                if not visited_flags[child_node]:
                    visited_flags[child_node] = True
                    bfs_queue.append((child_node, current_dist + 1))
                n_index += 1

            iterate_bfs()

        iterate_bfs()
        return max_dist

    def minimumDiameterAfterMerge(self, edges1, edges2):
        length_n = len(edges1) + 1
        length_m = len(edges2) + 1

        adj_list1 = [[] for _ in range(length_n)]
        adj_list2 = [[] for _ in range(length_m)]

        idx1 = 0
        while idx1 < len(edges1):
            u1, v1 = edges1[idx1]
            adj_list1[u1].append(v1)
            adj_list1[v1].append(u1)
            idx1 += 1

        idx2 = 0
        while idx2 < len(edges2):
            u2, v2 = edges2[idx2]
            adj_list2[u2].append(v2)
            adj_list2[v2].append(u2)
            idx2 += 1

        dia1 = self.tree_diameter(adj_list1)
        dia2 = self.tree_diameter(adj_list2)

        longest_paths1 = []
        counter1 = 0
        while counter1 < length_n:
            longest_paths1.append(self.maximum_path_length_from_node(adj_list1, counter1))
            counter1 += 1

        longest_paths2 = []
        counter2 = 0
        while counter2 < length_m:
            longest_paths2.append(self.maximum_path_length_from_node(adj_list2, counter2))
            counter2 += 1

        minimal_diameter = inf
        loop_u = 0
        while loop_u < length_n:
            loop_v = 0
            while loop_v < length_m:
                combined_distance = longest_paths1[loop_u] + longest_paths2[loop_v] + 1
                potential_diameter = dia1
                if dia2 > potential_diameter:
                    potential_diameter = dia2
                if combined_distance > potential_diameter:
                    potential_diameter = combined_distance

                if potential_diameter < minimal_diameter:
                    minimal_diameter = potential_diameter

                loop_v += 1
            loop_u += 1

        return minimal_diameter