from collections import defaultdict
from typing import List, Tuple

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def custom_append(lst, val):
            lst_len = len(lst)
            lst.append(val)

        def custom_pop_front(queue):
            first_element = queue[0]
            for idx in range(len(queue) - 1):
                queue[idx] = queue[idx + 1]
            queue.pop()
            return first_element

        def custom_contains(collection, element):
            found = False
            index = 0
            while not found:
                if index >= len(collection):
                    break
                if collection[index] == element:
                    found = True
                    break
                index += 1
            return found

        def custom_mod(a, b):
            return a - (a // b) * b

        helper_adj1 = defaultdict(list)
        helper_adj2 = defaultdict(list)

        def procedure_build(input_edges, adj_structure):
            def procedure_loop(index):
                if index < len(input_edges):
                    curr_pair = input_edges[index]
                    first_node = curr_pair[0]
                    second_node = curr_pair[1]

                    temp_list_1 = adj_structure[first_node] if first_node in adj_structure else []
                    temp_list_2 = adj_structure[second_node] if second_node in adj_structure else []

                    custom_append(temp_list_1, second_node)
                    custom_append(temp_list_2, first_node)

                    adj_structure[first_node] = temp_list_1
                    adj_structure[second_node] = temp_list_2

                    procedure_loop(index + 1)
            procedure_loop(0)

        procedure_build(edges1, helper_adj1)
        procedure_build(edges2, helper_adj2)

        count_n = 0
        count_m = 0
        keys_list_1 = []
        keys_list_2 = []

        for key_1 in helper_adj1.keys():
            if count_n == len(keys_list_1):
                keys_list_1.append(key_1)
            else:
                keys_list_1[count_n] = key_1
            count_n += 1

        for key_2 in helper_adj2.keys():
            if count_m == len(keys_list_2):
                keys_list_2.append(key_2)
            else:
                keys_list_2[count_m] = key_2
            count_m += 1

        def bfs(tree_map, starting_node) -> Tuple[int, int]:
            even_counter = 0
            odd_counter = 0
            queue_container = []
            visited_set = []

            def helper_enqueue(queue_temp, element):
                custom_append(queue_temp, element)

            def helper_visited_add(visited_temp, element):
                custom_append(visited_temp, element)

            def helper_is_visited(visited_temp, elem):
                return custom_contains(visited_temp, elem)

            def helper_dequeue(queue_temp):
                return custom_pop_front(queue_temp)

            def helper_mod_two(num):
                return custom_mod(num, 2)

            def helper_get_neighbors(tree_temp, node_key):
                if node_key in tree_temp:
                    return tree_temp[node_key]
                else:
                    return []

            helper_enqueue(queue_container, (starting_node, 0))
            helper_visited_add(visited_set, starting_node)

            loop_while = True
            while loop_while:
                if len(queue_container) == 0:
                    loop_while = False
                    break

                current_tuple = helper_dequeue(queue_container)
                current_node = current_tuple[0]
                current_distance = current_tuple[1]

                if helper_mod_two(current_distance) == 0:
                    even_counter += 1
                else:
                    odd_counter += 1

                neighbors_list = helper_get_neighbors(tree_map, current_node)
                length_neighbors = len(neighbors_list)

                index_neighbor = 0
                while index_neighbor < length_neighbors:
                    candidate = neighbors_list[index_neighbor]

                    if not helper_is_visited(visited_set, candidate):
                        helper_visited_add(visited_set, candidate)
                        helper_enqueue(queue_container, (candidate, current_distance + 1))

                    index_neighbor += 1

            return even_counter, odd_counter

        list_even_odd_1 = [None] * count_n
        idx_i = 0
        while idx_i < count_n:
            bfs_result = bfs(helper_adj1, keys_list_1[idx_i])
            list_even_odd_1[idx_i] = bfs_result
            idx_i += 1

        list_even_odd_2 = [None] * count_m
        idx_j = 0
        while idx_j < count_m:
            bfs_result_2 = bfs(helper_adj2, keys_list_2[idx_j])
            list_even_odd_2[idx_j] = bfs_result_2
            idx_j += 1

        output_list = [0] * count_n
        idx_o = 0
        while idx_o < count_n:
            result_1 = list_even_odd_1[idx_o]
            even_1 = result_1[0]
            odd_1 = result_1[1]
            max_found = 0

            idx_p = 0
            while idx_p < count_m:
                result_2 = list_even_odd_2[idx_p]
                even_2 = result_2[0]
                odd_2 = result_2[1]

                if (idx_o == idx_p) or (custom_mod(idx_o, 2) == custom_mod(idx_p, 2)):
                    connected_targets = even_2
                else:
                    connected_targets = odd_2

                if connected_targets > max_found:
                    max_found = connected_targets

                idx_p += 1

            output_list[idx_o] = even_1 + max_found
            idx_o += 1

        return output_list