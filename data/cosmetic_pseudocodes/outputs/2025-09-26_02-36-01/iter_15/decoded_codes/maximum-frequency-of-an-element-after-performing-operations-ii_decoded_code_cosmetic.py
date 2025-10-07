from collections import defaultdict
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        alpha = defaultdict(int)
        beta = defaultdict(int)
        for omega in nums:
            alpha[omega] += 1
            beta[omega] += 0
            beta[omega - k] += 1
            beta[omega + k + 1] += -1

        rho = 0
        sigma = 0
        delta = sorted(beta.keys())

        def processKeys(i: int):
            nonlocal rho, sigma
            if i >= len(delta):
                return
            sigma += beta[delta[i]]
            rho = max(rho, min(sigma, alpha[delta[i]] + numOperations))
            processKeys(i + 1)

        processKeys(0)
        return rho