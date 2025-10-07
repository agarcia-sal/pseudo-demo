import math

class Solution:
    def minOperations(self, k: int) -> int:
        minimalCount = float('inf')
        currentIndex = 1
        limit = math.isqrt(k) + 1
        while currentIndex <= limit:
            dividend = k + currentIndex - 1
            quotient = dividend // currentIndex
            currentOps = (currentIndex - 1) + (quotient - 1)
            if currentOps < minimalCount:
                minimalCount = currentOps
            currentIndex += 1
        return minimalCount