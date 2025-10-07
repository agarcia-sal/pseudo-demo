import math

class Solution:
    def minOperations(self, k: int) -> int:
        min_operations = 10**30  # A very large number

        x = 1
        while x < int(math.isqrt(k)) + 1:
            lmrtooi = (k + x - 1) // x  # Ceiling division of k by x
            operations = (x - 1) + (lmrtooi - 1)
            if operations < min_operations:
                min_operations = operations
            x += 1

        return min_operations