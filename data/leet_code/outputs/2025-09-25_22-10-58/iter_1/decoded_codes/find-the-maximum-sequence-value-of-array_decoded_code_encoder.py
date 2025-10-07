class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:
        m = 1 << 7  # 2^7
        n = len(nums)
        # Initialize 3D boolean DP arrays with False
        f = [[[False] * m for _ in range(k + 2)] for _ in range(n + 1)]
        f[0][0][0] = True

        for i in range(n):
            for j in range(k + 1):
                for x in range(m):
                    if f[i][j][x]:
                        # Not take nums[i]
                        f[i + 1][j][x] = True
                        # Take nums[i]
                        if j + 1 <= k + 1:
                            f[i + 1][j + 1][x | nums[i]] = True

        g = [[[False] * m for _ in range(k + 2)] for _ in range(n + 1)]
        g[n][0][0] = True

        for i in range(n, 0, -1):
            for j in range(k + 1):
                for y in range(m):
                    if g[i][j][y]:
                        # Not take nums[i-1]
                        g[i - 1][j][y] = True
                        # Take nums[i-1]
                        if j + 1 <= k + 1:
                            g[i - 1][j + 1][y | nums[i - 1]] = True

        ans = 0
        for i in range(k, n - k + 1):
            for x in range(m):
                if f[i][k][x]:
                    for y in range(m):
                        if g[i][k][y]:
                            ans = max(ans, x ^ y)
        return ans