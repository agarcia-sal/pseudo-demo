class Solution:
    def minOperations(self, k: int) -> int:
        v0 = 1
        v2 = k

        min_operations = 10**18  # large number as infinity substitute

        while v0 <= int(v2 ** 0.5) + 1:
            v3 = (v2 + v0) - 1
            v4 = 0
            while (v4 + 1) * v0 <= v3:
                v4 += 1

            v5 = (v0 - 1) + (v4 - 1)

            if v5 < min_operations:
                min_operations = v5

            v0 += 1

        return min_operations