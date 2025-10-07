from collections import defaultdict
from math import inf

class Solution:
    def minimumTime(self, n, edges, disappear):
        def custom_push(heap_list, item):
            index_var = len(heap_list)
            heap_list.append(item)
            while index_var > 0:
                parent_var = (index_var - 1) // 2
                if heap_list[parent_var][0] <= heap_list[index_var][0]:
                    break
                heap_list[parent_var], heap_list[index_var] = heap_list[index_var], heap_list[parent_var]
                index_var = parent_var

        def custom_pop(heap_list):
            return_item = heap_list[0]
            last_item = heap_list.pop()
            if not heap_list:
                return return_item
            heap_list[0] = last_item
            current_index = 0
            heap_size = len(heap_list)
            while True:
                left_child = 2 * current_index + 1
                right_child = 2 * current_index + 2
                smallest_index = current_index

                if left_child < heap_size and heap_list[left_child][0] < heap_list[smallest_index][0]:
                    smallest_index = left_child
                if right_child < heap_size and heap_list[right_child][0] < heap_list[smallest_index][0]:
                    smallest_index = right_child
                if smallest_index == current_index:
                    break
                heap_list[current_index], heap_list[smallest_index] = heap_list[smallest_index], heap_list[current_index]
                current_index = smallest_index

            return return_item

        def create_graph(edge_list):
            map_var = defaultdict(list)
            for first_val, second_val, third_val in edge_list:
                map_var[first_val].append((second_val, third_val))
                map_var[second_val].append((first_val, third_val))
            return map_var

        def init_array(length_val, init_val):
            arr_var = []
            counter_var = 0
            while counter_var < length_val:
                arr_var.append(init_val)
                counter_var += 1
            return arr_var

        graph_data = create_graph(edges)
        dist_array = init_array(n, inf)
        dist_array[0] = 0
        heap_store = [(0, 0)]

        while len(heap_store) > 0:
            curr_dist, curr_node = custom_pop(heap_store)
            if curr_dist >= disappear[curr_node]:
                continue
            if curr_dist > dist_array[curr_node]:
                continue

            for nbr, len_val in graph_data[curr_node]:
                tentative_dist = curr_dist + len_val
                if tentative_dist < dist_array[nbr] and tentative_dist < disappear[nbr]:
                    dist_array[nbr] = tentative_dist
                    custom_push(heap_store, (tentative_dist, nbr))

        outcome_array = init_array(n, -1)
        idx_var = 0
        while idx_var < n:
            if dist_array[idx_var] < disappear[idx_var]:
                outcome_array[idx_var] = dist_array[idx_var]
            idx_var += 1

        return outcome_array