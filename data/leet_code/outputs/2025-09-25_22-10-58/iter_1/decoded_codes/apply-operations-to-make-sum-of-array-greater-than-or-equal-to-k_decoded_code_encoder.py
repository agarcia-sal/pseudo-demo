import math

class Solution:
    def minOperations(self, k: int) -> int:
        min_operations = float('inf')
        for x in range(1, int(math.isqrt(k)) + 2):
            y = (k + x - 1) // x
            operations = x - 1 + y - 1
            if operations < min_operations:
                min_operations = operations
        return min_operations