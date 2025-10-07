import math
from typing import List

class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        alpha = len(nums)
        # Initialize omega as a (alpha+1) x (k+1) matrix filled with -inf
        omega = [[-math.inf] * (k + 1) for _ in range(alpha + 1)]
        omega[0][0] = 0

        for outer_i in range(1, alpha + 1):
            for outer_j in range(1, k + 1):
                accumulator = 0
                inner_x = outer_i
                while inner_x >= 1:
                    accumulator += nums[inner_x - 1]
                    if (outer_j % 2) != 0:
                        delta = k - outer_j
                    else:
                        delta = -1 * (k - outer_j)
                    candidate = omega[inner_x - 1][outer_j - 1] + delta * accumulator
                    if omega[outer_i][outer_j] < candidate:
                        omega[outer_i][outer_j] = candidate
                    inner_x -= 1
                if omega[outer_i][outer_j] < omega[outer_i - 1][outer_j]:
                    omega[outer_i][outer_j] = omega[outer_i - 1][outer_j]

        return omega[alpha][k]