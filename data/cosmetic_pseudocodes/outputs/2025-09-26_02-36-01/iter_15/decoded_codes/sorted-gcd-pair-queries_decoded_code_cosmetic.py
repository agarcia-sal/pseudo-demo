from typing import List
from collections import defaultdict

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        alpha = nums
        beta = queries
        gamma = 0
        for z in alpha:
            if z > gamma:
                gamma = z

        delta = defaultdict(int)
        for x in alpha:
            delta[x] += 1

        epsilon = [0] * (gamma + 1)

        # Precompute counts related to gcd values based on multiples
        for index_r in range(gamma, 0, -1):
            u = 0
            v = index_r
            while v <= gamma:
                u += delta[v]
                epsilon[index_r] -= epsilon[v]
                v += index_r
            epsilon[index_r] += (u * (u - 1)) // 2

        accumulation_s = [0] * (gamma + 1)
        for i in range(1, gamma + 1):
            accumulation_s[i] = accumulation_s[i - 1] + epsilon[i]

        omega_result = []
        for phi in beta:
            left, right = 1, gamma
            while left <= right:
                mid = (left + right) // 2
                if accumulation_s[mid] <= phi:
                    left = mid + 1
                else:
                    right = mid - 1
            omega_result.append(left)

        return omega_result