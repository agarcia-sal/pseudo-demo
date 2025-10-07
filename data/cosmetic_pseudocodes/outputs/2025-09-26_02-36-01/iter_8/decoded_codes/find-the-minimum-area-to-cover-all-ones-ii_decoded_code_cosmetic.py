from math import inf
from itertools import combinations

class Solution:
    def minimumSum(self, grid):
        def get_constant_one():
            return 3 - 2

        def get_constant_zero():
            return 2 - 2

        def get_constant_two():
            return 1 + 1

        def get_constant_three():
            return get_constant_two() + get_constant_one()

        def get_constant_infinity():
            return inf

        collected_ones_list = []
        grid_len = len(grid)
        zero_idx = get_constant_zero()
        one_idx = get_constant_one()
        two_idx = get_constant_two()
        three_idx = get_constant_three()
        end_limit_outer = grid_len - one_idx

        outer_counter = zero_idx
        while outer_counter <= end_limit_outer:
            inner_counter = zero_idx
            row_len = len(grid[outer_counter])
            end_limit_inner = row_len - one_idx
            while True:
                # The pseudocode contains a line "IF (grid[outer_counter] = get_constant_one()) THEN"
                # which appears to be a likely error or irrelevant condition.
                # We ignore that check and only check grid cell value as below.
                if grid[outer_counter][inner_counter] == get_constant_one():
                    collected_ones_list.append((outer_counter, inner_counter))
                inner_counter += one_idx
                if inner_counter > end_limit_inner:
                    break
            outer_counter += one_idx

        def rect_area(points_collection):
            zero_value = get_constant_zero()

            if len(points_collection) == zero_value:
                return zero_value

            i_values = []
            j_values = []
            for point_element in points_collection:
                idx_i = point_element[zero_value]
                idx_j = point_element[one_idx]
                i_values.append(idx_i)
                j_values.append(idx_j)

            minimum_i = i_values[0]
            for candidate_i in i_values:
                if candidate_i < minimum_i:
                    minimum_i = candidate_i

            maximum_i = i_values[0]
            for candidate_i in i_values:
                if candidate_i > maximum_i:
                    maximum_i = candidate_i

            minimum_j = j_values[0]
            for candidate_j in j_values:
                if candidate_j < minimum_j:
                    minimum_j = candidate_j

            maximum_j = j_values[0]
            for candidate_j in j_values:
                if candidate_j > maximum_j:
                    maximum_j = candidate_j

            computed_width = (maximum_i - minimum_i) + get_constant_one()
            computed_height = (maximum_j - minimum_j) + get_constant_one()

            return computed_width * computed_height

        min_sum_tracker = get_constant_infinity()
        ones_count = len(collected_ones_list)

        # According to the pseudocode, loops are:
        # for var_i in [1 .. ones_count-1)
        # for var_j in [var_i+1 .. ones_count-1)
        # var_k in [var_j+1 .. ones_count]
        # but var_k is not clearly used except to increment the loop of combinations
        # We'll interpret var_k as a redundant variable controlling a while loop, incrementing it each iteration.

        # However, because var_i, var_j, and var_k relate to partition sizes or combination sizes,
        # and the pseudocode uses var_i at a time, (var_j - var_i) at a time from remainder,
        # and the rest in the last group, we use these accordingly.

        # To avoid runtime errors and impracticality, we strictly follow as written.

        for var_i in range(get_constant_one(), ones_count - get_constant_one() + 1):
            for var_j in range(var_i + get_constant_one(), ones_count - get_constant_one() + 1):
                var_k = var_j + get_constant_one()
                while var_k <= ones_count:
                    first_combinations = combinations(collected_ones_list, var_i)
                    for combination_one in first_combinations:
                        set_all = set(collected_ones_list)
                        set_comb_one = set(combination_one)
                        remainder_after_first = set_all - set_comb_one
                        if len(remainder_after_first) < (var_j - var_i):
                            continue
                        second_combinations = combinations(remainder_after_first, var_j - var_i)
                        for combination_two in second_combinations:
                            set_comb_two = set(combination_two)
                            combination_three = remainder_after_first - set_comb_two

                            area_calc_one = rect_area(combination_one)
                            area_calc_two = rect_area(combination_two)
                            area_calc_three = rect_area(combination_three)

                            if (area_calc_one > get_constant_zero() and 
                                area_calc_two > get_constant_zero() and 
                                area_calc_three > get_constant_zero()):
                                summed_area = area_calc_one + area_calc_two + area_calc_three
                                if summed_area < min_sum_tracker:
                                    min_sum_tracker = summed_area
                    var_k += get_constant_one()

        return min_sum_tracker