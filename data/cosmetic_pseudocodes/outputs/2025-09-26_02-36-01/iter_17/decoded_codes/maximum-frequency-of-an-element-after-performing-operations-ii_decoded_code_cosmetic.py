from collections import defaultdict
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        alpha = defaultdict(int)
        beta = defaultdict(int)
        for current in nums:
            alpha[current] += 1
            beta[current] += 0
            beta[current - k] += 1
            beta[current + k + 1] -= 1

        result = 0
        accumulator = 0
        sortedItems = sorted(beta.items())
        for key, value in sortedItems:
            accumulator += value
            minimumCandidate = accumulator if accumulator < alpha.get(key, 0) + numOperations else alpha.get(key, 0) + numOperations
            result = minimumCandidate if minimumCandidate > result else result
        return result