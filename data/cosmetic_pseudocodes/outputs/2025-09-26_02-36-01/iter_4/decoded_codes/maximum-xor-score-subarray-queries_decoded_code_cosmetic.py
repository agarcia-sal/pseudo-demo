class Solution:
    def maximumSubarrayXor(self, nums, queries):
        length = len(nums)
        f = [[0] * length for _ in range(length)]
        g = [[0] * length for _ in range(length)]

        for i in range(length - 1, -1, -1):
            f[i][i] = nums[i]
            g[i][i] = nums[i]
            for j in range(i + 1, length):
                f[i][j] = f[i][j - 1] ^ f[i + 1][j]
                candidate1 = f[i][j]
                candidate2 = g[i][j - 1]
                candidate3 = g[i + 1][j]
                g[i][j] = candidate1
                if candidate2 > g[i][j]:
                    g[i][j] = candidate2
                if candidate3 > g[i][j]:
                    g[i][j] = candidate3

        results = []
        for l, r in queries:
            results.append(g[l][r])

        return results