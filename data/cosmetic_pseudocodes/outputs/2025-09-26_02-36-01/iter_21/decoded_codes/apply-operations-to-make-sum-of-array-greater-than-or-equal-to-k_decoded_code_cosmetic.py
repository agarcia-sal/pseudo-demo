class Solution:
    def minOperations(self, k: int) -> int:
        R0 = float('inf')
        R1 = 1
        while R1 * R1 <= k:
            R2 = (k + R1 - 1) // R1
            R3 = (R1 - 1) + (R2 - 1)
            if R3 < R0:
                R0 = R3
            R1 += 1
        return R0