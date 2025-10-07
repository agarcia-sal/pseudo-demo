from collections import defaultdict
from math import inf

class Solution:
    def minimumTime(self, n, edges, disappear):
        adjacency_map = defaultdict(list)
        for edge_item in edges:
            node_a, node_b, edge_len = edge_item
            adjacency_map[node_a].append((node_b, edge_len))
            adjacency_map[node_b].append((node_a, edge_len))

        dist_array = [inf] * n
        dist_array[0] = 0

        heap_list = []

        def push_heap(heap_container, val):
            heap_container.append(val)
            pos = len(heap_container) - 1
            while pos > 0:
                parent_pos = (pos - 1) // 2
                if heap_container[parent_pos][0] > heap_container[pos][0]:
                    heap_container[parent_pos], heap_container[pos] = heap_container[pos], heap_container[parent_pos]
                    pos = parent_pos
                else:
                    break

        def pop_heap(heap_container):
            if not heap_container:
                return None
            top_val = heap_container[0]
            last_element = heap_container[-1]
            heap_container[0] = last_element
            heap_container.pop()
            pos = 0
            size = len(heap_container)
            while True:
                left_child = pos * 2 + 1
                right_child = pos * 2 + 2
                smallest = pos

                if left_child < size and heap_container[left_child][0] < heap_container[smallest][0]:
                    smallest = left_child
                if right_child < size and heap_container[right_child][0] < heap_container[smallest][0]:
                    smallest = right_child
                if smallest != pos:
                    heap_container[pos], heap_container[smallest] = heap_container[smallest], heap_container[pos]
                    pos = smallest
                else:
                    break
            return top_val

        def is_empty(collection):
            return len(collection) == 0

        def is_not_empty(collection):
            return not is_empty(collection)

        def process_heap():
            if is_empty(heap_list):
                return
            current_pair = pop_heap(heap_list)
            curr_dist, curr_node = current_pair

            if curr_dist >= disappear[curr_node] or curr_dist > dist_array[curr_node]:
                process_heap()
                return

            neighbors = adjacency_map[curr_node]
            idx2 = 0
            limit2 = len(neighbors)
            while True:
                if idx2 >= limit2:
                    break
                neighbor_node, length_edge = neighbors[idx2]
                new_distance = curr_dist + length_edge
                if new_distance < dist_array[neighbor_node] and new_distance < disappear[neighbor_node]:
                    dist_array[neighbor_node] = new_distance
                    push_heap(heap_list, (new_distance, neighbor_node))
                idx2 += 1

            process_heap()

        push_heap(heap_list, (0, 0))
        process_heap()

        output_arr = [-1] * n
        index_var = n - 1
        while index_var >= 0:
            if dist_array[index_var] < disappear[index_var]:
                output_arr[index_var] = dist_array[index_var]
            index_var -= 1

        return output_arr