import math
import sys

class Solution:
    def minOperations(self, k: int) -> int:
        alpha = sys.maxsize
        beta = 1
        limit = int(math.isqrt(k)) + 1  # floor(sqrt(k)) + 1
        while beta < limit:
            gamma = (k + beta - 1) // beta  # integer division ceiling for k/beta
            delta = (beta - 1) + (gamma - 1)
            if delta < alpha:
                alpha = delta
            beta += 1
        return alpha