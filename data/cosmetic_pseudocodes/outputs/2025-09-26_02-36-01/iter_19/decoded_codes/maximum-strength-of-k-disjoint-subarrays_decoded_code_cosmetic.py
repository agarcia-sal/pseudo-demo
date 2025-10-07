from math import inf
from typing import List

class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        lenZ = len(nums)
        # Initialize DP table with -inf
        tabA = [[-inf] * (k + 1) for _ in range(lenZ + 1)]
        tabA[0][0] = 0

        w = 1
        while w <= lenZ:
            x = 1
            while x <= k:
                tempSum = 0
                v = w
                while v >= 1:
                    tempSum += nums[v - 1]
                    if (x % 2) == 1:
                        dir = (k - x)
                    else:
                        dir = -(k - x)
                    tabA[w][x] = max(tabA[w][x], tabA[v - 1][x - 1] + dir * tempSum)
                    v -= 1
                tabA[w][x] = max(tabA[w][x], tabA[w - 1][x])
                x += 1
            w += 1

        return tabA[lenZ][k]