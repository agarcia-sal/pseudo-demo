from itertools import combinations
from math import inf

class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        MODULO = 1_000_000_007
        accumulated_sum = 0

        for subset in combinations(nums, k):
            smallest_diff = inf
            for pos1 in range(k - 1):
                for pos2 in range(pos1 + 1, k):
                    diff = abs(subset[pos1] - subset[pos2])
                    if diff < smallest_diff:
                        smallest_diff = diff
            accumulated_sum += smallest_diff
            accumulated_sum %= MODULO

        return accumulated_sum