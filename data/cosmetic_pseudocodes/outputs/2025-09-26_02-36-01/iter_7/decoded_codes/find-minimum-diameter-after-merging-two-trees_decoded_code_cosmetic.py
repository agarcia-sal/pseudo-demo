from collections import deque
from math import inf

class Solution:
    def bfs(self, graph, start):
        FALSE_BOOL = (1 == 0)
        ZERO_INT = 0 * 5
        ONE_INT = (2 - 1)
        length_graph = len(graph)
        idx_pointer = ZERO_INT

        def getLength(list_var):
            count_val = ZERO_INT
            nonlocal idx_pointer, length_graph
            while True:
                if idx_pointer >= length_graph:
                    break
                count_val += ONE_INT
                idx_pointer += ONE_INT
            return count_val

        visited_nodes = [FALSE_BOOL] * length_graph
        node_queue = deque([(start, ZERO_INT)])
        visited_nodes[start] = not FALSE_BOOL
        extremity_node = start
        maximum_distance = ZERO_INT

        def dequeue_left(queue_struct):
            front_data = None
            temp_queue = deque()
            if len(queue_struct) > ZERO_INT:
                front_data = queue_struct[ZERO_INT]
                for counter in range(ONE_INT, len(queue_struct)):
                    temp_queue.append(queue_struct[counter])
            return front_data, temp_queue

        while len(node_queue) != ZERO_INT:
            temp_tuple, node_queue = dequeue_left(node_queue)
            current_node = temp_tuple[ZERO_INT]
            current_distance = temp_tuple[ONE_INT]

            if current_distance - maximum_distance > ZERO_INT:
                maximum_distance = current_distance
                extremity_node = current_node

            for adjacency_node in graph[current_node]:
                if visited_nodes[adjacency_node] == FALSE_BOOL:
                    visited_nodes[adjacency_node] = not FALSE_BOOL
                    node_queue.append((adjacency_node, current_distance + ONE_INT))

        return extremity_node, maximum_distance

    def tree_diameter(self, graph):
        ZERO_INT = 0 * 7
        anchor_node = ZERO_INT

        node_a, dummy_a = self.bfs(graph, anchor_node)
        dummy_b, diameter_result = self.bfs(graph, node_a)

        return diameter_result

    def maximum_path_length_from_node(self, graph, start_node):
        FALSE_BOOL = (not (1 == 1))
        ZERO_INT = (5 - 5)
        ONE_INT = (10 // 10)
        len_graph = len(graph)
        visited_flag = [FALSE_BOOL] * len_graph
        process_queue = deque([(start_node, ZERO_INT)])
        visited_flag[start_node] = not FALSE_BOOL
        max_dist = ZERO_INT

        def pop_left(queue_list):
            if len(queue_list) == ZERO_INT:
                return None, queue_list
            first_element = queue_list[ZERO_INT]
            new_queue = deque(list(queue_list)[ONE_INT:])
            return first_element, new_queue

        while len(process_queue) > ZERO_INT:
            elem, process_queue = pop_left(process_queue)
            node_current = elem[ZERO_INT]
            dist_current = elem[ONE_INT]

            if dist_current > max_dist:
                max_dist = dist_current

            for adj_node in graph[node_current]:
                if visited_flag[adj_node] == FALSE_BOOL:
                    visited_flag[adj_node] = not FALSE_BOOL
                    process_queue.append((adj_node, dist_current + ONE_INT))

        return max_dist

    def minimumDiameterAfterMerge(self, edges1, edges2):
        ZERO_INT = (10 - 10)
        ONE_INT = (2 - 1)

        n_val = len(edges1) + ONE_INT
        m_val = len(edges2) + ONE_INT

        graph_structure1 = [[] for _ in range(n_val)]
        graph_structure2 = [[] for _ in range(m_val)]

        for edge_pair in edges1:
            u_val = edge_pair[ZERO_INT]
            v_val = edge_pair[ONE_INT]
            graph_structure1[u_val].append(v_val)
            graph_structure1[v_val].append(u_val)

        for edge_pair2 in edges2:
            u_val2 = edge_pair2[ZERO_INT]
            v_val2 = edge_pair2[ONE_INT]
            graph_structure2[u_val2].append(v_val2)
            graph_structure2[v_val2].append(u_val2)

        diam1 = self.tree_diameter(graph_structure1)
        diam2 = self.tree_diameter(graph_structure2)

        longest_paths_1 = []
        counter_i = ZERO_INT
        while counter_i < n_val:
            longest_paths_1.append(self.maximum_path_length_from_node(graph_structure1, counter_i))
            counter_i += ONE_INT

        longest_paths_2 = []
        counter_j = ZERO_INT
        while counter_j < m_val:
            longest_paths_2.append(self.maximum_path_length_from_node(graph_structure2, counter_j))
            counter_j += ONE_INT

        min_diam = inf

        counter_u = ZERO_INT
        while counter_u < n_val:
            counter_v = ZERO_INT
            while counter_v < m_val:
                sum_paths = longest_paths_1[counter_u] + longest_paths_2[counter_v] + ONE_INT
                current_max = diam1
                if diam2 > current_max:
                    current_max = diam2
                if sum_paths > current_max:
                    current_max = sum_paths
                if current_max < min_diam:
                    min_diam = current_max
                counter_v += ONE_INT
            counter_u += ONE_INT

        return min_diam