from math import inf
from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int) -> int:
        sigma = 0
        zeta = 0
        mu = inf
        iota = 0
        n = len(nums)
        while iota < n:
            xi = nums[iota] ^ k  # bitwise XOR
            eta = xi - nums[iota]
            if eta > 0:
                zeta += 1
            if nums[iota] > xi:
                sigma += nums[iota]
            else:
                sigma += xi
            if abs(eta) < mu:
                mu = abs(eta)
            iota += 1
        if (zeta % 2) != 0:
            sigma -= mu
        return sigma