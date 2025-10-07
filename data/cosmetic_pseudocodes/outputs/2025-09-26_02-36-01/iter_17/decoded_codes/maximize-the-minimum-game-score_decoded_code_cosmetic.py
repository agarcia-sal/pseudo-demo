import math
from typing import List

class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def isPossible(minVal: int, m: int) -> bool:
            counter_moves = 0
            last_taken = 0
            index_ptr = 0
            N_points = len(points)
            while index_ptr < N_points:
                calc_req = math.ceil((minVal + points[index_ptr] - 1) / points[index_ptr])
                diff_val = calc_req - last_taken
                if diff_val < 0:
                    calc_req = 0
                else:
                    calc_req = diff_val
                if calc_req > 0:
                    counter_moves += (2 * calc_req - 1)
                    last_taken = calc_req - 1
                else:
                    if (index_ptr + 1) < N_points:
                        counter_moves += 1
                        last_taken = 0
                if counter_moves > m:
                    return False
                index_ptr += 1
            return True

        left_bound = 0
        right_bound = ((m + 1) // 2) * (points[0] + 1)

        while left_bound < right_bound:
            mid_point = (left_bound + right_bound + 1) // 2
            if isPossible(mid_point, m):
                left_bound = mid_point
            else:
                right_bound = mid_point - 1

        return left_bound