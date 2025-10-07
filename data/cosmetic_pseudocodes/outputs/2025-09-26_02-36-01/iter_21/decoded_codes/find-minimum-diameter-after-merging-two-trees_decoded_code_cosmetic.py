from collections import deque
from math import inf

class Solution:
    def bfs(self, graph, start):
        length_var = 0
        visited_list = [False]
        deque_var = [(start, 0)]
        flag_var = False
        node_far = 0
        dist_max = 0

        def init_vars():
            nonlocal length_var, visited_list, deque_var, flag_var, node_far, dist_max
            length_var = len(graph)
            visited_list = []
            def fill_visited():
                counterA = 0
                while counterA < length_var:
                    visited_list.append(False)
                    counterA += 1
            fill_visited()
            deque_var = [(start, 0)]
            flag_var = True
            visited_list[start] = flag_var
            node_far = start
            dist_max = 0
            return visited_list, deque_var, flag_var, node_far, dist_max
        visited_list, deque_var, flag_var, node_far, dist_max = init_vars()

        def dequeue_process():
            nonlocal deque_var
            if len(deque_var) > 0:
                pair_var = deque_var[0]
                deque_var = deque_var[1:]
                return pair_var
            return (None, None)

        def neighbor_iterate(node_in, dist_in):
            idx_var = 0
            temp_list = graph[node_in]
            len_temp = len(temp_list)
            nonlocal visited_list, deque_var
            while idx_var < len_temp:
                adj_node = temp_list[idx_var]
                if not visited_list[adj_node]:
                    visited_list[adj_node] = True
                    deque_var.append((adj_node, dist_in + 1))
                idx_var += 1

        while len(deque_var) > 0:
            current_tuple = dequeue_process()
            current_node, current_dist = current_tuple
            if current_node is None:
                break
            if current_dist > dist_max:
                dist_max = current_dist
                node_far = current_node
            neighbor_iterate(current_node, current_dist)

        return node_far, dist_max

    def tree_diameter(self, graph):
        zero_var = 0
        far_node = 0
        dummy_a = 0
        dummy_b = 0
        diameter_val = 0

        def bfs_call_one():
            nonlocal far_node, dummy_a
            far_node, dummy_a = self.bfs(graph, zero_var)

        def bfs_call_two():
            nonlocal dummy_b, diameter_val
            dummy_b, diameter_val = self.bfs(graph, far_node)

        bfs_call_one()
        bfs_call_two()
        return diameter_val

    def maximum_path_length_from_node(self, graph, node):
        lengthX = 0
        bool_arr = []
        dequeQ = []
        true_flag = True
        max_distX = 0

        def init_setup():
            nonlocal lengthX, bool_arr, dequeQ, max_distX
            lengthX = len(graph)
            countI = 0
            while countI < lengthX:
                bool_arr.append(False)
                countI += 1
            dequeQ = [(node, 0)]
            bool_arr[node] = true_flag
            max_distX = 0
            return bool_arr, dequeQ, max_distX

        bool_arr, dequeQ, max_distX = init_setup()

        def pop_left():
            nonlocal dequeQ
            ret_tuple = dequeQ[0]
            dequeQ = dequeQ[1:]
            return ret_tuple

        def visit_neighbors(currentN, distN):
            indexK = 0
            neighbors_list = graph[currentN]
            lenN = len(neighbors_list)
            nonlocal bool_arr, dequeQ
            while indexK < lenN:
                next_node = neighbors_list[indexK]
                if not bool_arr[next_node]:
                    bool_arr[next_node] = True
                    dequeQ.append((next_node, distN + 1))
                indexK += 1

        while len(dequeQ) > 0:
            nodeDist = pop_left()
            actual_node, dist_val = nodeDist
            if dist_val > max_distX:
                max_distX = dist_val
            visit_neighbors(actual_node, dist_val)

        return max_distX

    def minimumDiameterAfterMerge(self, edges1, edges2):
        lenN = len(edges1) + 1
        lenM = len(edges2) + 1

        graphA = []
        graphB = []

        def create_empty_lists():
            nonlocal graphA, graphB
            cntX = 0
            while cntX < lenN:
                graphA.append([])
                cntX += 1
            cntY = 0
            while cntY < lenM:
                graphB.append([])
                cntY += 1

        create_empty_lists()

        def add_edges(list_of_edges, target_graph):
            counterE = 0
            maxE = len(list_of_edges)
            while counterE < maxE:
                pair_edge = list_of_edges[counterE]
                u_node, v_node = pair_edge
                target_graph[u_node].append(v_node)
                target_graph[v_node].append(u_node)
                counterE += 1

        add_edges(edges1, graphA)
        add_edges(edges2, graphB)

        diameterA = self.tree_diameter(graphA)
        diameterB = self.tree_diameter(graphB)

        longest_from_nodesA = []
        longest_from_nodesB = []

        def fill_longest_A():
            nonlocal longest_from_nodesA
            iterI = 0
            while iterI < lenN:
                valA = self.maximum_path_length_from_node(graphA, iterI)
                longest_from_nodesA.append(valA)
                iterI += 1

        def fill_longest_B():
            nonlocal longest_from_nodesB
            iterJ = 0
            while iterJ < lenM:
                valB = self.maximum_path_length_from_node(graphB, iterJ)
                longest_from_nodesB.append(valB)
                iterJ += 1

        fill_longest_A()
        fill_longest_B()

        min_d = inf
        outer_idx = 0
        while outer_idx < lenN:
            inner_idx = 0
            while inner_idx < lenM:
                combined_max = longest_from_nodesA[outer_idx] + longest_from_nodesB[inner_idx] + 1
                cur_max = diameterA
                if diameterB > cur_max:
                    cur_max = diameterB
                if combined_max > cur_max:
                    cur_max = combined_max
                if cur_max < min_d:
                    min_d = cur_max
                inner_idx += 1
            outer_idx += 1

        return min_d