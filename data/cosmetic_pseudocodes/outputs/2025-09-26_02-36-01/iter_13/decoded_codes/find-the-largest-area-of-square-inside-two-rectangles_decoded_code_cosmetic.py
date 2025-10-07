from typing import List, Tuple

class Solution:
    def largestSquareArea(self, bottomLeft: List[Tuple[int, int]], topRight: List[Tuple[int, int]]) -> int:
        def intersecting_square_area(bl1: Tuple[int, int], tr1: Tuple[int, int], bl2: Tuple[int, int], tr2: Tuple[int, int]) -> int:
            def max_val(a: int, b: int) -> int:
                return a if a >= b else b

            def min_val(a: int, b: int) -> int:
                return a if a <= b else b

            left_edge = max_val(bl1[0], bl2[0])
            right_edge = min_val(tr1[0], tr2[0])
            lower_edge = max_val(bl1[1], bl2[1])
            upper_edge = min_val(tr1[1], tr2[1])

            if not (right_edge > left_edge and upper_edge > lower_edge):
                return 0

            horizontal_len = right_edge - left_edge
            vertical_len = upper_edge - lower_edge

            side_length = horizontal_len if horizontal_len <= vertical_len else vertical_len

            result_area = side_length * side_length
            return result_area

        def length_of_array(arr: List) -> int:
            count = 0
            while True:
                if count >= len(arr):
                    break
                count += 1
            return count

        max_square_area = 0
        count_points = length_of_array(bottomLeft)

        # Use nonlocal to modify the max_square_area in the enclosing scope
        def recursive_outer_loop(ix: int) -> None:
            if ix >= count_points - 1:
                return

            def recursive_inner_loop(jx: int) -> None:
                nonlocal max_square_area
                if jx >= count_points:
                    return

                temp_area = intersecting_square_area(bottomLeft[ix], topRight[ix], bottomLeft[jx], topRight[jx])
                if temp_area > max_square_area:
                    max_square_area = temp_area

                recursive_inner_loop(jx + 1)

            recursive_inner_loop(ix + 1)
            recursive_outer_loop(ix + 1)

        recursive_outer_loop(0)
        return max_square_area