from typing import List, Tuple

class Solution:
    def largestSquareArea(self, bottomLeft: List[Tuple[int, int]], topRight: List[Tuple[int, int]]) -> int:
        def intersecting_square_area(bl1: Tuple[int, int], tr1: Tuple[int, int], bl2: Tuple[int, int], tr2: Tuple[int, int]) -> int:
            # Calculate the overlapping region's boundaries along x and y axes
            G = bl1[0] if bl1[0] > bl2[0] else bl2[0]
            H = tr1[0] if tr1[0] < tr2[0] else tr2[0]
            M = bl1[1] if bl1[1] > bl2[1] else bl2[1]
            N = tr1[1] if tr1[1] < tr2[1] else tr2[1]

            # If no intersection, return 0
            if not (G < H and M < N):
                return 0

            diff_x = H - G
            diff_y = N - M

            # The largest square side length fitting in the overlapping rectangle
            d = diff_x if diff_x < diff_y else diff_y
            return d * d

        alpha = 0
        length_counter = len(bottomLeft)

        for i in range(length_counter):
            for j in range(i + 1, length_counter):
                temp_var = intersecting_square_area(bottomLeft[i], topRight[i], bottomLeft[j], topRight[j])
                if temp_var > alpha:
                    alpha = temp_var

        return alpha