from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Initialize f with ones, dimensions n x (k+1)
        f = [[1] * (k + 1) for _ in range(n)]
        ans = 0
        for i, x in enumerate(nums):
            for h in range(k + 1):
                for j, y in enumerate(nums[:i]):
                    if x == y:
                        f[i][h] = max(f[i][h], f[j][h] + 1)
                    elif h > 0:
                        f[i][h] = max(f[i][h], f[j][h - 1] + 1)
            ans = max(ans, f[i][k])
        return ans