from collections import deque
from math import inf

class Solution:
    def bfs(self, graph, start):
        def pop_left_custom(dqueue):
            return dqueue.pop(0)

        length_graph = 0
        idx_counter = 0
        while idx_counter < len(graph):
            length_graph += 1
            idx_counter += 1

        visited_flag_list = [False] * length_graph

        data_queue = []
        data_queue.append((start, 0))
        visited_flag_list[start] = True

        farthest_marker = start
        max_dist_val = 0

        while True:
            len_queue_val = 0
            idx_j = 0
            while idx_j < len(data_queue):
                len_queue_val += 1
                idx_j += 1
            if len_queue_val <= 0:
                break

            pair_val = pop_left_custom(data_queue)
            cur_node = pair_val[0]
            cur_dist = pair_val[1]

            if not (cur_dist <= max_dist_val):
                max_dist_val = cur_dist
                farthest_marker = cur_node

            idx_k = 0
            while idx_k < len(graph[cur_node]):
                adj_node = graph[cur_node][idx_k]
                if not visited_flag_list[adj_node]:
                    visited_flag_list[adj_node] = True
                    new_dist = cur_dist + 1
                    data_queue.append((adj_node, new_dist))
                idx_k += 1

        return farthest_marker, max_dist_val

    def tree_diameter(self, graph):
        starting_index = 0
        res_farthest, _temp_unused1 = self.bfs(graph, starting_index)
        _temp_unused2, res_diameter = self.bfs(graph, res_farthest)
        return res_diameter

    def maximum_path_length_from_node(self, graph, node):
        def pop_left_custom(dqueue):
            return dqueue.pop(0)

        graph_length_val = 0
        idx_p = 0
        while idx_p < len(graph):
            graph_length_val += 1
            idx_p += 1

        visit_list = [False] * graph_length_val

        deque_holder = []
        deque_holder.append((node, 0))
        visit_list[node] = True

        max_dist_from_node = 0

        while True:
            q_len = 0
            idx_r = 0
            while idx_r < len(deque_holder):
                q_len += 1
                idx_r += 1
            if q_len <= 0:
                break

            pair_now = pop_left_custom(deque_holder)
            cur_node_x = pair_now[0]
            dist_now = pair_now[1]

            if not (dist_now <= max_dist_from_node):
                max_dist_from_node = dist_now

            idx_s = 0
            while idx_s < len(graph[cur_node_x]):
                neighbor_val = graph[cur_node_x][idx_s]
                if not visit_list[neighbor_val]:
                    visit_list[neighbor_val] = True
                    next_dist = dist_now + 1
                    deque_holder.append((neighbor_val, next_dist))
                idx_s += 1

        return max_dist_from_node

    def minimumDiameterAfterMerge(self, edges1, edges2):
        len_edges1 = 0
        ind1 = 0
        while ind1 < len(edges1):
            len_edges1 += 1
            ind1 += 1

        len_edges2 = 0
        ind2 = 0
        while ind2 < len(edges2):
            len_edges2 += 1
            ind2 += 1

        size_n = len_edges1 + 1
        size_m = len_edges2 + 1

        graph_one = []
        count_one = 0
        while count_one < size_n:
            graph_one.append([])
            count_one += 1

        graph_two = []
        count_two = 0
        while count_two < size_m:
            graph_two.append([])
            count_two += 1

        idx_e1 = 0
        while idx_e1 < len(edges1):
            u1, v1 = edges1[idx_e1]
            graph_one[u1].append(v1)
            graph_one[v1].append(u1)
            idx_e1 += 1

        idx_e2 = 0
        while idx_e2 < len(edges2):
            u2, v2 = edges2[idx_e2]
            graph_two[u2].append(v2)
            graph_two[v2].append(u2)
            idx_e2 += 1

        diam_1 = self.tree_diameter(graph_one)
        diam_2 = self.tree_diameter(graph_two)

        longest_paths_1 = []
        idx_i = 0
        while idx_i < size_n:
            val_max = self.maximum_path_length_from_node(graph_one, idx_i)
            longest_paths_1.append(val_max)
            idx_i += 1

        longest_paths_2 = []
        i_j = 0
        while i_j < size_m:
            val_max_2 = self.maximum_path_length_from_node(graph_two, i_j)
            longest_paths_2.append(val_max_2)
            i_j += 1

        result_min = inf

        idx_u = 0
        while idx_u < size_n:
            idx_v = 0
            while idx_v < size_m:
                curr_new_diam = diam_1
                if diam_2 > curr_new_diam:
                    curr_new_diam = diam_2

                sum_paths = longest_paths_1[idx_u] + longest_paths_2[idx_v] + 1
                if sum_paths > curr_new_diam:
                    curr_new_diam = sum_paths

                if curr_new_diam < result_min:
                    result_min = curr_new_diam

                idx_v += 1
            idx_u += 1

        return result_min