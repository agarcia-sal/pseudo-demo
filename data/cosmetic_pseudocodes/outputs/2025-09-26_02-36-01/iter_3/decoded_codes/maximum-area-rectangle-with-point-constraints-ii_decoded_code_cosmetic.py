from bisect import bisect_left

class Fenwick:
    def __init__(self, n):
        length_plus_one = n + 1
        zero_filled_list = [0] * length_plus_one
        self.tree = zero_filled_list

    def add(self, i):
        while i < len(self.tree):
            self.tree[i] += 1
            neg_i = -i
            mask = i & neg_i
            i += mask

    def pre(self, i):
        accumulator = 0
        while i > 0:
            accumulator += self.tree[i]
            i = i & (i - 1)
        return accumulator

    def query(self, l, r):
        prefix_r = self.pre(r)
        prefix_l_minus_one = self.pre(l - 1)
        difference = prefix_r - prefix_l_minus_one
        return difference


class Solution:
    def maxRectangleArea(self, xCoord, yCoord):
        zipped_pairs = [(xCoord[i], yCoord[i]) for i in range(len(xCoord))]
        zipped_pairs.sort(key=lambda p: (p[0], p[1]))
        unique_sorted_ys = sorted(set(yCoord))
        max_area_so_far = -1
        fenwicks_length = len(unique_sorted_ys)
        fenwick_tree_instance = Fenwick(fenwicks_length)
        first_point_y_index_raw = bisect_left(unique_sorted_ys, zipped_pairs[0][1])
        first_point_y_index = first_point_y_index_raw + 1
        fenwick_tree_instance.add(first_point_y_index)
        pre_map = {}
        total_points = len(zipped_pairs)
        idx = 0
        while idx < total_points - 1:
            tuple_curr = zipped_pairs[idx]
            tuple_next = zipped_pairs[idx + 1]
            curr_x, curr_y = tuple_curr
            next_x, next_y = tuple_next
            next_y_pos_raw = bisect_left(unique_sorted_ys, next_y)
            next_y_pos = next_y_pos_raw + 1
            fenwick_tree_instance.add(next_y_pos)
            if curr_x != next_x:
                idx += 1
                continue
            curr_y_pos_raw = bisect_left(unique_sorted_ys, curr_y)
            curr_y_pos = curr_y_pos_raw + 1
            current_query_value = fenwick_tree_instance.query(curr_y_pos, next_y_pos)
            if next_y in pre_map:
                stored_x, stored_y, stored_val = pre_map[next_y]
                condition1 = (stored_y == curr_y)
                condition2 = ((stored_val + 2) == current_query_value)
                if condition1 and condition2:
                    candidate_area = (next_x - stored_x) * (next_y - curr_y)
                    if candidate_area > max_area_so_far:
                        max_area_so_far = candidate_area
            pre_map[next_y] = (curr_x, curr_y, current_query_value)
            idx += 1
        return max_area_so_far