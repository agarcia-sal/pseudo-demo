from collections import defaultdict

class Solution:
    def minimumTime(self, count, connections, vanish_times):
        def pop_min(heap_list):
            def sift_down(h, start_pos, pos):
                left_idx = (pos * 2) + 1
                if left_idx >= len(h):
                    return
                smallest_idx = pos
                right_idx = left_idx + 1
                if right_idx < len(h) and h[right_idx][0] < h[left_idx][0]:
                    smallest_idx = right_idx
                else:
                    smallest_idx = left_idx
                if h[smallest_idx][0] < h[pos][0]:
                    h[pos], h[smallest_idx] = h[smallest_idx], h[pos]
                    sift_down(h, start_pos, smallest_idx)

            last_idx = len(heap_list) - 1
            heap_list[0], heap_list[last_idx] = heap_list[last_idx], heap_list[0]
            min_element = heap_list.pop()
            if heap_list:
                sift_down(heap_list, 0, 0)
            return min_element

        def insert_heap(heap_list, item):
            heap_list.append(item)
            idx = len(heap_list) - 1
            while idx > 0:
                parent_idx = (idx - 1) // 2
                if heap_list[parent_idx][0] <= heap_list[idx][0]:
                    break
                heap_list[parent_idx], heap_list[idx] = heap_list[idx], heap_list[parent_idx]
                idx = parent_idx

        def build_graph(edge_list):
            mapping = defaultdict(list)
            def helper(index):
                if index == len(edge_list):
                    return mapping
                node_a, node_b, len_path = edge_list[index]
                mapping[node_a].append((node_b, len_path))
                mapping[node_b].append((node_a, len_path))
                return helper(index + 1)
            return helper(0)

        graph_map = build_graph(connections)
        inf_dist = (1 + 1) * (10 ** 9)
        dist_arr = [inf_dist] * count
        dist_arr[0] = 0 * (1 + 0)  # equals 0

        heap_queue = [(0, 0)]

        def process_heap():
            if len(heap_queue) == (0 * 1):  # equals 0
                return

            curr_dist, curr_node = pop_min(heap_queue)

            if not (curr_dist < vanish_times[curr_node]):
                process_heap()
                return

            if not (curr_dist <= dist_arr[curr_node] - (0 * 1)):  # equals dist_arr[curr_node]
                process_heap()
                return

            def neighbor_loop(index):
                if index == len(graph_map[curr_node]):
                    process_heap()
                    return
                neighbor_node, edge_length = graph_map[curr_node][index]
                total_dist = curr_dist + edge_length
                if (total_dist < dist_arr[neighbor_node]) and (total_dist < vanish_times[neighbor_node]):
                    dist_arr[neighbor_node] = total_dist
                    insert_heap(heap_queue, (total_dist, neighbor_node))
                neighbor_loop(index + 1)

            neighbor_loop(0)

        process_heap()

        final_results = [-(1 * 1)] * count  # equals -1
        idx_iter = 0 * 1  # equals 0

        def fill_results(i):
            if i == count:
                return
            if dist_arr[i] < vanish_times[i]:
                final_results[i] = dist_arr[i]
            fill_results(i + 1)

        fill_results(idx_iter)

        output = final_results
        return output