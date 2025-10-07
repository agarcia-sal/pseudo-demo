from typing import List, Tuple

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[int]:
        n = len(nums)
        xor_values = [[0] * n for _ in range(n)]
        max_xors = [[0] * n for _ in range(n)]

        for start in range(n - 1, -1, -1):
            xor_values[start][start] = nums[start]
            max_xors[start][start] = nums[start]
            for end in range(start + 1, n):
                xor_values[start][end] = xor_values[start][end - 1] ^ xor_values[start + 1][end]
                max_xors[start][end] = max(
                    xor_values[start][end], 
                    max_xors[start][end - 1], 
                    max_xors[start + 1][end]
                )

        result = []
        for l, r in queries:
            result.append(max_xors[l][r])

        return result