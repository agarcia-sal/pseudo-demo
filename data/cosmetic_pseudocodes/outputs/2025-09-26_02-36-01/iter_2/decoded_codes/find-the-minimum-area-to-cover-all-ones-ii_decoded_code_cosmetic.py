from math import inf
from itertools import combinations

class Solution:
    def minimumSum(self, grid):
        coordinates = []
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    coordinates.append((x, y))

        def rect_area(points):
            if len(points) == 0:
                return 0
            rows = [p[0] for p in points]
            cols = [p[1] for p in points]

            min_row = max_row = rows[0]
            min_col = max_col = cols[0]

            for idx in range(1, len(rows)):
                if rows[idx] < min_row:
                    min_row = rows[idx]
                elif rows[idx] > max_row:
                    max_row = rows[idx]

                if cols[idx] < min_col:
                    min_col = cols[idx]
                elif cols[idx] > max_col:
                    max_col = cols[idx]

            width = (max_row - min_row) + 1
            height = (max_col - min_col) + 1

            return width * height

        minimum_total = inf
        total_points = len(coordinates)

        # We choose a, b, c such that 0 < a < b < c <= total_points and these are counts of points forming subsets
        # But as per pseudocode a starts from 1 to total_points-2, b from a+1 to total_points-1, c from b+1 to total_points
        # The subsets subsets sizes are:
        # subset1 size = a
        # subset2 size = b - a
        # subset3 size = total_points - b (derived from leftover points)
        # Make sure subsets are disjoint and cover all coordinates

        for a in range(1, total_points - 1):
            for b in range(a + 1, total_points):
                c = total_points  # c varies up to total_points; actually the third subset size is total_points - b
                # Iterate subset1 of size a from coordinates
                for subset1 in combinations(coordinates, a):
                    set_all = set(coordinates)
                    set_sub1 = set(subset1)
                    leftover_after_sub1 = set_all - set_sub1

                    for subset2 in combinations(leftover_after_sub1, b - a):
                        set_sub2 = set(subset2)
                        subset3 = leftover_after_sub1 - set_sub2

                        area_1 = rect_area(subset1)
                        area_2 = rect_area(subset2)
                        area_3 = rect_area(subset3)

                        if area_1 > 0 and area_2 > 0 and area_3 > 0:
                            sum_areas = area_1 + area_2 + area_3
                            if sum_areas < minimum_total:
                                minimum_total = sum_areas

        return minimum_total