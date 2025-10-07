from math import inf
from itertools import combinations

class Solution:
    def minimumSum(self, grid):
        ones = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == 1]

        def rect_area(points):
            if not points:
                return 0
            rows = [p[0] for p in points]
            cols = [p[1] for p in points]
            min_row, max_row = min(rows), max(rows)
            min_col, max_col = min(cols), max(cols)
            width = max_row - min_row + 1
            height = max_col - min_col + 1
            return width * height

        min_sum = inf
        total_ones = len(ones)

        # We want idx1 < idx2 < idx3 with idx3 == total_ones, so idx3 is fixed as total_ones
        # Reformulate idx1 in [1, total_ones-2], idx2 in [idx1+1, total_ones-1], idx3 = total_ones
        # Since the pseudocode is 1-based indexing, python is 0-based and combinations use length as counts.
        # We'll interpret idx1, idx2, idx3 as sizes of groups that partition ones into three subsets:
        # subset_1 size idx1,
        # subset_2 size idx2 - idx1,
        # subset_3 size idx3 - idx2 (which is total_ones - idx2)

        # To avoid repeated calculating all combinations of the entire list multiple times,
        # we iterate over all possible splits of sizes and then try all combinations for subset_1,
        # and then subset_2 from the remaining elements.

        for idx1 in range(1, total_ones - 1):
            for idx2 in range(idx1 + 1, total_ones):
                len_subset_1 = idx1
                len_subset_2 = idx2 - idx1
                len_subset_3 = total_ones - idx2
                if len_subset_3 <= 0:
                    continue

                # Generate all combinations for subset 1
                for subset_1 in combinations(ones, len_subset_1):
                    set_ones = set(ones)
                    set_subset_1 = set(subset_1)
                    remaining_after_1 = set_ones - set_subset_1
                    # Generate all combinations for subset 2 from remaining_after_1
                    # To use combinations on a set, convert to sorted list for determinism
                    rem_list = sorted(remaining_after_1)
                    for subset_2 in combinations(rem_list, len_subset_2):
                        set_subset_2 = set(subset_2)
                        subset_3 = remaining_after_1 - set_subset_2
                        area_1 = rect_area(subset_1)
                        area_2 = rect_area(subset_2)
                        area_3 = rect_area(subset_3)
                        if area_1 > 0 and area_2 > 0 and area_3 > 0:
                            total_area = area_1 + area_2 + area_3
                            if total_area < min_sum:
                                min_sum = total_area

        return min_sum if min_sum != inf else 0