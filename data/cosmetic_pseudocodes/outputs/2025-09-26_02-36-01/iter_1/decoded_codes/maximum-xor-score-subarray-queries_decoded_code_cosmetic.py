from typing import List, Tuple

class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[int]:
        length = len(nums)
        f = [[0] * length for _ in range(length)]
        g = [[0] * length for _ in range(length)]

        for start in range(length - 1, -1, -1):
            f[start][start] = nums[start]
            g[start][start] = nums[start]

            end = start + 1
            while end < length:
                leftXor = f[start][end - 1]
                rightXor = f[start + 1][end]
                f[start][end] = leftXor ^ rightXor

                currentXor = f[start][end]
                prevMaxLeft = g[start][end - 1]
                prevMaxRight = g[start + 1][end]
                g[start][end] = max(currentXor, prevMaxLeft, prevMaxRight)

                end += 1

        return [g[l][r] for l, r in queries]