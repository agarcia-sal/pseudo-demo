from typing import List, Tuple

class Solution:
    def largestSquareArea(self, bottomLeft: List[Tuple[int, int]], topRight: List[Tuple[int, int]]) -> int:
        def intersecting_square_area(bl1: Tuple[int, int], tr1: Tuple[int, int], bl2: Tuple[int, int], tr2: Tuple[int, int]) -> int:
            def maximum(a: int, b: int) -> int:
                return a if a > b else b

            def minimum(a: int, b: int) -> int:
                return a if a < b else b

            x_left = maximum(bl1[0], bl2[0])
            x_right = minimum(tr1[0], tr2[0])
            y_bottom = maximum(bl1[1], bl2[1])
            y_top = minimum(tr1[1], tr2[1])

            if not (x_left < x_right) or (y_bottom >= y_top):
                return 0

            length_side = minimum(x_right - x_left, y_top - y_bottom)
            return length_side * length_side

        highest_area = 0
        amount = len(bottomLeft)

        def loop_outer(idx_outer: int) -> None:
            nonlocal highest_area
            if idx_outer >= amount:
                return

            def loop_inner(idx_inner: int, current_max: int) -> int:
                if idx_inner >= amount:
                    return current_max
                area_calc = intersecting_square_area(bottomLeft[idx_outer], topRight[idx_outer], bottomLeft[idx_inner], topRight[idx_inner])
                updated_max = area_calc if area_calc > current_max else current_max
                return loop_inner(idx_inner + 1, updated_max)

            inter_max = loop_inner(idx_outer + 1, highest_area)
            if inter_max > highest_area:
                highest_area = inter_max
            loop_outer(idx_outer + 1)

        loop_outer(0)
        return highest_area