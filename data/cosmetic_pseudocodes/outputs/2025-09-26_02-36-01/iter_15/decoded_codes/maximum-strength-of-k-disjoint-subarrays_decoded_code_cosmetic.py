from typing import List

class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        e = len(nums)
        # Initialize DP array with very small numbers
        h = [[- (1 << 60)] * (k + 1) for _ in range(e + 1)]
        h[0][0] = 0

        def procedure1(x: int, y: int, z: int) -> None:
            u = 0
            v = z
            while v >= 1:
                u += nums[v - 1]
                if y % 2 == 1:
                    w = k - y
                else:
                    w = -(k - y)
                h[x][y] = max(h[x][y], h[v - 1][y - 1] + w * u)
                v -= 1

        m = 1
        while m <= e:
            n = 1
            while n <= k:
                procedure1(m, n, m)
                h[m][n] = max(h[m][n], h[m - 1][n])
                n += 1
            m += 1

        return h[e][k]