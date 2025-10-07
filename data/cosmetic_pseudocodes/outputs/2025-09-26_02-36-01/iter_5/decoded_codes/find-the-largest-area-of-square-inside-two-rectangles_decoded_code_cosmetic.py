from typing import List, Tuple

class Solution:
    def largestSquareArea(self, bottomLeft: List[Tuple[int, int]], topRight: List[Tuple[int, int]]) -> int:
        def intersecting_square_area(bl_one: Tuple[int, int], tr_one: Tuple[int, int],
                                    bl_two: Tuple[int, int], tr_two: Tuple[int, int]) -> int:
            left_edge = max(bl_one[0], bl_two[0])
            right_edge = min(tr_one[0], tr_two[0])
            lower_edge = max(bl_one[1], bl_two[1])
            upper_edge = min(tr_one[1], tr_two[1])

            if not (right_edge > left_edge and upper_edge > lower_edge):
                return 0

            width_candidate = right_edge - left_edge
            height_candidate = upper_edge - lower_edge

            side_length = min(width_candidate, height_candidate)
            area_of_square = side_length * side_length
            return area_of_square

        max_area_found = 0
        total_squares = len(bottomLeft)

        def iterate_j(i_idx: int, j_idx: int, current_max: int) -> int:
            if j_idx >= total_squares:
                return current_max
            curr_area = intersecting_square_area(bottomLeft[i_idx], topRight[i_idx], bottomLeft[j_idx], topRight[j_idx])
            new_max = max(current_max, curr_area)
            return iterate_j(i_idx, j_idx + 1, new_max)

        def iterate_i(i_idx: int, accumulated_max: int) -> int:
            if i_idx >= total_squares - 1:
                return accumulated_max
            max_after_j = iterate_j(i_idx, i_idx + 1, accumulated_max)
            return iterate_i(i_idx + 1, max_after_j)

        max_area_found = iterate_i(0, max_area_found)
        return max_area_found