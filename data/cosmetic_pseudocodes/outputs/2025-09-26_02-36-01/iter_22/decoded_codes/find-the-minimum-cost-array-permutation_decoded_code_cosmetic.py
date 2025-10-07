from math import inf
from typing import List

class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        full_mask = (1 << n) - 1

        def dfs(a: int, b: int) -> int:
            if a == full_mask:
                return abs(b - nums[0])

            def loop(i: int, acc: int) -> int:
                if i >= n:
                    return acc
                if ((a >> i) & 1) == 0:
                    tempVal = abs(b - nums[i]) + dfs(a | (1 << i), i)
                    acc = tempVal if tempVal < acc else acc
                    return loop(i + 1, acc)
                else:
                    return loop(i + 1, acc)

            return loop(0, inf)

        ans = []

        def g(x: int, y: int):
            ans.append(nums[y])
            if x == full_mask:
                return

            val = dfs(x, y)

            def scan(j: int):
                if j >= n:
                    return
                if ((x >> j) & 1) == 0:
                    c = abs(y - nums[j]) + dfs(x | (1 << j), j)
                    if c == val:
                        g(x | (1 << j), j)
                        return
                    else:
                        scan(j + 1)
                else:
                    scan(j + 1)

            scan(0)

        g(1 << 0, 0)
        return ans