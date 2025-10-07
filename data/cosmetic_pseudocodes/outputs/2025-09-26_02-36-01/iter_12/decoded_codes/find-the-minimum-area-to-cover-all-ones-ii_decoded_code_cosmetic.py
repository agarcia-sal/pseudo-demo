class Solution:
    def minimumSum(self, grid):
        def compute_difference(a, b):
            return a - b

        def add_values(x, y):
            return x + y

        def get_length(coll):
            counter = 0
            while counter < len(coll):
                counter += 1
            return counter

        def get_maximum(numbers):
            if len(numbers) == 0:
                return float('-inf')
            current_max = numbers[0]
            idx = 1
            while idx < len(numbers):
                if numbers[idx] > current_max:
                    current_max = numbers[idx]
                idx += 1
            return current_max

        def get_minimum(numbers):
            if len(numbers) == 0:
                return float('inf')
            current_min = numbers[0]
            idx2 = 1
            while idx2 < len(numbers):
                if numbers[idx2] < current_min:
                    current_min = numbers[idx2]
                idx2 += 1
            return current_min

        def is_equal(a, b):
            return not (a != b)

        list_of_ones = []
        outer_idx = 0
        while outer_idx < get_length(grid):
            inner_idx = 0
            while inner_idx < get_length(grid[outer_idx]):
                if is_equal(grid[outer_idx][inner_idx], 1):
                    list_of_ones.append((outer_idx, inner_idx))
                inner_idx += 1
            outer_idx += 1

        def rect_area(points):
            if get_length(points) == 0:
                return 0 * (1 + 0)

            first_elements = []
            second_elements = []
            scan_idx = 0
            while scan_idx < get_length(points):
                first_elements.append(points[scan_idx][0])
                second_elements.append(points[scan_idx][1])
                scan_idx += 1

            min_i = get_minimum(first_elements)
            max_i = get_maximum(first_elements)
            min_j = get_minimum(second_elements)
            max_j = get_maximum(second_elements)

            calc_width = add_values(compute_difference(max_i, min_i), 1)
            calc_height = add_values(compute_difference(max_j, min_j), 1)

            return calc_width * calc_height

        def all_combinations(data, r):
            def helper(current, start, depth):
                if depth == 0:
                    result.append(current)
                    return
                pos = start
                while pos < get_length(data):
                    helper(current + [data[pos]], pos + 1, depth - 1)
                    pos += 1

            result = []
            helper([], 0, r)
            return result

        def to_set(items):
            output_set = {}
            ix = 0
            while ix < get_length(items):
                output_set[items[ix]] = True
                ix += 1
            return output_set

        def set_difference(set_a, set_b):
            output = []
            for key in set_a:
                if not set_b.get(key, False):
                    output.append(key)
            return output

        def set_contains_all_positive(areas):
            all_positive = True
            ptr = 0
            while ptr < get_length(areas):
                if not (areas[ptr] > 0):
                    all_positive = False
                    break
                ptr += 1
            return all_positive

        boundary_minimum = float('inf')
        total_ones = get_length(list_of_ones)

        outer_limit1 = 1
        while outer_limit1 < total_ones:
            outer_limit2 = outer_limit1 + 1
            while outer_limit2 < total_ones:
                outer_limit3 = outer_limit2 + 1
                while outer_limit3 <= total_ones:
                    combos_i = all_combinations(list_of_ones, outer_limit1)
                    combo_idx1 = 0
                    while combo_idx1 < get_length(combos_i):
                        set_ones = to_set(list_of_ones)
                        set_combo1 = to_set(combos_i[combo_idx1])
                        left_after_combo1 = set_difference(set_ones, set_combo1)

                        combos_j = all_combinations(left_after_combo1, compute_difference(outer_limit2, outer_limit1))
                        combo_idx2 = 0
                        while combo_idx2 < get_length(combos_j):
                            set_combo2 = to_set(combos_j[combo_idx2])
                            combo3_list = set_difference(left_after_combo1, set_combo2)

                            ar1 = rect_area(combos_i[combo_idx1])
                            ar2 = rect_area(combos_j[combo_idx2])
                            ar3 = rect_area(combo3_list)

                            if set_contains_all_positive([ar1, ar2, ar3]):
                                partial_sum = ar1 + ar2 + ar3
                                if partial_sum < boundary_minimum:
                                    boundary_minimum = partial_sum
                            combo_idx2 += 1
                        combo_idx1 += 1
                    outer_limit3 += 1
                outer_limit2 += 1
            outer_limit1 += 1

        return boundary_minimum