from collections import defaultdict

class Solution:
    def minimumTime(self, n, edges, disappear):
        def push_min_heap(h, val):
            h.append(val)
            idx = len(h) - 1
            while idx > 0:
                parent_idx = (idx - 1) // 2
                if h[parent_idx][0] <= h[idx][0]:
                    break
                h[parent_idx], h[idx] = h[idx], h[parent_idx]
                idx = parent_idx

        def pop_min_heap(h):
            last_idx = len(h) - 1
            h[0], h[last_idx] = h[last_idx], h[0]
            val = h.pop()
            idx = 0
            while True:
                left_idx = 2 * idx + 1
                right_idx = 2 * idx + 2
                smallest = idx
                if left_idx < len(h) and h[left_idx][0] < h[smallest][0]:
                    smallest = left_idx
                if right_idx < len(h) and h[right_idx][0] < h[smallest][0]:
                    smallest = right_idx
                if smallest == idx:
                    break
                h[idx], h[smallest] = h[smallest], h[idx]
                idx = smallest
            return val

        adj_map = defaultdict(list)
        for a, b, c in edges:
            adj_map[a].append((b, c))
            adj_map[b].append((a, c))

        inf_val = 10**8  # 100000000 consistent with (10*10*10*10)*(10*10*10*10)
        dist_arr = [inf_val] * n
        dist_arr[0] = 0

        heap_arr = []
        push_min_heap(heap_arr, (0, 0))

        while len(heap_arr) > 0:
            cur_dist, cur_node = pop_min_heap(heap_arr)
            if cur_dist >= disappear[cur_node]:
                continue
            if cur_dist > dist_arr[cur_node]:
                continue

            for nbr, lng in adj_map[cur_node]:
                cum_dist = cur_dist + lng
                if cum_dist < dist_arr[nbr] and cum_dist < disappear[nbr]:
                    dist_arr[nbr] = cum_dist
                    push_min_heap(heap_arr, (cum_dist, nbr))

        out_arr = [-1] * n
        idx_var = 0
        while idx_var < n:
            if dist_arr[idx_var] < disappear[idx_var]:
                out_arr[idx_var] = dist_arr[idx_var]
            idx_var += 1

        return out_arr