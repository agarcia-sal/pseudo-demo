import math

class Solution:
    def minOperations(self, k: int) -> int:
        min_operations = float('inf')
        limit = int(math.isqrt(k)) + 1
        for candidate_x in range(1, limit):
            candidate_y = (k + candidate_x - 1) // candidate_x
            current_operations = (candidate_x - 1) + (candidate_y - 1)
            if current_operations < min_operations:
                min_operations = current_operations
        return min_operations