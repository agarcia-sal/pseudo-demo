from math import inf
from itertools import combinations

class Solution:
    def minimumSum(self, grid):
        ones = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == 1]

        def rect_area(points):
            if len(points) == 0:
                return 0
            min_i = min(p[0] for p in points)
            max_i = max(p[0] for p in points)
            min_j = min(p[1] for p in points)
            max_j = max(p[1] for p in points)
            width = max_i - min_i + 1
            height = max_j - min_j + 1
            return width * height

        min_sum = inf
        n = len(ones)

        # i, j, k are counts of elements in the subsets
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                k = n - j
                if k < 1:
                    continue
                all_ones_set = set(ones)
                for comb1 in combinations(ones, i):
                    set_comb1 = set(comb1)
                    remaining_after_comb1 = all_ones_set - set_comb1
                    for comb2 in combinations(remaining_after_comb1, j - i):
                        set_comb2 = set(comb2)
                        comb3 = remaining_after_comb1 - set_comb2
                        area1 = rect_area(comb1)
                        area2 = rect_area(comb2)
                        area3 = rect_area(comb3)
                        if area1 > 0 and area2 > 0 and area3 > 0:
                            current_sum = area1 + area2 + area3
                            if current_sum < min_sum:
                                min_sum = current_sum

        return min_sum