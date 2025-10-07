from typing import List
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

class Solution:
    def numberOfPairs(self, points: List[Point]) -> int:
        # Sort points by ascending x, then descending y
        sorted_points = sorted(points, key=lambda p: (p.x, -p.y))
        total_points = len(sorted_points)
        pair_count = 0
        outer_index = 0

        while outer_index < total_points - 1:
            inner_index = outer_index + 1
            while inner_index < total_points:
                first_point_x = sorted_points[outer_index].x
                first_point_y = sorted_points[outer_index].y
                second_point_x = sorted_points[inner_index].x
                second_point_y = sorted_points[inner_index].y

                condition1 = first_point_x <= second_point_x
                condition2 = first_point_y >= second_point_y

                if condition1 and condition2:
                    is_valid_pair = True
                    middle_index = outer_index + 1
                    while middle_index < inner_index:
                        mid_point_x = sorted_points[middle_index].x
                        mid_point_y = sorted_points[middle_index].y

                        inside_x_range = first_point_x <= mid_point_x <= second_point_x
                        inside_y_range = second_point_y <= mid_point_y <= first_point_y

                        if inside_x_range and inside_y_range:
                            is_valid_pair = False
                            break
                        middle_index += 1

                    if is_valid_pair:
                        pair_count += 1
                inner_index += 1
            outer_index += 1

        return pair_count